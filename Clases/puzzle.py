class A:             #estructura principal 
    def z(self):        #función
        return self 
 
    def y(self, t):         #función
        return len(t) 
 
a = A           # vuelve a la clase A
y = a.z 
print(y(a)) 
aa = a() #instancia
print(aa is a()) 
z = aa.y        #función
print(z(()))            #tupla vacía
print(a().y((a,))) 
print(A.y(aa, (a,z))) 
print(aa.y((z,1,'z'))) 

# el primer valor será el cero por estar la tupla t vacía
# el segundo valor es el 1 por estar en la casilla 2
#luego, tendríamos el valor z que sería el 3