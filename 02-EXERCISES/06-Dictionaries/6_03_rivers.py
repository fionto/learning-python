# Make a dictionary containing three major rivers and the
# capital each river runs through.
# Use a loop to print a sentence avout each river
# Use a loop to print each river name
# Use a loop to print each nation

# Memorizzo nome e numero preferito
fiumi = {
    "Tevere": "Roma",
    "Senna": "Parigi",
    "Manzanarre": "Madrid",
    "Moldava": "Praga",
}

for fiume, città in fiumi.items():
    print(f"Il fiume {fiume} scorre in {città}")

for fiume in fiumi.keys():
    print(fiume)

for capitale in fiumi.values():
    print(capitale)