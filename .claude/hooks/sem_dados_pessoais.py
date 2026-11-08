"""Hook (PreToolUse em Write/Edit): o planner é compartilhado com outras pessoas, então nenhum dado pessoal
real pode entrar no código. Barra CPF, telefone, e-mail e código de backup (PDB1:, que carrega os gastos
de alguém). Exit 2 = a edição não acontece e o Claude recebe o motivo.
"""
import json
import re
import sys

try:
    dados = json.loads(sys.stdin.buffer.read().decode("utf-8-sig"))
except Exception:
    sys.exit(0)
ti = dados.get("tool_input") or {}
caminho = (ti.get("file_path") or "").replace("\\", "/").lower()
if "/.claude/" in caminho or caminho.endswith(".md"):
    sys.exit(0)  # regras e documentação podem citar os padrões
texto = (ti.get("content") or "") + "\n" + (ti.get("new_string") or "")

padroes = {
    "CPF": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
    "telefone": r"\(?\b\d{2}\)?\s?9\d{4}-?\d{4}\b",
    "e-mail": r"[\w.+-]+@(?!example\.)[\w-]+\.[a-z]{2,}",
    "código de backup": r"PDB1:[A-Za-z0-9+/=]{40,}",
}
achados = [nome for nome, p in padroes.items() if re.search(p, texto, re.I)]
if achados:
    print("Bloqueado: parece ter " + ", ".join(achados) + " no planner. Ele é compartilhado; "
          "use dados de exemplo (como a 'Ana') e nunca dados reais de quem usa.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
