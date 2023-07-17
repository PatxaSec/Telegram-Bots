import telebot

# Token del bot de Telegram
TOKEN = '6380866038:AAEX-uHUc_8konAZGR55I4aF7d6Jjnq1LyM'

# Crear instancia del bot
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, '¡Hola! Bienvenido al bot de Python. ¿En qué puedo ayudarte?')

# Comando /ayuda
@bot.message_handler(commands=['ayuda', 'help'])
def send_help(message):
    response = '''
    Puedes hacerme preguntas sobre Python o usar los siguientes comandos:

    - /ayuda, /help: Muestra esta ayuda.
    - /variable: Información sobre variables en Python.
    - /funcion: Información sobre funciones en Python.
    - /condicional: Información sobre condicionales en Python.
    - /bucle: Información sobre bucles en Python.
    - /excepcion: Información sobre excepciones en Python.
    - /operador: Información sobre operadores en Python.
    - /string: Información sobre el manejo de strings en Python.
    '''

    bot.reply_to(message, response)

# Comando /variable
@bot.message_handler(commands=['variable'])
def send_variable_info(message):
    response = '''
    En Python, una variable es un contenedor que almacena un valor. Los tipos de datos en Python incluyen:

    - Números:
      - int: números enteros, ej. 10
      - float: números decimales, ej. 3.14
      - complex: números complejos, ej. 2+3j

    - Cadena de caracteres (string):
      - str: secuencia de caracteres, ej. "Hola, mundo!"

    - Booleano:
      - bool: representa un valor verdadero (True) o falso (False)

    - Listas:
      - list: colección ordenada y modificable de elementos

    - Tuplas:
      - tuple: colección ordenada e inmutable de elementos

    - Conjuntos:
      - set: colección desordenada de elementos únicos

    - Diccionarios:
      - dict: colección de pares clave-valor

    Ejemplo de declaración de variables:

    nombre = "Juan"
    edad = 25
    precio = 10.99
    is_valid = True
    '''

    bot.reply_to(message, response)

# Comando /funcion
@bot.message_handler(commands=['funcion'])
def send_function_info(message):
    response = '''
    En Python, una función es un bloque de código reutilizable que realiza una tarea específica.
    Ejemplo de declaración de función:

    def suma(a, b):
        return a + b

    resultado = suma(3, 4)
    print(resultado)  # Salida: 7
    '''

    bot.reply_to(message, response)

# Comando /condicional
@bot.message_handler(commands=['condicional'])
def send_conditional_info(message):
    response = '''
    En Python, un condicional permite ejecutar diferentes bloques de código según una condición.
    Ejemplo de condicional:

    edad = 18

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")
    '''

    bot.reply_to(message, response)

# Comando /bucle
@bot.message_handler(commands=['bucle'])
def send_loop_info(message):
    response = '''
    En Python, un bucle se utiliza para repetir un bloque de código varias veces.
    Ejemplo de bucle:

    for i in range(5):
        print(i)

    # Salida:
    # 0
    # 1
    # 2
    # 3
    # 4
    '''

    bot.reply_to(message, response)

# Comando /excepcion
@bot.message_handler(commands=['excepcion'])
def send_exception_info(message):
    response = '''
    En Python, las excepciones manejan errores y situaciones excepcionales.
    Ejemplo de uso de excepción:

    try:
        numero = int("abc")
    except ValueError:
        print("Ocurrió un error de valor")

    '''

    bot.reply_to(message, response)

# Comando /operador
@bot.message_handler(commands=['operador'])
def send_operator_info(message):
    response = '''
    En Python, los operadores se utilizan para realizar operaciones en variables y valores.
    Ejemplo de uso de operadores:

    - Operadores matemáticos:
      - Suma: +
      - Resta: -
      - Multiplicación: *
      - División: /
      - División entera: //
      - Módulo: %

    - Operadores lógicos:
      - AND: and, &
      - OR: or, |
      - NOT: not, !

    Ejemplo de operadores lógicos:

    a = True
    b = False

    resultado_and = a and b
    resultado_or = a or b
    resultado_not = not a

    '''

    bot.reply_to(message, response)

# Comando /string
@bot.message_handler(commands=['string'])
def send_string_info(message):
    response = '''
    En Python, existen cuatro maneras de incluir variables dentro de un string:

    1. Concatenación:
       variable = "mundo"
       saludo = "Hola, " + variable

    2. Interpolación de variables:
       variable = "mundo"
       saludo = "Hola, {}".format(variable)

    3. F-strings (formatted string literals) - a partir de Python 3.6:
       variable = "mundo"
       saludo = f"Hola, {variable}"

    4. Literales de cadena formateados (con operador de porcentaje):
       variable = "mundo"
       saludo = "Hola, %s" % variable

    Ejemplo de uso de estas formas:

    nombre = "Juan"
    edad = 25

    mensaje_concatenacion = "Hola, " + nombre + ". Tienes " + str(edad) + " años."
    mensaje_interpolacion = "Hola, {}. Tienes {} años.".format(nombre, edad)
    mensaje_fstrings = f"Hola, {nombre}. Tienes {edad} años."
    mensaje_literal = "Hola, %s. Tienes %d años." % (nombre, edad)

    print(mensaje_concatenacion)
    print(mensaje_interpolacion)
    print(mensaje_fstrings)
    print(mensaje_literal)
    '''

    bot.reply_to(message, response)


# Responder a mensajes de texto
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    text = message.text.lower()

    # Palabras clave y respuestas
    keywords = {
        'variable': 'Una variable en Python es un contenedor que almacena un valor.',
        'funcion': 'Una función en Python es un bloque de código reutilizable que realiza una tarea específica.',
        'condicional': 'Un condicional en Python permite ejecutar diferentes bloques de código según una condición.',
        'bucle': 'Un bucle en Python se utiliza para repetir un bloque de código varias veces.',
    }

    # Buscar palabras clave y enviar respuesta
    for keyword, response in keywords.items():
        if keyword in text:
            bot.reply_to(message, response)
            return


# Iniciar el bot
bot.polling()