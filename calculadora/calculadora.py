
print("por favor selecciona tu operacion:")
print("1 - Suma")
print("2- Resta")
print("3 - Multiplicacion")
print("4 - Division")

while True:
    opcion = input("Selecciona una de las opciones: 1 - 2 - 3 - 4 ")
    if opcion in ('1', '2', '3', '4'):
        num1 = int(input("Ingresa el primer numero: "))
        mun2 = int(input("ingresa el segundo numero: "))
        if opcion == '1':
            print(suma)
        elif opcion == '2':
            print(resta)
        elif opcion =='3':
            print(multiplicacion)
        elif opcion == '4':
            print(division)            




