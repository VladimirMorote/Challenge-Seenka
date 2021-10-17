texto = "La historia de la ópera tiene una duración relativamente corta dentro del contexto de la historia de la música en general: apareció en 1597, fecha en que se creó la primera ópera."
texto2 = "Para mantener sus tardes abiertas para el tiempo en familia, Pablo aborda sus tareas diarias y su agitado horario con rápida ayuda."
texto3 = "Cuando se prepara para su tradición favorita, la semanal cena familiar, Antonia usa la ayuda para preparar temporizadores y encontrar recetas sin sus manos."
tam = 30

def justificar(texto,tam):
    linea = ""
    lista = []
    resto = ""
    i = 1
    resultado = ""
    for letra in texto:
        if i < 30:
            '''Se arma la línea hasta el caracter 30'''
            linea += letra
            if letra != " ":
                '''En la variable resto se va guardando cada palabra que se suma a la línea'''
                resto += letra
            else:
                '''Si ya la palabra se cargó en la línea, la variable resto se vacía para guardar la palagra siguiente'''
                resto = ""
            i += 1
        elif letra == " ":
            '''Si el último caracter de la línea es un espacio, se termina la línea'''
            linea = linea.strip()
            '''Se borra el último caracter'''
            lista = linea.split()
            if len(linea) == 30:
                '''Acá se pregunta si la línea es justo de 30 caracteres con la línea completa.
                Se puede dar que casualmente la línea no necesite ser justificada.'''
                resultado += linea + "\n"
                linea = ""
                i = 1
            else:
                '''Se pasa la linea a un formato de lista'''
                lista.insert(1," ")
                '''Se inserta un espacio después de la primer palabra'''
                linea = ""
                for palabra in lista:
                    '''En este for se arma la línea correcta a partir de la lista y con el espacio que se insertó'''
                    if palabra != " ":
                        linea += palabra + " "
                    else:
                        linea += palabra
                linea = linea.strip()
                '''Línea terminada'''
                resultado += linea + "\n"
                linea = ""
                i = 1
        else:
            '''En esta parte del if se ingresa si el último caracter no es un espacio.
            Cuando esto pasa, quiere decir que una palabra se está cortando y hay que eliminarla de la línea'''
            linea = linea[:-len(resto)]
            '''Se borra la palabra parcial en resto de la línea.'''
            linea = linea.strip()
            '''Se elimina el espacio en blanco al final de la línea'''
            lista = linea.split()
            '''Se pasa la linea a un formato de lista'''
            espacios = 30 - len(linea)
            '''Se calcula los espacios en blanco que hay que agregar a la línea para que llegue a 30 caracteres.'''
            ratio = espacios / (len(lista) - 1)
            '''Se calcula cuantos espacios en blanco van entre cada palabra'''
            if ratio > 1:
                '''Si el ratio es mayor a 1, se tiene que agregar al menos 1 espacio entre cada palabra'''
                if ratio % (len(lista) - 1) == 0:
                    '''Si el módulo del ratio por la cantidad de palabras es 0, quiere decir que entre palabra 
                    y palabra tiene que haber exactamente el mismo espacio.'''
                    linea = ""
                    for palabra in lista:
                        linea += palabra + " "
                        for n in range(int(ratio)): 
                            linea += " "
                    linea = linea.strip()
                else:
                    '''Si el módulo del ratio por la cantidad de palabras no es 0, quiere decir que las primeras
                    palabras de la línea van a tener más espacios en blanco que otras.'''
                    linea = ""
                    restantes = espacios % (len(lista) - 1)
                    i = 0
                    linea = ""
                    for palabra in lista:
                        linea += palabra + " "
                        for n in range(int(ratio)): 
                            linea += " "
                        if restantes != 0:
                            linea += " "
                            restantes -= 1
                    linea = linea.strip()
            else:
                '''Si el ratio es menor que 1, solo se tienen que agregar algunos espacios en blanco en la línea'''
                linea = ""
                i = 0
                for palabra in lista:
                    if i == espacios:
                        linea += palabra + " "
                    else:
                        linea += palabra + "  "
                        i += 1
                linea = linea.strip()
            resultado += linea + "\n"


            resto += letra
            linea = resto
            i = len(resto)
    resultado += linea
    return resultado


'''Se llama a la función con el texto a justificar y el tamaño de línea'''
print("---PRIMER PRUEBA---")
print("")
a = justificar(texto,tam)
print(a)
print("\n")
print("---SEGUNDA PRUEBA---")
print("")
a = justificar(texto2,tam)
print(a)
print("\n")
print("---TERCER PRUEBA---")
print("")
a = justificar(texto3,tam)
print(a)