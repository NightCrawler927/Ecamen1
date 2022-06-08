

'''

#super Clase
class Docente:
    def __init__(self,nombre,apellido,edad):     clase inicial con datos principales

        variables

        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.rol=rol
        self.departamento=departamento
        self.salario=salario


    def mostrar(self):    metodo de mostrar todos los datos ingresados
      
         mostramos todos los datos 

        print("Registro de Docente")
        print("Nombre: ",self.nombre,"Apellido: ",self.apellido)
        print("edad:",self.edad,"rol: ",self.rol)
        print("Departamento: ",self.edad,"Salario: ",self.rol)



ingresamos todods los datos de clases y metodods 


instancia la classe principal  personal=Docente(nombre,apellido,edad)

mostramos el metodo personal.mostrar
'''




#super Clase
class Docente:
    def __init__(self,nombre,apellido,edad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.rol=rol
        self.departamento=departamento
        self.salario=salario


    def mostrar(self):

        print("Registro de Docente")
        print("Nombre: ",self.nombre,"Apellido: ",self.apellido)
        print("edad:",self.edad,"rol: ",self.rol)
        print("Departamento: ",self.edad,"Salario: ",self.rol)


#ingresar datos de objeto de superclase
print("=========================================================")
nombre=str(input("Ingrese nombre del Docente: "))
apellido=str(input("Ingrese el apellido del Docente: "))
edad=int(input("Ingrese edad del Docente: "))
rol=str(input("Ingrese Rol de Docente: "))
departamento=str(input("Ingrese Departamento del docente: "))
salario=float(input("Ingrese sueldo del Docente: "))
print("=========================================================")

#instanciar objeto de superclase
personal=Docente(nombre,apellido,edad)

#Mostrar metodo
print(personal.mostrar())
