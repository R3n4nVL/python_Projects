import math

x1 = int(input("Digte o ponto em x1:"))
y1 = int(input("Digte o ponnto em y1:"))
#plano cartesiano do 1ºQuadrante

x2 = int(input("Digte o ponto em x2:"))
y2 = int(input("Digte o ponnto em y2:"))
#plano cartesiano do 2°Quadrante

dx = (x1 - x2)**2
dy = (y1 - y2)**2

D = math.sqrt(dx + dy)

if D >= 10:
    print("longe")
else:
    print("perto")



