import math

print("[Enter length of 3 side]")
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
s=(a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("Area of triangle: ",area)
