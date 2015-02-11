def isPrime(n):#verifica si es primo
    if n<2: return False
    if n==2: return True
    for i in range(3,int(n**0.5)+1,2): #empieza en 3 y se salta de 2 en 2
        if n%i==0:
            return False    
    return True

def goldbach():
	compuestos = [] # lista para guardar compuestos
	r = [] #lista de ayuda
	for i in range (3,1000000,2):
		if not isPrime(i):
			compuestos.append(i) #si no es primo lo guarda en compuestos 
	for x in compuestos:
		p = 1 #numero no primo del compuesto x
		flag = False
		while 2*(p**2) < x: #aumenta los p y los guarda en la lista auxiliar
			r.append(x - 2*(p**2))
			p += 1
		for y in r :
			if (not isPrime(y)): #mientras no sea primo y la bandera sera falsa
				flag = False
			else:
				flag = True #si es primo se rompe el siglo 
				break
		r = []	#reinicializa la lista auxiliar
		if(flag == False): # si la bandera se quedo en falso siginifica que encontramos al contraejemplo
			return x
		
print (goldbach())
			
