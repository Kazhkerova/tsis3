def sphere_volume(radius):
    volume = (4 / 3) * 3.14159 * radius**3
    return volume
rad=float(input())
res=sphere_volume(rad)
print(res)