from math import radians, sin, cos, acos
def distance_lat_long(slat,slon,elat,elon):
 dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
 return dist