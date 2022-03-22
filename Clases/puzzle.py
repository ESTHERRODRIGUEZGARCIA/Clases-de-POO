class A:                    # estructura principal 
    def z(self):            # función
        return self 
 
    def y(self, t):         # función
        return len(t) 
 
a = A                       # vuelve a la clase A
y = a.z                     # sigue formando parte de la clase A por la anterior condición
print(y(a))                 # me devuelve <class 'Clases.puzzle.A'> por el self definido en z
aa = a()                    # instancia
print(aa is a())            # False pues la condición no es verdadera
z = aa.y                    # función
print(z(()))                # tupla vacía, devuelve el valor 0
print(a().y((a,)))          # tupla que devuelve len(a). Es 1 por estar formada sólo por a
print(A.y(aa, (a,z)))       # tupla que devuelve la longitud. Es 2 por estar formada tanto por a como por z
print(aa.y((z,1,'z')))      # tupla que devuelve len( z, 1, 'z') que son 3 elementos

