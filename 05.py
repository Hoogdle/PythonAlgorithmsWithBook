# Group Anagrams

# Make a Group per Unit of Anagrams from given String Array.

### Solution1 ###
import collections

def group_anagrams(input: list[str])-> list[list[str]]:
    anagrams_dict = collections.defaultdict(list)

    for item in input:
        key = str(sorted(item))
        anagrams_dict[key].append(item)
    
    result = []

    for key, _ in anagrams_dict.items():
        result.append(anagrams_dict[key])
    
    # return list(anagrams_dict.values())
    return result
