import math 
def circleValue(r):
    circumference = round( 2 * math.pi * r)
    area = round(math.pi * r ** 2)
    return circumference , area

circumference , area = circleValue(3)
print(f"Area is : {area} , circumference is : {circumference}")