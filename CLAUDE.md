# Planner de Bolso

App de finanças pessoais para celular, feito pelo Alexandre para uma amiga, para ele e para quem mais quiser usar. Projeto pessoal, **separado do robo-cubbo** (não misturar arquivos, memória nem regras de lá).

## Onde está cada coisa
- `src/planner.html`: o app inteiro (HTML + CSS + JS num arquivo só, sem biblioteca). Está no formato do link do Claude: sem `<html>`, `<head>` nem `<body>`. **É o único arquivo que se edita.**
- `build.py`: gera `docs/index.html`, a versão independente que abre em qualquer navegador e que o GitHub Pages serve. `python build.py --downloads` também copia para `Downloads/planner-de-bolso/` (para mandar no WhatsApp).
- Link do Claude (privado até ele compartilhar): https://claude.ai/artifact/LSDFFmNpcFAFiPDgRR7NuP. Para republicar, use a skill `/publicar-planner`.
- Teste local: `.claude/launch.json` → preview `planner` (porta 8812, serve `docs/`).

## Como o app funciona
- Cada pessoa responde às perguntas da montagem: nome, o que faz, maior dor de cabeça, renda, contas fixas, objetivo com valor, **porquê**, prazo, quanto guardar e a cor do ingresso. Nada vem pronto igual pra todo mundo: o objetivo e o porquê são da pessoa.
- Os dados ficam só no `localStorage` do aparelho (chave `planner-de-bolso-v1`). Não há servidor nem conta. O backup é um código `PDB1:` que a pessoa copia.
- As contas do mês: livre = renda − contas fixas − guardar. O valor por dia é o livre que sobra dividido pelos dias que faltam no mês, contando hoje. A semana vai de segunda a domingo, e o livre da semana é o livre do mês ÷ dias do mês × 7. Uma meta com prazo pede (alvo − guardado) ÷ meses até o prazo.

## Regras que não podem ser quebradas
- **Nada de dado pessoal real no código** (nomes reais, renda real, CPF, e-mail, código de backup). O exemplo usa "Ana". O `build.py` e o hook `sem_dados_pessoais.py` barram isso.
- **Nada de foto, letra de música, logo ou marca de artista ou empresa.** Se a pessoa gosta de um artista, ela escreve isso na meta dela.
- Tom de amiga: acolhedor, sem bronca, sem julgamento. **Nunca dar conselho de investimento** (não indicar produto, banco ou aplicação).
- Celular primeiro: tudo funciona em 375px, nos temas claro e escuro e com as 5 cores de ingresso. A página nunca pode rolar pro lado.
- Antes de mexer no visual, carregue a skill `identidade-planner`. Depois de mexer, rode o agente `testador-celular`. Se mexer em conta ou texto, rode também o `revisor-de-contas`.
