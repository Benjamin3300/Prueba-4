#Sistema de gestion de estudiantes

Estudiantes=[]

def validar_nombre(nombre):
 return nombre.strip() != ""  


def validar_edad(edad):
 return edad >0    



def validar_nota(nota):
 return nota >0



#COMPONENTES DEL MENU
def mostrar_menu():
 print("\n=====MENU PRINCIPAL=======")
 print("1.Agregar estudiante")
 print("2.Buscar estudiante")
 print("3.Eliminar estudiante")
 print("4.Actualizar estados")
 print("5.Mostrar estudiantes")
 print("6.Salir")


def leer_opcion():
 while True:
  try:
   opcion=int(input("Seleccione una opcion (1-6): "))

  if 1<=opcion<=6:
   return opcion

 else:
  print("Solo se le permite ingresar una opcion entre el 1 y 6")

 except ValueError:  
print("Error: Debe ingresar un numero entero valido") 

def agregar_estudiante(lista):
 nombre=input("ingrese el nombre: ")
 
 if not validar_nombre(nombre):
  print("Error: El nombre no puede estar vacio")
  return
 
 try:
  edad=int(input("Ingrese edad: "))
  if not validar_edad(edad):
   print("Error: La edad debe de ser un numero mayor a cero")
   return
  
 except ValueError:
  print("Error: La edad debe de ser un numero entero")
  return

try:
 nota=float(input("ingrese la nota: "))
 if not validar_nota(nota):
  print("Error: Debe ingresar una nota mayor que cero")
 return
except ValueError:
 print("Error: Debe ingresar un numero decimal")

estudiante={"nombre":nombre,
            "edad":edad,
            "nota":nota,
            "aprobado": False}

lista.append(estudiante)
print("Estudiante agregado correctamente")

def buscar_estudiante(lista,nombre):
 for i in range(len(lista)):
  if lista[i][nombre]==nombre:
   return i
  return -1
 
def eliminar_estudiante(lista):
 nombre=input("Ingrese nombre a eliminar: ")

 posicion= buscar_estudiante(lista,nombre) 

 if posicion != -1:
  lista.pop(posicion)
  print("Estudiante eliminado correctamente")

 else:
  print(f" El estudiante {nombre} no se encuentra registrado")

def actualizar_estados(lista):
 for estudiante in lista:
  if estudiante["nota"]>4.0:
   estudiante["aprobado"]=True
  else:
   estudiante["aprobado"]=False

 print("Estados actualizados correctamente")      

def mostrar_estudiantes(lista):
 actualizar_estados(lista)

 if len(lista)==0:
  print("No existen estudiantes registrados")
  return
 
print("\n==LISTA DE ESTUDIANTES===")

for estudiante in lista:
 estado="APROBADO" if estudiante["aprobado"] else "REPROBADO"

 print(f"Nombre: {estudiante["nombre"]}")
 print(f"Edad: {estudiante["edad"]}")
 print(f"Nota: {estudiante["nota"]}")
 print(f"Estado {estado}")
 print("==============")


while True:
 mostrar_menu()
 opcion=leer_opcion()

 if opcion==1:
  agregar_estudiante(estudiante)

 elif opcion==2:
  nombre=input("Ingrese nombre a buscar: ")

  posicion=buscar_estudiante(estudiante,nombre)

  if posicion != -1:
   est=estudiante[posicion]

   print("\nEstudiante Encontrado") 
   print("Posicion: ", posicion)
   print("Nombre: ",est["nombre"])
   print("Edad: ",est["edad"])
   print("Nota ",est["nota"])
   print("Aprobado ",est["aprobado"])

 else:
  print("Estudiante no encontrado")

 elif opcion==3:
eliminar_estudiante(estudiante)

elif opcion==4:
actualizar_estados(estudiante)

elif opcion==5:
 mostrar_estudiantes(Estudiantes)

 elif opcion==6:
 print("Gracias por usar nuestro sistema, vuelva pronto")
 break

else:
print("Ingrese una opcion valida")


 

