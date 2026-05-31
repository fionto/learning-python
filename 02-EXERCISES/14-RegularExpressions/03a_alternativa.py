import re

# DIZIONARIO DEI PATTERN (per avere una descrizione)
pattern1 = r'campione_(AB|BA)\.txt'      # Punto ESCAPATO → cerca punto letterale
pattern2 = r'campione_(AB|BA)?\.txt'     # (AB|BA) è opzionale + punto letterale
pattern3 = r'campione_(AB|BA).txt'       # Punto NON ESCAPATO → qualsiasi carattere

patterns = [pattern1, pattern2, pattern3]
nomi_patterns = [
    'Pattern 1: campione_(AB|BA)\\.txt  (punto letterale)',
    'Pattern 2: campione_(AB|BA)?\\.txt (AB/BA opzionale + punto letterale)',
    'Pattern 3: campione_(AB|BA).txt    (punto = qualsiasi carattere)'
]

samples = ['campione_AB.txt', 'campione_BA.txt', 'campione_.txt', 'campione.txt', 'campione_BA-txt']

print("=" * 80)
print("📚 CONFRONTO PATTERN REGEX: punto letterale (.) vs punto metacarattere (.)")
print("=" * 80)

print("\n🎯 LEGENDA:")
print("   ✅ = MATCH (nome accettato)")
print("   ❌ = NO MATCH (nome rifiutato)")
print("\n" + "-" * 80)

# Per ogni pattern, stampo una sezione
for idx, (pattern, descrizione) in enumerate(zip(patterns, nomi_patterns), 1):
    print(f"\n📌 {descrizione}")
    print("-" * 80)
    
    for sample in samples:
        match = re.search(pattern, sample)
        if match:
            print(f"   ✅ {sample:30} → MATCH trovato: '{match.group()}'")
        else:
            print(f"   ❌ {sample:30} → NESSUN match")
    
    print()  # riga vuota tra un pattern e l'altro

# RIEPILOGO FINALE CONFRONTO DIRETTO
print("\n" + "=" * 80)
print("🔍 ANALISI DELLE DIFFERENZE")
print("=" * 80)

print("\nQual è la differenza tra Pattern 1 e Pattern 3?")
print("-" * 80)
print("Pattern 1: campione_(AB|BA)\\.txt")
print("   • Il punto è ESCAPATO (\\.) → cerca il carattere punto LETTERALE")
print("   • 'campione_AB.txt' ✅   'campione_ABXtxt' ❌")
print()
print("Pattern 3: campione_(AB|BA).txt")
print("   • Il punto NON è escapato (.) → cerca QUALSIASI carattere")
print("   • 'campione_AB.txt' ✅   'campione_ABXtxt' ✅ (X matcha il punto)")
print("   • 'campione_BA-txt' ✅ (il trattino matcha il punto)")
print()

print("Cosa fa Pattern 2 in più?")
print("-" * 80)
print("Pattern 2: campione_(AB|BA)?\\.txt")
print("   • Il ? dopo (AB|BA) rende 'AB' o 'BA' OPZIONALI")
print("   • Quindi matcha ANCHE: 'campione_.txt' (senza AB o BA)")
print("   • Ma NON matcha: 'campione.txt' (manca underscore)")

print("\n" + "=" * 80)
print("💡 RIASSUNTO FINALE")
print("=" * 80)
print("""
• Pattern 1: Matcha SOLO 'campione_AB.txt' e 'campione_BA.txt' (punto letterale)
• Pattern 2: Matcha 'campione_AB.txt', 'campione_BA.txt' e 'campione_.txt' (AB/BA opzionali)
• Pattern 3: Matcha 'campione_AB.txt', 'campione_BA.txt' e 'campione_BA-txt' (punto = qualsiasi carattere)

⚠️ ATTENZIONE: Pattern 3 matcha anche 'campione_BA-txt' che probabilmente NON volevi!
""")