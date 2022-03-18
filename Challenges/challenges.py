# Import all files

import sys
sys.path.append('modules')  

from is_pal import *
from add_evens import *
from add_evens_followup import *
from can_cheese import *
from can_cheese_followup import *
from min_of_maxes import *
from space_acquaintance import *
from shortest_path import *
from longest_uppercase import *
from max_tastiness import *
from lifeguard_budget import *




######################################
#                                    #
# Level 1 (2 pts each)               # 
#                                    #
######################################


# is_pal
"""
>>> is_pal("cars")
False
>>> is_pal("tacocat")
True
>>> is_pal("aa")
True
>>> is_pal("abaa")
False
>>> is_pal("tacobcat")
False
"""

    


# add_evens
"""
>>> add_evens([5])
5
>>> add_evens([1, 2, 3, 4, 5])
9
>>> add_evens([-4, 3, 0, 2])
-4
"""



# add_evens_followup
"""
>>> add_evens(5)
5
>>> add_evens(12345)
9
>>> add_evens(4302])
5
"""



######################################
#                                    #
# Level 2 (3 pts each)               # 
#                                    #
######################################


# can_cheese
"""
>>> can_cheese(3, 1, 8)
True
>>> can_cheese(3, 1, 9)
False
>>> can_cheese(3, 2, 10)
True
>>> can_cheese(1, 3, 12)
False
>>> can_cheese(13, 1, 13)
True
>>> can_cheese(14, 0, 13)
True
"""


# can_cheese_followup
"""
More test cases to come...
>>> can_cheese(3, 3, 5, 5, 27)
True
>>> can_cheese(3, 3, 5, 5, 28)
True
>>> can_cheese(3, 3, 5, 5, 32)
False
"""
    


# min_of_maxes
"""
>>> min_of_maxes([1,3,-1,-3,5,3,6,7], 3)
3
>>> min_of_maxes([1,3,-1,-3,5,3,6,7], 1)
-3
"""
    



######################################
#                                    #
# Level 3 (4 pts each)               # 
#                                    #
######################################


# space_acquaintance
"""
>>> space_acquaintance([1, 2, 2, 3, 4, 5], [2, 4, 5, 5, 5, 6])
3
>>> space_acquaintance([1, 4, 4, 2, 5, 6, 7, 2], [3, 1, 3, 5, 6, 7, 5, 6])
0
"""
  


# shortest_path
"""
>>> shortest_path({1:[2], 2:[]}, 1,2)
1
>>> shortest_path({1: [2, 3], 2: [1, 3, 8], 3: [1, 2, 4, 8], 5: [3, 6], 6: [5, 7], 7: [6, 8], 8: [2, 7]}, 1, 1)
0
>>> shortest_path({1: [2, 3], 2: [1, 3, 8], 3: [1, 2, 4, 8], 5: [3, 6], 6: [5, 7], 7: [6, 8], 8: [2, 7]}, 1, 8)
2
>>> shortest_path({1: [2, 3], 2: [1, 3, 8], 3: [1, 2, 4, 8], 5: [3, 6], 6: [5, 7], 7: [6, 8], 8: [2, 7]}, 4, 7)
3
"""



# longest_uppercase
"""
>>> longest_uppercase("aaabbcajnnaddgfjn", 2)
5
>>> longest_uppercase("aaabbbcajnnnnaddgfjn", 1)
4
>>> longest_uppercase("aaabbbcajnnnnadddgfjn", 4)
9
"""




######################################
#                                    #
# Extras (0 pts each)                # 
#                                    #
######################################


# max_tastiness
"""
>>> round(max_tastiness([(4,.9), (6,.5)]), 5)
9.4
>>> round(max_tastiness([(10,0.1),(5,0.1),(4,0.2),(2,0.6)]), 5)
10.544
>>> round(max_tastiness([(0,1),(1,1),(0,0),(1,0),(5,0.4),(4,0.5),(2,0.7)]), 5)
8.14
>>> ar = [((0.003*x*x*x + 0.001*x*x + 4.159)%100, (0.00265*x*x)%1) for x in range(10000)]
>>> round(max_tastiness(ar), 5)
7534.58121
"""



# lifeguard_budget
"""
>>> lifeguard_budget([(0,1000),(0,500),(500,1440)])
1440
>>> lifeguard_budget([(0,1000),(0,500),(501,1440)])
1939
>>> lifeguard_budget([(a*5-7,a*5) for a in range(400)])
2016
>>> lifeguard_budget([(a*6-10,a*6-2) for a in range(400)][::-1])
1928
"""



# largest_valid_tree
"""
>>> largest_valid_tree("AB AC BD")
3
>>> largest_valid_tree("AB BC CA")
2
"""


if __name__ == "__main__":
    import doctest
    #doctest.testmod()

