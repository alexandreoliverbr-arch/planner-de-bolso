---
name: identidade-planner
description: Identidade visual e tom do Planner de Bolso (ingresso com canhoto, cores por pessoa, fontes, textos de amiga). Carregar antes de criar ou mudar qualquer tela, componente, cor, texto ou animação em src/planner.html.
user-invocable: false
---

# Identidade do Planner de Bolso

## A ideia
Quem usa está juntando dinheiro pra algo que importa pra ela. O cartão principal é um **ingresso**: a parte grande mostra o livre do mês, e o **canhoto destacável** (separado por picote, com dois furinhos feitos por `mask`) mostra quanto dá pra gastar por dia e "válido até" o último dia do mês. **O ingresso é o único elemento ousado da tela.** O resto fica quieto.

O segundo elemento com personalidade é o **marca-texto**, uma lembrança do caderno de papel. Ele grifa o nome no "Oi, Fulana" e o **porquê** da meta principal na tela inicial. Use só nesses dois lugares.

## Cores
- Tokens no `:root`: `--plum` (ingresso e botões), `--plum-2` (destaque), `--plum-soft`, `--plum-ink`, `--stub` (canhoto), `--marca` (grifo), `--save` (verde de guardar), `--spend` (vermelho de gasto), `--gold`/`--gold-soft` (dicas e alertas leves).
- Cada pessoa escolhe a cor do ingresso, gravada em `perfil.vibe` e aplicada com `data-vibe` no `<html>`: **uva** (padrão, violeta + amarelo), **chiclete** (rosa + menta), **oceano** (azul + coral), **pôr do sol** (laranja-queimado + amarelo), **floresta** (verde + rosa). Toda cor nova precisa funcionar nas 5 vibes e nos dois temas: valores claros no `:root[data-vibe=…]`, escuros no `@media (prefers-color-scheme: dark)` com `:not([data-theme="light"])` e de novo em `[data-theme="dark"]`.
- Componente nenhum usa cor literal. Exceções: as cores das categorias (tons médios que funcionam nos dois temas) e o branco translúcido dentro do ingresso.

## Tipografia
- **Big Shoulders Display** (estreita, de letreiro de show): números, títulos e o porquê. Pesos 700 e 800.
- **Instrument Sans**: todo o resto. Sempre em frase normal.
- Números com `font-variant-numeric: tabular-nums`.

## Não fazer
- Rótulo em CAIXA ALTA, emoji em título de seção, "·" separando informações, `→` em botão, degradê decorativo, borda e sombra iguais em todo cartão.
- Animação de entrada em cada seção. Movimento só como resposta a uma ação: abrir a folha de baixo, confete ao guardar, bater uma meta ou pagar todas as contas.
- Foto, letra de música, logo ou nome de artista ou marca no código. O objetivo de cada pessoa vem das respostas dela.

## Tom dos textos
- Amiga que entende de dinheiro: frases curtas, sem bronca, sem julgamento. "Anotado!", "Segura firme até virar o mês, você consegue 💛".
- O botão diz exatamente o que faz ("Guardar", "Esperar 24h"), e o aviso confirma com o mesmo verbo.
- Linguagem neutra quando der ("Faço freela ou trabalho por conta" em vez de "autônoma").
- Nunca indicar investimento, banco ou produto financeiro.

## Estrutura técnica
- Telas: `inicio`, `semana`, `metas`, `desejos`, `plano` (rotas `#nome`). Montagem em 9 passos (`renderOnb`). Folhas de baixo com `abrir()`, avisos com `toast()`, confete com `confete(n)`.
- Ações por `data-a` (objeto `A`) e formulários por `data-form` (objeto `F`).
- Não existe `alert`/`confirm`/`prompt` (o link do Claude bloqueia): para confirmar, use `confirmar(titulo, texto, botao, fn)`.
- Todo acesso ao `localStorage` fica dentro de try/catch.
