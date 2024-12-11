# komparasi logika boolean
# not, or, and, xor
# NOT
a = True
c = not a
print(a,'NOT',c,'=', c)
print('data c =', c)

# OR akan False jika keduanya False selebihnya True
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)

a = False
b = False
c = a or b
print(a,'OR',b,'=',c)

a = True
b = False
c = a or b
print(a,'OR',b,'=',c)

a = False
b = True
c = a or b
print(a,'OR',b,'=',c)

# and akan True jika keduanya True selebihnya False
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)

a = False
b = False
c = a and b
print(a,'AND',b,'=',c)

a = True
b = False
c = a and b
print(a,'AND',b,'=',c)

a = False
b = True
c = a and b
print(a,'AND',b,'=',c)

# xor akan True jka satu saja yg True
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)

a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
