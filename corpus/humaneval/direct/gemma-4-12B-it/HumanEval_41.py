def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """
    # There are n cars moving left to right.
    # There are n cars moving right to left.
    # Every car moving left to right will eventually collide with 
    # every car moving right to left because they are on an 
    # infinite straight line moving toward each other at the 
    # same speed.
    # The number of collisions is the number of pairs (car_L, car_R).
    # Since there are n cars of each type, the total number of pairs is n * n.
    return n * n