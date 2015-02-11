def isPrime(n):
    if n<2: return False
    if n==2: return True
    for i in range(3,int(n**0.5)+1,2): #empieza en 3 y se salta de 2 en 2
        if n%i==0:
            return False    
    return True
    
def getPrimos():#genera una lista de primos menores a 100,000
	lista = []
	for n in range (2, 100000):
		if (isPrime(n)):
			lista.append(n)
	return lista#regresa la lista

def goldbach(primos, compuesto):
	for n in range(1, 1000):#el rango es porque  no puede pasar de ahi  
		for i in primos:
			numero = i + (2*(n**2))
			if numero == c:
				return True # significa que el numero pasado si es compuesto por un primo y el doble del numero elevado al cuadrado
				break
			else:
				continue
	return False # significa que el numero no esta compuesta por un primo y el doble de otro numero al cuadrado
	
def main():
	
	primos = get_Primos() #genera la lista de primos
	compuestos = []
	for c in range(29, 100000, 2): #va en un rango solo contando los impares
		if c not in primos:  # si el impar contado es primo no lo mete a la lista de compuestos.
			compuestos.append(c)
		else:
			continue
	for x in compuestos: #recorre la lista de compuestos
		if goldbach(primos, x) ==False: 
			print "Respuesta = ", x
			break #cuando encuentre ese compuesto que no cumple se rompe el ciclo y lo imprime
		else:
			continue #continua iterando
if __name__ == '__main__':
	main()
