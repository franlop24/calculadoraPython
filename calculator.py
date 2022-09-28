def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

if __name__ == '__main__':
	message = f"Calculadora: \n Elige una opción:\n1 - suma\n2 - resta\n3 - multiplicacion\n4 - division\n5 - Salir\n"
	while True:
		opcion = int(input(message))
		# comparar cada una de las opciones y llamar a la funcion que corresponda
		if opcion == 1:
			resultado_suma = suma(23, 54)
			print("El resultado de la suma es", resultado_suma)
		elif opcion == 2:
			resultado_resta = resta(23, 54)
			print("El resultado de la resta es", resultado_resta)
		if opcion == 3:
			resultado_multi = multiply(23, 54)
			print("El resultado de la multiplicación es", resultado_multi)
		if opcion == 4:
			resultado_div = divide(23, 54)
			print("El resultado de la división es", resultado_div)
		elif opcion == 5:
			print("Bye!")
			break
		else:
			print("Opción Incorrecta")
