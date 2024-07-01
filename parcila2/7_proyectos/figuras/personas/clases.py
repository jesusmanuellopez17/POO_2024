class personas:
     def __init__(self,nombre,edad,tel):
         self.nombre=nombre
         self.edad=edad
         self.tel=tel     
class estudiantes(personas):
     def __init__(self,carrera,matricula):
         self.carrera=carrera
         self.matricula=matricula
     def getcarrera(self):
         return self.carrera
     def setcarrera(self,carrera):
         self.carrera=carrera
     def getmatricula(self):
         return self.matricula
     def setmatricula(self,matricula):
         self.matricula=matricula
     def getInfo(self):
         print(f"carrera: {self.getcarrera()} {self.getmatricula}")
class docente(personas):
     def __init__(self,nombre,edad,tel):
          super().__init__(nombre,edad,tel)
     def getnombre(self):
         return self.nombre
     def setnombre(self,nombre):
         self.nombre=nombre
     def getedad(self):
         return self.edad
     def setedad(self,edad):
         self.edad=edad
     def gettel(self):
         self.tel
     def settel(self,tel):
         self.tel=tel
     def getInfo(self):
         print(f": {self.getcarrera()} {self.getmatricula}")


          
            

