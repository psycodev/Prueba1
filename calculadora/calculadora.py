from Suma import Suma
from resta import Resta
from mullti import Multiplicar
from division import Division

print("por favor selecciona tu operacion:")
print("1 - Suma")
print("2- Resta")
print("3 - Multiplicacion")
print("4 - Division")

while True:
    opcion = input("Selecciona una de las opciones >> ")
    if opcion in ('1', '2', '3', '4'):
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("ingresa el segundo numero: "))
        if opcion == '1':
             print("el resultado de la suma es: ",Suma(num1, num2))
        elif opcion == '2':
            print("el resultado de la resta es : ", Resta(num1, num2))
        elif opcion =='3':
             print("el resultado de la multiplicacion es : ", Multiplicar(num1,num2))
        elif opcion == '4':
            print("el resultado de la division es : ", Division( num1, num2))           








