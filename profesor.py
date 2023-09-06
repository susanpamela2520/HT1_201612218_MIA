class Profesor:
   def __init__(self):
      self.type = "~" * 1
      self.ide = -1 #19 bytes
      self.cui = -1
      self.nombre = "~" * 15 # 15 bytes
      self.curso = "~" * 25

   def set_type(self, type):
      self.type = type[:1].ljust(2, ' ')

   def set_ide(self, ide):
      if ide > 0:
         self.ide = ide

   def set_cui(self, cui): 
      if cui > 0:
         self.cui = cui
 
   def set_nombre(self, nombre):
      self.nombre = nombre[:15].ljust(16, ' ')

   def set_curso(self, curso):
      self.curso = curso[:25].ljust(26, ' ')

   def imprimir_info(self):
      print("Tipo: ", self.type)
      print("Id Profesor: ", self.ide)
      print("CUI: ", self.cui)
      print("Nombre: ", self.nombre)
      print("Curso: ", self.curso)