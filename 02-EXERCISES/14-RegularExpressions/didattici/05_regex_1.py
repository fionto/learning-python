import re

# ============================================
# USING REGULAR EXPRESSIONS (REGEX)
# Concept: Raw strings (r"") are used in Python regex so backslashes 
#          aren't treated as standard Python escape characters.
# ============================================


# Search for a word that starts with 'q' and ends with 'k'
text_1 = "The quick brown fox jumps over the lazy dog."

# Pattern Breakdown:
# q       -> Matches the literal character 'q'
# \w+     -> Matches 1 or more (+) word characters (letters, digits, underscores)
# k       -> Matches the literal character 'k'
pattern_1 = r"q\w+k"

match_1 = re.search(pattern_1, text_1)
if match_1:
    print(f"Found: '{match_1.group()}'") 
    # Output: Found: 'quick'