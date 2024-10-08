def volume_sphere(r):
    pi = 22 / 7
    val = (4 * pi * r**3) / 3
    return round(val, 2)

radius = int(input("enter the value of radius: ")) 
volume = volume_sphere(radius)
print("volume of the sphere = ", volume)

