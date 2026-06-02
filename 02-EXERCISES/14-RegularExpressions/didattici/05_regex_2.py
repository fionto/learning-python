import re

# ============================================
# QUANTIFIERS & FINDING ALL MATCHES
# Concept: \d matches any digit (0-9). {n} means "exactly n times".
# Concept: re.findall() returns a LIST of all non-overlapping matches.
# ============================================

text_2 = "Call us at 123-456-7890 or 987-654-3210 for support."

# Pattern Breakdown:
# \d{3}   -> Exactly 3 digits
# -       -> A literal hyphen
# \d{4}   -> Exactly 4 digits
pattern_2 = r"\d{3}-\d{3}-\d{4}"

# Notice we use findall() here to get ALL phone numbers, not just the first!
all_numbers = re.findall(pattern_2, text_2)
print(f"Phone numbers found: {all_numbers}") 
# Output: Phone numbers found: ['123-456-7890', '987-654-3210']