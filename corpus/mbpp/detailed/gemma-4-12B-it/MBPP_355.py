import math
from typing import List

def count_Rectangles(r: float) -> int:
    """
    Counts the number of rectangles that can be formed using points with 
    integer coordinates (x, y) that lie strictly inside or on the 
    boundary of a circle centered at (0, 0) with radius r.

    The problem's assertions imply a specific definition of "rectangles":
    - count_Rectangles(1) == 1: Only the rectangle with vertices (0,0), (0,1), (1,1), (1,0) 
      is not possible because (1,1) is outside radius 1. Wait, let's re-evaluate.
    - Standard geometry: A rectangle with sides parallel to axes is defined by 
      two x-coordinates (x1, x2) and two y-coordinates (y1, y2) such that 
      all four vertices (x1, y1), (x1, y2), (x2, y1), (x2, y2) are within the circle.
    - For r=1: Points are (0,0), (1,0), (-1,0), (0,1), (0,-1). 
      The only rectangle is formed by (0,0) is not a rectangle. 
      Wait, the assertion says count_Rectangles(1) == 1. 
      If r=1, the only rectangle possible is the one with vertices (0,0), (0,1), (1,0), (1,1)? 
      No, (1,1) is at distance sqrt(2) > 1.
      If r=1, points are (0,0), (1,0), (-1,0), (0,1), (0,-1). 
      The only rectangle is formed by (0,0) and points? No.
      Actually, let's check r=2. Points are (x,y) such that x^2 + y^2 <= 4.
      Points: (0,0), (1,0), (2,0), (-1,0), (-2,0), (0,1), (0,2), (0,-1), (0,-2), 
      (1,1), (1,-1), (-1,1), (-1,-1), (1, \sqrt{3}), etc.

      Re-evaluating the assertions:
      r=1, result=1.
      r=2, result=8.
      r=0, result=0.

      This pattern (r=1 -> 1, r=2 -> 8) suggests the rectangles are formed 
      by 4 points (x, y) where x != 0 and y != 0 and they are symmetric? 
      No, let's look at the number of integer points (x, y) such that x^2 + y^2 <= r^2.
      For r=1: (0,0), (1,0), (-1,0), (0,1), (0,-1). 
      A rectangle with sides parallel to axes is defined by x_min, x_max, y_min, y_max.
      To be a rectangle, we need x_min < x_max and y_min < y_max.
      All four corners must satisfy x^2 + y^2 <= r^2.
      For r=1:
      Possible x values: -1, 0, 1.
      Possible y values: -1, 0, 1.
      Pairs (x_min, x_max): (-1, 0), (-1, 1), (0, 1).
      Pairs (y_min, y_max): (-1, 0), (-1, 1), (0, 1).
      Check corners for (-1, 0) and (-1, 0): (-1,-1), (-1,0), (0,-1), (0,0).
      Distances: sqrt(2), 1, 1, 0. All <= 1. This is 1 rectangle.
      Check corners for (-1, 0) and (0, 1): (-1,0), (-1,1), (0,0), (0,1).
      Distances: 1, sqrt(2), 0, 1. (1,1) is out.
      Check corners for (0, 1) and (0, 1): (0,0), (0,1), (1,0), (1,1).
      Distances: 0, 1, 1, sqrt(2). (1,1) is out.

      Wait, if r=1, the only rectangle is corners (-1,0), (-1,-1), (0,-1), (0,0)? 
      No, that's 4 points. The corner (-1,-1) has distance sqrt(2) > 1.
      The only possible rectangle with integer coordinates in r=1 is ... 
      Actually, the only way to get 1 for r=1 is if the rectangle is (0,0), (0,1), (1,0), (1,1)
      but (1,1) is only inside if r >= sqrt(2). 

      Let's reconsider. Maybe the rectangles are formed by the 4 points 
      (x, y), (-x, y), (-x, -y), (x, -y) where x, y > 0.
      For r=1: x=1, y=1 => 1^2 + 1^2 = 2. 2 > 1^2. No.

      Let's re-read: "rectangles in a circle of radius r".
      Maybe it's the number of rectangles with 4 vertices on the circumference?
      No, for r=1, there is only 1 rectangle? That would be the inscribed rectangle.
      But a circle has infinite rectangles.

      Wait! Let's try the "sum of products" approach for rectangles with sides parallel to axes.
      A rectangle is defined by x1 < x2 and y1 < y2. 
      The condition is: x1^2 + y1^2 <= r^2, x1^2 + y2^2 <= r^2, x2^2 + y1^2 <= r^2, x2^2 + y2^2 <= r^2.
      Since x1 < x2 and y1 < y2, the "worst" corner is the one with the largest 
      absolute values. 
      Case 1: x1, x2 >= 0 and y1, y2 >= 0. Max is (x2, y2).
      Case 2: x1, x2 <= 0 and y1, y2 <= 0. Max is (x1, y1).
      Case 3: x1 < 0, x2 > 0 and y1, y2 > 0. Max is (x2, y2).

      Let's test r=1 with this:
      Integer points (x,y) s.t. x^2 + y^2 <= 1:
      (0,0), (1,0), (-1,0), (0,1), (0,-1)
      Possible x: -1, 0, 1. Possible y: -1, 0, 1.
      Pairs (x1, x2) from {-1, 0, 1}: (-1,0), (-1,1), (0,1).
      Pairs (y1, y2) from {-1, 0, 1}: (-1,0), (-1,1), (0,1).
      Rectangles (x1, x2, y1, y2):
      1. (-1,0, -1,0) -> Corners: (-1,-1), (-1,0), (0,-1), (0,0). 
         Distances: sqrt(2), 1, 1, 0. Max dist = sqrt(2). sqrt(2) > 1. Invalid.
      2. (-1,0, -1,1) -> Corners: (-1,-1), (-1,1), (0,-1), (0,1).
         Max dist = sqrt(2). Invalid.
      3. (-1,0, 0,1) -> Corners: (-1,0), (-1,1), (0,0), (0,1).
         Max dist = sqrt(2). Invalid.
      4. (-1,1, -1,0) -> Invalid (y1 > y2).
      5. (-1,1, -1,1) -> Invalid.
      6. (-1,1, 0,1) -> Corners: (-1,1), (-1,1), (0,1), (0,1). Not a rectangle (x1=x2).
      ...
      Wait, if r=1 gives 1, then the rectangle must be something else.
      What if the rectangles are not parallel to the axes? 
      Or what if the coordinates don't have to be integers? No, that's impossible.

      Let's try: Number of pairs of points (x,y) such that they are opposite corners 
      of a rectangle whose other two corners are also in the circle.

      Let's try a different interpretation. 
      If r=1, result=1.
      If r=2, result=8.

      Let's look at the number of integer points (x,y) inside x^2 + y^2 <= r^2.
      For r=1: (0,0), (1,0), (-1,0), (0,1), (0,-1). Total 5 points.
      For r=2: (0,0), (1,0), (-1,0), (2,0), (-2,0), (0,1), (0,-1), (0,2), (0,-2), 
               (1,1), (1,-1), (-1,1), (-1,-1), (1,\sqrt{3}) -> (1, \pm 1) are inside. 
               Wait, 1^2 + 1^2 = 2 <= 4. 
               (1, \pm 1), (-1, \pm 1) -> 4 points.
               (1, \pm 1), (-1, \pm 1).
               (2, 0), (-2, 0), (0, 2), (0, -2).
               (0,0).
               Total points for r=2: 1 + 4 + 4 + 4 = 13.

      Could the formula be related to the number of pairs of diameters?
      A rectangle is formed by two diameters of the circle.
      If we only consider rectangles with vertices on the circle boundary:
      For r=1: Boundary points are (1,0), (-1,0), (0,1), (0,-1).
      These 4 points form 1 rectangle (a square).
      For r=2: Boundary points (x^2 + y^2 = 4):
      (2,0), (-2,0), (0,2), (0,-2).
      Any other integer points on boundary? x^2 + y^2 = 4.
      If x=1, y^2=3 (no). If x=2, y=0.
      So only 4 points on the boundary. They form 1 rectangle. 
      But the assertion says 8.

      Wait! What if the rectangles are formed by any two diameters? 
      A diameter is a line segment passing through (0,0) with endpoints on the boundary.
      For r=2, are there 8 diameters? No.

      Let's try another approach. What if the rectangles are formed by 
      picking 2 points (x1, y1) and (x2, y2) such that they are opposite corners 
      of a rectangle whose other corners are also in the circle?
      The corners of a rectangle with opposite corners (x1, y1) and (x2, y2) 
      (assuming x1 != x2 and y1 != y2) are (x1, y1), (x2, y2), (x1, y2), (x2, y1).

      Let's count these for r=1:
      Points (x,y) with x^2 + y^2 <= 1: (0,0), (1,0), (-1,0), (0,1), (0,-1).
      Pairs of points (x1, y1) and (x2, y2) from this set:
      To form a rectangle, we need x1 != x2 and y1 != y2.
      Let's list the points: P1(0,0), P2(1,0), P3(-1,0), P4(0,1), P5(0,-1).
      Possible pairs (P_i, P_j):
      - (P2, P4) i.e., (1,0) and (0,1). Other corners: (1,1) and (0,0).
        Is (1,1) in? 1^2 + 1^2 =