"""
Write a program to maximize the total rating of a sequence of sweets,
but under the condition that you cannot select adjacent sweets
from the display case
"""

# List of sweets and their ratings
our_sweets_list = [("choc", 3), ("straw", 10), ("vanilla", 12), ("pistachio", 16), ("rasp", 4)]


# Tuple: (a, b)
# Lightweight way of connecting two pieces of data that don't change
# Quickier and easier than dataclasses

def rating(the_list, for_index: int) -> int:
    return the_list[for_index][1]

def max_sweets(sweets_list: list[tuple[str,int]], start_ind: int) -> int:
    if start_ind == len(sweets_list) - 1:  # If this is the last sweet
        return rating(sweets_list, start_ind)
    
    elif start_ind == len(sweets_list) - 2:  # If this is the next to last sweet
        return max(rating(sweets_list, start_ind),
                   rating(sweets_list, start_ind + 1))
    
    else: # Otherwise
        pick_this_sweet = rating(sweets_list, start_ind) + max_sweets(sweets_list, start_ind + 2)
        skip_this_sweet = max_sweets(sweets_list, start_ind + 1)
        return max(pick_this_sweet, skip_this_sweet)

print(max_sweets(our_sweets_list, 0))


