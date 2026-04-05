# Risultati — Section 1 Mock Exam

**Punteggio: 21 / 25 (84%)**

---

## ❌ Errate (4)

**Q6** — Risposta data: D (`1`) — **Risposta corretta: B (`3`)**

`x //= 3` equivale a `x = x // 3`, cioè `10 // 3 = 3` (divisione intera). Il risultato è `3`, non `1`. Probabilmente hai confuso con `10 % 3 = 1`.

---

**Q9** — Risposta data: C — **Risposta corretta: B**

Python richiede indentazione coerente all'interno di un blocco, ma non impone esattamente 4 spazi: 2 spazi, tab, o qualsiasi numero consistente sono tecnicamente accettati dall'interprete. PEP-8 raccomanda 4 spazi, ma non è un requisito sintattico. Anche i tab sono ammessi (seppur sconsigliati). L'unica regola assoluta è la coerenza.

---

**Q10** — Risposta data: A (`True`) — **Risposta corretta: B (`False`)**

Questo è il classico trabocchetto sulla precisione dei float in IEEE 754. `0.1 + 0.2` produce `0.30000000000000004` in memoria, quindi il confronto `== 0.3` restituisce `False`. È uno dei punti esplicitamente citati nel syllabus alla voce 1.4 ("accuratezza dei float").

---

**Q12** — Risposta data: A — **Risposta corretta: B**

`input(int("Enter a number: "))` tenta di convertire la stringa prompt in int, lanciando un `ValueError` prima ancora di chiedere input all'utente. La forma corretta è `int(input("Enter a number: "))`: prima si legge la stringa, poi la si converte.

---

## Riepilogo per argomento

| Area | Esito |
|---|---|
| Keyword e indentazione (1.2) | ⚠️ Q9 errata |
| Operatori e tipi, float accuracy (1.4) | ⚠️ Q6, Q10 errate |
| Input/Output, type casting (1.5) | ⚠️ Q12 errata |

---

## Punti da ripassare

I tre errori genuini convergono su due temi precisi: la precisione dei float (1.4) e la distinzione tra operatori aritmetici simili (`//` vs `%`). Per Q12, il pattern `int(input(...))` è un idioma fondamentale che vale la pena fissare bene.