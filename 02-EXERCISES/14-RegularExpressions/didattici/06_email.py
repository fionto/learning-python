import re
# ============================================
# EXTRACTING EMAILS
# Concept: Character classes [] allow you to specify a custom set of allowed characters.
# ============================================

text_5 = "Contact support at help@company.com or sales.team+promo@sub.domain.co.uk."

# Pattern Breakdown:
# [a-zA-Z0-9._%+-]+ -> 1 or more valid email username characters
# @                 -> Literal '@' symbol
# [a-zA-Z0-9.-]+    -> 1 or more valid domain name characters
# \.                -> Literal dot (escaped with \ because . normally means "any character")
# [a-zA-Z]{2,}      -> 2 or more letters for the domain extension (.com, .uk, etc.)
pattern_5 = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern_5, text_5)
print(f"Emails found: {emails}")
# Output: Emails found: ['help@company.com', 'sales.team+promo@sub.domain.co.uk']