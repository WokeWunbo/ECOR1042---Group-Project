# Arun Karki 101219923

def printer():
    print(__name__)

# Function Exercise 2
def max_min(list_tuples : list[tuple]) -> list[tuple]:
    
    """Returns list of maximum and minimum integers in a tuple
    
    >>> max_min([(2,3,2,4), (5,2,4)])
    [(4, 2), (5, 2)]
    >>> max_min([(5,2,34,63), (51,42,43), (5,35,31,85,75)])
    [(63, 2), (51, 42), (85, 5)]
    >>> max_min([(234,60,4,0), (5,3,44,233), (23,345,54), (34,75,64,64,3455)])
    [(234, 0), (233, 3), (345, 23), (3455, 34)]
    """
    
    new_list_tuples = []
    
    for index_tuple in list_tuples:
        new_tuple = (max(index_tuple), min(index_tuple))
        new_list_tuples.append(new_tuple)
    
    return new_list_tuples

# Function Exercise 4
def sum_y(n_points : set(tuple())) -> float:
    
    """Returns sum of y-coordinate given a set of tuple (x,y) coordinates
    
    Precondition: set cannot contain repeating tuples.
    
    >>> sum_y({(1, 2), (1, 4)})
    6
    >>> sum_y({(-5, -4), (34, 6)})
    2
    >>> sum_y({(-123, -5), (4, -60)})
    -65
    >>> sum_y({(13, 86), (4, 34)})
    120
    """
    
    net_y = 0
    for tuple_ in n_points:
        net_y += tuple_[1]
        
    return net_y