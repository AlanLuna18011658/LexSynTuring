"""Práctica 00 | 18011658"""

# Analizador Sintáctico.

import re


class Parser:
    def parse(self, expression):
        expression = expression.replace("", "")

        if self.validate(expression):
            result = self.evaluate(expression)
            print("RESULTADO:", result)
        else:
            print("--OPERACION INVALIDA--")

    def validate(self, expression):
        return re.match(r'^[-+*/()\d\s]+$', expression) is not None

    def evaluate(self, expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            print("No es posible la división entre cero")


parser = Parser()
expression = input("OPERACIÓN >>>")
parser.parse(expression)
