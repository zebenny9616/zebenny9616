import math

# conversion de DMS a DD
def decimal_degree(position):
    degree, minutes, seconds = position
    return degree + minutes / 60 + seconds / 3600

# calculer la distance entre deux points
def distance(p1_x, p1_y, p2_x, p2_y):
    return math.sqrt((p2_x - p1_x)**2 + (p2_y - p1_y)**2)

POLE_NORD_X = 86, 29, 38
POLE_NORD_Y = 162, 52, 1
MONTREAL_X = 45, 30, 31
MONTREAL_Y = 73, 35, 16

polenord_ddp_x = decimal_degree(POLE_NORD_X)
polenord_ddp_y = decimal_degree(POLE_NORD_Y)
montreal_ddp_x = decimal_degree(MONTREAL_X)
montreal_ddp_y = decimal_degree(MONTREAL_Y)

print(polenord_ddp_x, polenord_ddp_y)
print(montreal_ddp_x, montreal_ddp_y)
print(distance(polenord_ddp_x, polenord_ddp_y, montreal_ddp_x, montreal_ddp_y))