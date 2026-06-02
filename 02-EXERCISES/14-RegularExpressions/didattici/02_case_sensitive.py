import re

# ============================================
# CASE-SENSITIVE SEARCH
# ============================================
text_case = "I am Dracula; fear my bite!"
pattern_case = "dracula"

# By default, re.search() is case-sensitive
result_case = re.search(pattern_case, text_case)

if not result_case:
    print("\nCase-sensitive search: No match for", pattern_case, "in:", text_case)

# Use re.IGNORECASE flag for case-insensitive search
result_case_insensitive = re.search(pattern_case, text_case, re.IGNORECASE)
if result_case_insensitive:
    print("Case-insensitive match found:", result_case_insensitive.group())