"""Gera docs/index.html (site independente, servido pelo GitHub Pages ou aberto direto no celular)
a partir de src/planner.html (o formato do link do Claude, sem <html>/<head>/<body>).

Uso:
  python build.py              gera docs/index.html
  python build.py --downloads  também copia para Downloads/planner-de-bolso/index.html (para mandar no WhatsApp)
"""
import re
import shutil
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
SRC = RAIZ / "src" / "planner.html"
DOCS = RAIZ / "docs"

src = SRC.read_text(encoding="utf-8")
fim_style = src.index("</style>") + len("</style>")
cabeca = (
    "<!doctype html>\n<html lang=\"pt-BR\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\">\n"
)
saida = cabeca + src[:fim_style] + "\n</head>\n<body>\n" + src[fim_style:] + "\n</body>\n</html>\n"

# Trava de segurança: o arquivo é público, então nada de dado pessoal real nem código de backup.
proibidos = {
    "CPF": r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b",
    "código de backup": r"PDB1:[A-Za-z0-9+/=]{40,}",
    "e-mail": r"[\w.+-]+@(?!example\.)[\w-]+\.[\w.]+",
}
for nome, padrao in proibidos.items():
    if re.search(padrao, saida):
        sys.exit(f"Parei: achei {nome} no planner. Tire antes de publicar.")

DOCS.mkdir(exist_ok=True)
(DOCS / "index.html").write_text(saida, encoding="utf-8")
(DOCS / ".nojekyll").write_text("", encoding="utf-8")
print(f"docs/index.html gerado ({len(saida.encode('utf-8')) // 1024} KB)")

if "--downloads" in sys.argv:
    destino = Path.home() / "Downloads" / "planner-de-bolso"
    destino.mkdir(parents=True, exist_ok=True)
    shutil.copy(DOCS / "index.html", destino / "index.html")
    print(f"copiado para {destino / 'index.html'}")
