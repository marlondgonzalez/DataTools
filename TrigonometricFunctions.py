# Trigonometric functions used to calculate levels of parallelism. Shape object is from an arcpy polyline object
import math
import arcpy

def GetGeographicalDegrees(shape):
    radian = math.atan2(shape.lastpoint.y - shape.firstpoint.y, shape.lastpoint.x - shape.firstpoint.x)
    radian = radian - (math.pi / 2) # turn minus 90°
    if (radian > 0):
        degrees = 360 - (radian * 360) / (2 * math.pi )
    else:
        degrees = 360 - ((2* math.pi + radian  ) * 360) / ( 2 * math.pi )
    return degrees

def GetSlope(shape):
    y = shape.lastpoint.y - shape.firstpoint.y
    x = shape.lastpoint.x - shape.firstpoint.x
    if x == 0:
        return None # Undefined
    else:
        return y/x

def GetAngle(gasSlope, electricSlope):
    m = gasSlope * electricSlope
    if gasSlope == None:
        slope = electricSlope
        return abs(math.atan(abs(slope)) * (180/math.pi) - 90)
    elif electricSlope == None:
        slope = gasSlope
        return abs(math.atan(abs(slope)) * (180/math.pi) - 90)
    elif m == -1:
        return 90
    else:
        return (math.atan(abs((gasSlope - electricSlope) / (1 + m)))) * (180/math.pi)
