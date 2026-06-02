# ============================================
# Python Regular Expressions
# ============================================

import re

# ============================================
# 1. BASIC USAGE OF re.search()
# ============================================
text = 'I am Dracula; and I bid you welcome, Mr. Harker, to my house.'
pattern = 'Dracula'

# re.search() scans the text for the first occurrence of the pattern
# Returns a Match object if found, otherwise returns None
result = re.search(pattern, text)

# Check the type of the result (Match object or NoneType)
print("Type of result:", type(result))

# If a match is found, the Match object is truthy
if result:
    print("Match found!")
    
    # group(): Returns the matching substring
    print("Matching substring:", result.group())
    
    # span(): Returns a tuple with start and end indices of the match
    print("Start and end indices:", result.span())
    
    # start() and end(): Individual start and end indices
    print("Start index:", result.start(), "| End index:", result.end())

# ============================================
# 2. EXAMPLE: NO MATCH CASE
# ============================================
text_no_match = "I am a vampire hunter."
pattern_no_match = "Dracula"

result_no_match = re.search(pattern_no_match, text_no_match)

# If no match is found, result is None (falsy)
if not result_no_match:
    print("\nNo match found for", pattern_no_match, "in:", text_no_match)