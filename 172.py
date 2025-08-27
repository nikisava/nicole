class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
class Alumno(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)
class Profesor(Persona):
    def __init__(self,nombre):
        super().__init__(nombre)
class Clase:
    def __init__(self,materia,grado,division,profesor):
        self.materia=materia
        self.grado=grado
        self.division=division
        self.alumnos=[]
        self.profesor=profesor
    def agregar_alumno(self,nombre):
        alumno=Alumno(nombre)
        self.alumnos.append(alumno)
    def llenar_clase(self,nombres_de_alumnos):
        for nombre in nombres_de_alumnos:
            alumno=Alumno(nombre)
            self.agregar_alumno(alumno)
gabriel=Profesor("Gabriel")
nombres_de_alumno=["Mariana","Anghely","Dania","Belen","Juana","Rocio","Maximo","Nicole","Aaron","Rodrigo"]
tic5to1ra = Clase("TIC",5,1,gabriel)
tic5to1ra.llenar_clase(nombres_de_alumno)