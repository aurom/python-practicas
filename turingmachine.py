
def llena_estados():
	"""
	Llena la lista de estados de la maquina de turing
	"""
	q = []
	for i in range(0,1001):
		q.append(i)
	return q

def ini_cinta():
	"""
	Inicializa la cinta con ceros
	"""
	c = []
	for i in range(0,1001):
		c.append(0)
	return c

def out_of_range(b, cinta):
	"""
	Verifica si el indice b esta fuera del rango de la cinta
	b   blanco de la cinta
	cinta  cinta con la que se verificara
	"""
	return b <0 or len(cinta) <= b

def fill_rules(N):
	"""
	Genera el diccionario con las reglas establecidas
	N    numero de reglas a establecer
	"""
	diccionario = dict()
	for x in range(N):
		cadena = raw_input("Dame la regla: ")
		L = cadena.split(" ")
		diccionario[(L[0],L[1])] = L[1:]
	return diccionario

def llena_cinta(unos, cinta):
	"""
	Llena la cinta con los unos establecidos
	unos   numero de unos a poner
	cinta  cinta a llenar
	"""
	for y in range(0,unos):
		cinta[y] = 1

def machine(N, M, estados, cinta, rules, est_inicial, inicio_cinta):
	"""
	Maquina de turing
	N   numero de reglas
	M   numero de pruebas
	estados   conjunto de estados
	cinta     cinta de la maquina
	rules     diccionario con las reglas almacenadas
	est_inicial   estado inicial
	inicio_cinta  posicion inicial de la cinta
	"""
	if (N == 0 and M == 0):
		return
	for x in range(M):
		numeros = input("Cuantos 1's vas a meter: ")
		llena_cinta(numeros, cinta) # llena la cinta con unos
		res_deseado = input("Cuantos 1's crees que habra: ")
		estado_prev = est_inicial #auxiliar para dar los saltos entre estados
		blanco = inicio_cinta #blanco de la cina
		iteracion = 0
		reglas = rules
		while(iteracion <= 10000 and len(reglas) != 0 ):
			if ((str(estado_prev), str(cinta[blanco])) in reglas):
				break
			rule = reglas[(str(estado_prev) , str(cinta[blanco]))] #da la regla para el estado
			del reglas[(str(estado_prev), str(cinta[blanco]))] 
			cadena_prev = rule[0] #cadena leida
			estado_sig = int(rule[1]) #agarra el estado a donde se va a ir.
			cadena_sig = rule[2] #cadena a leer
			giro = rule[3]  #giro de la cinta
			estado_prev = estado_sig # cambia de estado
			cinta[blanco] = int(cadena_sig) #cambia el numero en la cinta por la cadena leida
			if (giro == "R"): blanco +=1
			if(giro == "L"): blanco -= 1
			iteracion += 1
			if(out_of_range(blanco, cinta)):
				 print ("MLE" + "\nTLE")
				 break
			if(iteracion == 10000):
				print ("TLE")
				break
		count = 0
		for i in cinta:
			if (i == 1): count+=1
		if(not out_of_range(blanco, cinta)):
			if (count == res_deseado): print "AL"
			else: print "WA"	
			
def main():
	N = input ("Cuantas reglas : ")
	M = input("Cuantas pruebas : ")
	estados = llena_estados() # Lista de estados
	cinta = ini_cinta() # Cinta de la maquina
	rules = fill_rules(N) # Diccionario con las reglas establecidas
	machine(N, M, estados, cinta, rules, estados[0], cinta[0])			
	
if __name__ == '__main__':
	main()
