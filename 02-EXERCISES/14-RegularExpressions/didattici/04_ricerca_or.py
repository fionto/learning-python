import re

# ============================================
# SEARCH FOR ALTERNATIVE PATTERNS
# ============================================
text_multi = "The quick brown fox jumps over the lazy dog."
patterns = r"fox|cat" # Special character '|' means or

result = re.search(patterns, text_multi)

if result:
    print(f"Found '{result.group()}' at index {result.span()}")
else:
    # The backslash '\' is used to escape the special '|' character
    readable_pattern = re.sub(r"\|", " or ", patterns) 
    print(f"\n'{readable_pattern}' not found in the text")