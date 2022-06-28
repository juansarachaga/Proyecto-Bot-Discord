class Persona:
    
    def _init_(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def getNombre(self):
        return self.nombre
    
    def setNombre(self,nombre):
        self.nombre = nombre
        
    def getEdad(self):
        return self.edad
    
    def setEdad(self,edad):
        self.edad = edad
        
    def mayorEdad(self):
        if self.edad >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")
            
    def _str_(self):
        return self.nombre + " tiene " + str(self.edad)
        
#Programa Principal
persona = Persona("Justina",6)
persona2 = Persona("Loren",17)
print(persona.getNombre())
print(persona2.getNombre())
persona.setNombre("Emiliano")
print(persona.getNombre())
persona.mayorEdad()
print(persona)
        