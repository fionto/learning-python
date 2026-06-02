import re

# ============================================
# SEARCH FOR MULTIPLE PATTERNS
# ============================================
text_multi = "The quick brown fox jumps over the lazy dog."
patterns = ["fox", "cat", "dog"]

for pattern in patterns:
    match = re.search(pattern, text_multi)
    if match:
        print(f"\nFound '{pattern}' at index {match.span()}")
    else:
        print(f"\n'{pattern}' not found in the text")