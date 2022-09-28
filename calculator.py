import os

def suma(num1, num2):
	return num1 + num2

def resta(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	if num2 == 0:
		num2 = 1
	return num1 / num2

def return_values():
	num1 = int(input("Ingresa un numero: "))
	num2 = int(input("Ingresa otro numero: "))
	return [num1, num2]

if __name__ == '__main__':
	message = f"Calculadora: \n Elige una opción:\n1 - suma\n2 - resta\n3 - multiplicacion\n4 - division\n5 - Salir\n"
	while True:
		os.system('clear')
		opcion = int(input(message))
		# comparar cada una de las opciones y llamar a la funcion que corresponda
		if opcion == 1:
			numeros = return_values()
			resultado_suma = suma(numeros[0], numeros[1])
			print("El resultado de la suma es", resultado_suma)
		elif opcion == 2:
			numeros = return_values()
			resultado_resta = resta(numeros[0], numeros[1])
			print("El resultado de la resta es", resultado_resta)
		if opcion == 3:
			numeros = return_values()
			resultado_multi = multiply(numeros[0], numeros[1])
			print("El resultado de la multiplicación es", resultado_multi)
		if opcion == 4:
			numeros = return_values()
			resultado_div = divide(numeros[0], numeros[1])
			print("El resultado de la división es", resultado_div)
		elif opcion == 5:
			print("Bye!")
			break
		else:
			print("Opción Incorrecta")
