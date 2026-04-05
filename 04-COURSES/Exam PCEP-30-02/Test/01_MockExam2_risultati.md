Ottimo lavoro. Ecco la correzione completa.

---

## Risultato: 22/25 — 88%

Miglioramento rispetto al primo test (84%). Tre errori, tutti su concetti precisi che vale la pena fissare.

---

## Domande errate

**Q11 — Risposta tua: A (14) — Risposta corretta: B (6)**

`0b1100 = 12`, `0b1010 = 10`. L'operatore `^` è XOR bit a bit: confronta ogni coppia di bit e restituisce 1 solo se i due bit sono diversi.

```
  1100  (12)
^ 1010  (10)
------
  0110  (6)
```

14 sarebbe il risultato di `|` (OR), non `^` (XOR). Da rivedere: la differenza tra OR e XOR.

---

**Q18 — Risposta tua: C (True) — Risposta corretta: B (2)**

In Python, `bool` è una sottoclasse di `int`: `True` vale `1` e `False` vale `0` nei contesti aritmetici. Quindi `True + True + False = 1 + 1 + 0 = 2`, un intero, non un booleano. Il risultato stampato è `2`.

---

**Q22 — Risposta tua: B, C, E — Risposta corretta: B, E (due risposte)**

La domanda chiedeva di selezionare esattamente due opzioni. Per le costanti PEP-8 prescrive `UPPER_CASE_WITH_UNDERSCORES`. Quindi `MAX_SPEED` e `MAXSPEED` sono entrambe accettabili come costanti (anche se `MAXSPEED` senza underscore è meno leggibile, non viola esplicitamente la regola). `max_speed` invece è la convenzione corretta per una variabile locale, non per una costante — quindi viola PEP-8 per una costante. Hai selezionato tre risposte invece di due: sul vero esame questo conta come risposta errata. Da ricordare: leggere con attenzione il numero di selezioni richiesto.

---

## Riepilogo errori

| # | Argomento | Problema |
|---|-----------|----------|
| Q11 | Operatori bitwise XOR vs OR | Confusione tra `^` e `\|` |
| Q18 | Aritmetica con bool | `True` si comporta come `1` in contesti numerici |
| Q22 | PEP-8 costanti + numero di selezioni | Selezionate tre opzioni invece di due |

---

## Andamento complessivo sui due test

| Test | Punteggio | Note |
|------|-----------|------|
| #1 | 21/25 — 84% | Errori su float precision, `//=`, indentazione, `int(input())` |
| #2 | 22/25 — 88% | Errori su XOR, bool arithmetic, PEP-8 costanti |

I concetti da consolidare prima dell'esame reale sono: operatori bitwise (specialmente XOR), comportamento aritmetico di `bool`, e la lettura attenta delle istruzioni per le domande a selezione multipla. Vuoi un terzo test, oppure una dispensa mirata su uno di questi argomenti?