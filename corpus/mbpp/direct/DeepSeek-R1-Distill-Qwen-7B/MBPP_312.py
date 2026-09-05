def volume_cone(radius, height):
    import math
    return (1/3) * math.pi * (radius ** 2) * height

volume_cone(5,12) == 314.15926535897927
volume_cone(10,15) == 1570.7963267948965
volume_cone(19,17) == 6426.651371693521