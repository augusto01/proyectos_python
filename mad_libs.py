#mad libs (historias locas) programa que reemplaza una cadena ingresada por el usuario en un parrafo preexistente

"""

organizacion = input ('Hola que esta haciendo en este momento ? ')

#distintas formas de concatenar cadenas 
print ('Hola estoy'+organizacion)
print ('Hola estoy',organizacion)
print ('Hola estoy {}'.format(organizacion))
print (f'hola estoy {organizacion}')


print ('Hola estoy '+organizacion): Esta es una concatenación simple de cadenas usando el operador +. La variable organizacion se concatena directamente a la cadena "Hola estoy ".

print ('Hola estoy ',organizacion): Aquí se utiliza una coma para separar la cadena "Hola estoy " y la variable organizacion como dos argumentos separados para la función print(). Python agrega automáticamente un espacio entre estos dos argumentos al imprimirlos.

print ('Hola estoy {}'.format(organizacion)): Esta es una forma de formatear una cadena usando el método format(). Dentro de la cadena, se utiliza {} como marcador de posición, y luego se llama al método format() con la variable organizacion como argumento para reemplazar el marcador de posición con su valor.

print (f'hola estoy {organizacion}'): Esta es una f-string, una forma más reciente y legible de formatear cadenas en Python. La 'f' antes de la cadena indica que es una f-string. Dentro de la cadena, se puede incluir directamente el nombre de la variable (en este caso organizacion) entre llaves {} y Python la reemplazará con su valor.

En términos de legibilidad y conveniencia, las f-strings tienden a ser la forma más preferida de formatear cadenas en Python moderno debido a su claridad y concisión. Sin embargo, los otros métodos todavía son útiles y ampliamente utilizados en ciertas situaciones.

"""

#Mad libs, historias locas #

adj_usuario = input ('Ingrese un adjetivo: ')
verbo1 = input ('ingrese un verbo: ')
persona1 = input ('ingrese una persona: ')
objetivos = input ('Ingrese un objetivo: ')

madlibs = f"Programar es tan {adj_usuario}! siempre me emociona porque me encanta {verbo1} problemas. Aprende a programar con {persona1} y alcanza tus {objetivos} !"

print(madlibs)