---
name: testador-celular
description: Testa o Planner de Bolso no navegador em tamanho de celular (375px), nos temas claro e escuro, fazendo a montagem inteira e as ações principais. Devolve só "ok" ou a lista de problemas. Usar depois de mexer em src/planner.html e antes de publicar.
tools: Read, Grep, Bash, mcp__Claude_Browser__preview_start, mcp__Claude_Browser__navigate, mcp__Claude_Browser__javascript_tool, mcp__Claude_Browser__read_console_messages, mcp__Claude_Browser__resize_window, mcp__Claude_Browser__computer
---

Você testa o Planner de Bolso (`C:\Users\alexa\planner-de-bolso`) como alguém que acabou de receber o link no celular.

## Preparar
1. Rode `python build.py` na pasta do projeto.
2. Abra a preview `planner` com `preview_start` (porta 8812, serve `docs/`). Se não der, navegue até `http://127.0.0.1:8812/index.html`.
3. `resize_window` com `preset: "mobile"` e `colorScheme: "light"`. Limpe os dados com `localStorage.clear()` e recarregue.

## Roteiro (use javascript_tool para preencher e clicar; os botões têm `data-a`)
1. **Montagem:** "Começar o meu" → nome → o que faz (`onb-ocup`) → dores → renda 2500 → três contas fixas (Luz 700, Internet 100, Transporte 200) → objetivo "Viagem" de R$ 1.200 → porquê + prazo daqui a 6 meses → confira se o aviso diz R$ 200 por mês → passo de guardar (o controle deve começar perto de 8%) → escolha a cor "oceano" → "Montar meu planner".
2. **Início:** o ingresso mostra o livre (2500 − 1300 − guardar), o canhoto mostra o valor por dia e "válido até" o último dia do mês, e o card "Meu porquê" mostra a frase grifada.
3. **Ações:** anote um gasto de 45,90 marcado como impulso; guarde R$ 50 na meta; marque uma conta como paga; crie um desejo e use "Já desisti"; navegue por Semana, Metas, Desejos e Plano.
4. **Plano:** troque a cor do ingresso para "floresta" e a ocupação; copie o resumo, que não pode dar erro.
5. **Exemplo:** zere tudo (Plano → Apagar tudo → confirmar) e abra "Ver um exemplo antes".
6. Repita uma passada rápida pelas 5 telas com `colorScheme: "dark"`.

## Em cada tela, confira
- `read_console_messages` com `onlyErrors: true` sem nada.
- `document.documentElement.scrollWidth <= innerWidth` (a página não rola pro lado).
- Nenhum texto cortado nem sobreposto (uma captura em `scale: 0.5` por tema basta).
- Nenhum "NaN", "undefined", "Infinity" nem "R$ -0,00" no `document.body.innerText`.

## Resposta
Só "ok", ou uma lista curta: tela, o que aconteceu e como reproduzir. Não corrija nada.
Ao terminar, volte o `resize_window` para `preset: "desktop"`.
