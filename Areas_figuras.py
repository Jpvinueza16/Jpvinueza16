import math

def area_cuadrado(lado):
    if(lado<=0):
        return print('Solo numeros positivos Error')
    else :
        area=lado**2
        return  print('El area del cuadrado es: ', area)
    
def area_triangulo(base,altura):

    if(base<=0 or altura <=0):
        return print('Solo numeros positivos Error')
    else :
        area=base*altura/2
        return print('El area del triángulo es: ', area)
        
salir = False
while not salir:
    print("Calcular Áreas de figuras Geométricas.\n")
    print("1.Cuadrado.\n2.Triángulo\n3.Salir\n")

    opciones=int(input("Escoja la figura: "))

    if opciones==1:
        lado=int(input('Ingrese el lado: '))
        area_cuadrado(lado)
        print("\n")
    
    if opciones==2:
    
        base=int(input('Ingrese la base: '))
        altura=int(input('Ingrese la altura: '))
        area_triangulo(base,altura)
        print("\n")
        
    if opciones==3:
        salir = True
        print ("Fin\n")
    

