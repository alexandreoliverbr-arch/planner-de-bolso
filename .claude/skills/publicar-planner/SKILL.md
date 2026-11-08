---
name: publicar-planner
description: Publica uma versão nova do Planner de Bolso nos três lugares (link do Claude, site do GitHub Pages e arquivo em Downloads), depois de testar. Usar quando o Alexandre pedir "/publicar-planner" ou "publica o planner".
disable-model-invocation: true
---

# Publicar o Planner de Bolso

Siga na ordem. Pare e avise se algum passo falhar.

1. **Gerar o site:** `python build.py --downloads`. Isso gera `docs/index.html`, copia para `Downloads/planner-de-bolso/index.html` e para se achar dado pessoal.
2. **Testar:** chame o agente `testador-celular`. Se ele não responder "ok", corrija antes de seguir. Se a mudança mexeu em conta ou texto, chame também o `revisor-de-contas`.
3. **Link do Claude:** publique com a ferramenta Artifact. Use `file_path` = `src/planner.html` e `url` = `https://claude.ai/artifact/LSDFFmNpcFAFiPDgRR7NuP`, com uma `description` de uma frase. Se a publicação disser que não leu o link nesta conversa, faça antes `action: "read"` nessa url.
4. **Git:** faça um commit com o que mudou, em português e no padrão do repositório.
5. **GitHub Pages:** `git push`. O site https://alexandreoliverbr-arch.github.io/planner-de-bolso/ atualiza em 1 ou 2 minutos. O `gh` fica em `C:\Program Files\GitHub CLI\gh.exe` (fora do PATH do bash). Antes de enviar, confira que `git config user.email` é o e-mail noreply do GitHub.
6. **Contar ao Alexandre** onde ficou cada coisa e o que mudou para quem usa, em linguagem simples. Lembre que os dados de quem já usa continuam no celular de cada pessoa: uma versão nova não apaga nada.
