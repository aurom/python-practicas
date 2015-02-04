#Eduardo Ruiz Morua
#Adriana López Hernandez
#Rene Guerra Leyva
#Alfonso Casanova

def impares(n):
	numero = 0
	cad = str(bin(n))
	for i in cad[2:]:
		if (i == "1"):
			numero+=1
	if(numero % 2 != 0):
		return True
	return False
def numeros(n):
	count = 0
	numeros = 0
	num = 0
	while count < n:
		if(impares(numeros)):
			count +=1
			num = numeros
			numeros +=1
		else:
			numeros +=1
	return num


