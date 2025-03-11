"""Práctica 00 | 18011658"""

# Analizador Léxico.

import ply.lex as lex

tokens = (
    'NUMERO',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'PARENTESISIZQUIERDA',
    'PARENTESISDERECHA',
    'PUNTO',
    'COMA',
    'LLAVEIZQUIERDA',
    'LLAVEDERECHA',
    'PUNTOCOMA',
    'MINUSMINUS',
    'MENORQUE',
    'MAYORQUE',
    'CORCHETEIZQUIERDA',
    'CORCHETEDERECHA',
    'COMILLASDOBLES',
    'AND',
    'DOSPUNTOS',
    'TEXTO',
    'GUIONBAJO',
    'PORCIENTO',
    'MENOSIGUAL',
    'MAYORIGUAL',
    'TILDE',
    'CIRCUMFLEX',
    'LEFTSHIFT',
    'RIGHTSHIFT',
    'PLUSEQUAL',
    'MINEQUAL',
    'VBAR',
    'RARROW',
    'COLONEQUAL',
    'DOUBLESLASH',
    'DOUBLESLASHEQUAL',
    'EXCLAMACIONIZQUIERDA',
    'EXCLAMACIONDERECHA',
    'IGUAL',
)

# Expresiones Regulares
t_NUMERO = r'\d+'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESISIZQUIERDA = r'\('
t_PARENTESISDERECHA = r'\)'
t_PUNTO = r'\.'
t_COMA = r'\,'
t_LLAVEIZQUIERDA = r'\{'
t_LLAVEDERECHA = r'\}'
t_PUNTOCOMA = r'\;'
t_MINUSMINUS = r'\-\-'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_CORCHETEIZQUIERDA = r'\['
t_CORCHETEDERECHA = r'\]'
t_COMILLASDOBLES = r'\"'
t_AND = r'\&'
t_DOSPUNTOS = r'\:'
t_TEXTO = r'[a-zA-Z]'
t_GUIONBAJO = r'\_'
t_PORCIENTO = r'\%'
t_MENOSIGUAL = r'\<='
t_MAYORIGUAL = r'\>='
t_TILDE = r'\~'
t_CIRCUMFLEX = r'\^'
t_LEFTSHIFT = r'\<<'
t_RIGHTSHIFT = r'\>>'
t_PLUSEQUAL = r'\+='
t_MINEQUAL = r'\-='
t_VBAR = r'\|'
t_RARROW = r'\->'
t_COLONEQUAL = r'\:='
t_DOUBLESLASH = r'\//'
t_DOUBLESLASHEQUAL = r'\//='
t_EXCLAMACIONIZQUIERDA = r'\¡'
t_EXCLAMACIONDERECHA = r'\!'
t_IGUAL = r'\='


def t_error(t):
    print("LEXEMA NO VALIDO '%s' " % t.value[0])

    t.lexer.skip(1)


lexer = lex.lex()

lexer.input("print(Hello_Word)")

print("-- ¡BIENVENIDO! - Analizador Léxico --\n")

while True:
    salida = lexer.token()
    if not salida:
        break
    print(salida)
