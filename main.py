texto = "La historia de la opera tiene una dura realidad en nuestra nacion"
ancho = 30

def justificar(texto,ancho):
  linea =  ""
  i = 1
  for letra in texto:
    linea += letra
    if letra != " ":
      resto += letra
    else:
      resto = ""
    i += 1
  elif letra == " ":
    linea = linea.strip()
    print(linea)
    linea = ""  
    i = 1
    else:
      linea = linea[:-len(resto)]
      print(linea)
      resto += letra

justificar(texto, ancho)

