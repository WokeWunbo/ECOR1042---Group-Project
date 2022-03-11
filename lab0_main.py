# Arun Karki 101219923

# imports
from lab0_functions import max_min
from lab0_functions import sum_y

"""
Exercise 1:

Step 1:
>>> [13.0, 12.0]

Step 2:
>>> [13.0, 12.0, 4.0] 
>>> [12.0, 4.0] 
>>> [12.0] 

Step 3:
>>> tuple type class
>>> (13.0, 12.0)

Step 4:
>>> 13.0 # x
>>> 12.0 # y

for x,y = point2
>>> 13.0
>>> 12.0

Step 5:
>>> point2[0] = 12.0     # Can we change the point to (12.0, 16.0)? 
No we cannot, tuples are not mutable
>>> point2.append(4.0)  # Can we add a third coordinate? 
No, tuples cannot be appended as they aren't mutable
>>> point2.pop(0)       # Can we remove the first coordinate?
No we can't, tuples aren't mutable so you cannot remove an element
"""

"""
Exercise 3:

Step 1:
>>> points = {(1.0, 2.0), (4.0, 6.0), (10.0, -2.0)}
{(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}
>>> points = {point1, point2, point3} 
{(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}
>>> points = set()
{(4.0, 6.0), (1.0, 2.0), (10.0, -2.0)}

Step 2:
1) only one copy is present

Step 3:
Sets are un-ordered therefore nothing can be indexed.

Step 4:
(4.0, 6.0)
(1.0, 2.0)
(10.0, -2.0)
"""
# Main Script

# Exercise 2
print(max_min([(2,3,2,4), (5,2,4)]))
print(max_min([(5,2,34,63), (51,42,43), (5,35,31,85,75)]))
print(max_min([(234,60,4,0), (5,3,44,233), (23,345,54), (34,75,64,64,3455)]))

# Exercise 4
print(sum_y({(1, 2), (1, 4)}))
print(sum_y({(-5, -4), (34, 6)}))
print(sum_y({(-123, -5), (4, -60)}))
print(sum_y({(13, 86), (4, 34)}))