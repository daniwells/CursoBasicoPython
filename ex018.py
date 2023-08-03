import math

angle = float(input('type it a angle:'))

vr = math.radians(angle)

tangent = math.tan(vr)
cosine = math.cos(vr)
sine = math.sin(vr)

print('The sine, cosine and tangent of {} is: {}, {}, {}'.format(angle, tangent, cosine, sine))