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
		if opcion == 5:
			print("Bye!")
			break
