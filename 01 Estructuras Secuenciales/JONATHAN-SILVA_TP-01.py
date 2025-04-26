#Ejercicio 1
print ("Hola Mundo!!!")

#Ejercicio 2
nombre= input("Ingrese su nombre.")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre= input("Ingrese su nombre: ")
apellido= input(f"Ingrese su apellido, {nombre}: ")
edad= input(f"Ingrese su edad, {nombre} {apellido}: ")
nacion= input(f"Ingrese su nacionalidad {nombre} {apellido}: ")
print(f"Soy {nombre} {apellido},tengo {edad} años y vivo en {nacion}.")

#Ejercicio 4
pi = 3.1416
radio = float(input("Ingrese el radio del circulo: "))
area = pi * radio**2
perimetro = 2 * pi * radio
print(f"Area del circulo: {area:.2f}")
print(f"Perimetro del circulo: {perimetro:.2f}")

#Ejercicio 5
segundos = float(input("Ingrese los segundos:"))
horas = segundos/3600
print (f"Los {segundos} segundos , equivalen a {horas} horas")

#Ejercicio 6
nume = int (input("Ingrese un numero: "))
print (nume*1)
print (nume*2)
print (nume*3)
print (nume*4)
print (nume*5)
print (nume*6)
print (nume*7)
print (nume*8)
print (nume*9)
print (nume*10)

#Ejercicio 7
num1=int (input("Ingrese el primer numero: "))
num2=int (input("Ingrese el segundo numero: "))
multi=num1*num2
divi=num1/num2
suma=num1+num2
resta=num1-num2
print(f"La multiplicacion de ambos numeros es: {multi}\n La division es: {divi}\n La suma es: {suma}\n La resta es: {resta}")

#Ejercicio 8
peso=int(input("Ingrese su peso: "))
altura=float(input("ingrese su altura: "))      
indice_masa=peso/altura**2
print(f"Su indice de masa corporal es: {indice_masa}")

#Ejercicio 9
celcius=int(input("Ingrese los grados C: "))
temp_fahren=(9/5*celcius)+32
print(f"{celcius} Grados Celcius Equivalen a {temp_fahren} Grados Fahrenheit")

#Ejercicio 10
num1= int(input("Ingrese el primer numero: "))
num2= int(input("Ingrese el segundo numero: "))
num3= int(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3
print(f"El promedio de los 3 numeros es: {promedio}")