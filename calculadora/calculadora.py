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
            multiplicar(a,b)
        elif opcion == '4':
            print(division)            


def Multiplicar(a,b):
    c = int(a*b)
    w= print (" La multipliacion es igual a= ",c)
    return (w)

#a=int(input(" Ingrese el primer numero= "))
#b=int(input(" Ingrese el segundo numero= "))
Entradatexto= input("Ingrese la operaicon que desea realizar= ")
Entradatexto= Entradatexto.lower()
if Entradatexto=="mulplicar" or Entradatexto=="m":
    if a!=0 and b!=0:
        Multiplicar(a,b)
    else:
        "La Multipliacion es igual a 0"
        c=0
#else:
 #   print("esta no esta")


