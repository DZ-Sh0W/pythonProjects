print("PROGRAMME POUR CALCULER LES MOYENNES")
print()

# LES MODULES

# Coeff. 3
a = str(input("Module à coeff. 3 : "))

# Coeff. 2
b = str(input("1er module à coeff. 2 : "))
c = str(input("2ème module à coeff. 2 : "))
d = str(input("3ème module à coeff. 2 : "))
e = str(input("4ème module à coeff. 2 : "))
f = str(input("5ème module à coeff. 2 : "))

# Coeff. 1
g = str(input("1er module à coeff. 1 : "))
h = str(input("2ème module à coeff. 1 : "))
i = str(input("3ème module à coeff. 1 : "))
j = str(input("4ème module à coeff. 1 : "))

print()
# LES NOTES

# Coeff. 3
a1 = float(input("Entre la note du C.C du module " + a + " : "))
a2 = float(input("Entre la note de l'Examen du module " + a + " : "))
A = (a1*0.4) + (a2*0.6)

print()

# Coeff. 2
b1 = float(input("Entre la note du C.C du module " + b + " : "))
b2 = float(input("Entre la note de l'Examen du module " + b + " : "))
B = (b1*0.4) + (b2*0.6)

print()

c1 = float(input("Entre la note du C.C du module " + c + " : "))
c2 = float(input("Entre la note de l'Examen du module " + c + " : "))
C = (c1*0.4) + (c2*0.6)

print()

d1 = float(input("Entre la note du C.C du module " + d + " : "))
d2 = float(input("Entre la note de l'Examen du module " + d + " : "))
D = (d1*0.4) + (d2*0.6)

print()

e1 = float(input("Entre la note du C.C du module " + e + " : "))
e2 = float(input("Entre la note de l'Examen du module " + e + " : "))
E = (e1*0.4) + (e2*0.6)

print()

f1 = float(input("Entre la note du C.C du module " + f + " : "))
f2 = float(input("Entre la note de l'Examen du module " + f + " : "))
F = (f1*0.4) + (f2*0.6)

print()

# Coeff. 1
g1 = float(input("Entre la note de l'Examen du module " + g + " : "))
G = g1

print()

h1 = float(input("Entre la note de l'Examen du module " + h + " : "))
H = h1

print()

i1 = float(input("Entre la note de l'Examen du module " + i + " : "))
I = i1

print()

j1 = float(input("Entre la note de l'Examen du module " + j + " : "))
J = j1

print()

# LES CALCULS

total = ((A*3)+(B*2)+(C*2)+(D*2)+(E*2)+(F*2)+G+H+I+J)/17
print("La moyenne :","%.2f" % total)

