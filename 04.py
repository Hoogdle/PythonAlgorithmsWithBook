# Most Common Word

# "Print most common word, excpet forbid words."

# Cond #

# 1. Do not separate Big and small letters
# 2. Ignore '.', ','

### Solution1 ### (Regular Expression and List Comprehension)
import re
import collections

def most_common_word(input: str, banned: list[str]) -> str:
    words = [word for word in re.sub(r'[^\w]','',input).lower().split() if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

