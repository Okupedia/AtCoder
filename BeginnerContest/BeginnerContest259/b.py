import math

a, b, d = map(int,input().split())

length = math.sqrt(a**2 + b **2)

angle = math.atan2(b,a)
new_angle = angle + math.radians(d)


#print('cos:', math.cos(new_angle), '/sin:', math.sin(new_angle))
#print('angle:', math.degrees(angle), '→', math.degrees(new_angle))

print(length * math.cos(new_angle), length * math.sin(new_angle))
