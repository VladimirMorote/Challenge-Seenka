texto = "La historia de la opera tiene una dura realidad en nuestra nacion"
ancho = 30

def justificar(texto,ancho):
  linea = ""
  resto = ""
  i = 1
  for letra in texto:
    if i < 30:
      linea += letra
      if letra != " ":
        resto += letra
      else:
        resto = ""
      i += 1
    elif letra == " ":
      linea = linea.strip()
      print(linea)
      print("A esta linea hay que agregarle un espacio.")
      linea = ""  
      i = 1
    else:
      linea = linea[:-len(resto)]
      linea = linea.strip()
      print(linea)
      print("A esta linea hay que agregarle" + str(30 - len(linea)) + "espacios.")
      resto += letra
      linea = resto
      i = len(resto)
  print(linea)     

justificar(texto, ancho)

