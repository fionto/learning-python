import re

# ============================================
# CAPTURE GROUPS: EXTRACTING SPECIFIC PARTS
# Concept: Wrapping part of a pattern in parentheses () creates a "Capture Group".
#          This allows you to extract specific pieces of the matched text.
# ============================================

text_3 = "My SSN is 123-45-6789 and my phone is 555-123-4567."

# Pattern Breakdown:
# (\d{3}) -> Group 1: Exactly 3 digits (Area code)
# -       -> Literal hyphen
# (\d{3}) -> Group 2: Exactly 3 digits (Prefix)
# -       -> Literal hyphen
# (\d{4}) -> Group 3: Exactly 4 digits (Line number)
pattern_3 = r"(\d{3})-(\d{3})-(\d{4})"

match_3 = re.search(pattern_3, text_3)
if match_3:
    print(f"Full match: {match_3.group(0)}")  # group(0) is always the entire match
    print(f"Area code:  {match_3.group(1)}")  # group(1) is the first set of ()
    print(f"Prefix:     {match_3.group(2)}")  # group(2) is the second set of ()
    print(f"Line num:   {match_3.group(3)}")  # group(3) is the third set of ()