"""Hook (PostToolUse em Write/Edit): depois de editar um .html do planner, confere a sintaxe do JavaScript
com o node que vem no Playwright do robo-cubbo (esta máquina não tem node instalado). Erro = exit 2 com a
linha do .html, para corrigir na hora: um erro de sintaxe deixa o planner em branco no celular de quem usa.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CANDIDATOS = [
    shutil.which("node"),
    r"C:\Users\alexa\robo-cubbo\libs\playwright\driver\node.exe",
]
NODE = next((c for c in CANDIDATOS if c and Path(c).exists()), None)

try:
    dados = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
except Exception:
    sys.exit(0)
caminho = (dados.get("tool_input") or {}).get("file_path") or ""
if not caminho.lower().endswith(".html") or not NODE:
    sys.exit(0)
try:
    html = Path(caminho).read_text(encoding="utf-8")
except OSError:
    sys.exit(0)

erros = []
for m in re.finditer(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", html, re.S | re.I):
    codigo = "\n" * html.count("\n", 0, m.start(1)) + m.group(1)
    fd, nome = tempfile.mkstemp(suffix=".js")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(codigo)
    r = subprocess.run([NODE, "--check", nome], capture_output=True, text=True, encoding="utf-8", errors="replace")
    Path(nome).unlink(missing_ok=True)
    if r.returncode != 0:
        linhas = [l for l in r.stderr.splitlines() if l.strip()]
        onde = linhas[0].rsplit(":", 1)[-1] if linhas else "?"
        msg = next((l for l in linhas if "Error" in l), "")
        erros.append(f"linha {onde}: {msg}")
if erros:
    print(f"Erro de JavaScript em {caminho}:\n" + "\n".join(erros), file=sys.stderr)
    sys.exit(2)
sys.exit(0)
