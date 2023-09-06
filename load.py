import pickle

def Aescritura_desplazado(archivo,desplazamiento,data):
   archivo.seek(desplazamiento)
   data_serizada = pickle.dumps(data)
   archivo.write(data_serizada)

def Alectura_desplazado(archivo,desplazamiento,data):
   archivo.seek(desplazamiento)
   data_serializada = archivo.read()
   try:
      return pickle.loads(data_serializada)
   except Exception as e:
      return data