# -*- coding: utf-8 -*-

import sys
import os.path
import string

class AnalisadorLexico():
    PALAVRAS_RESERVADAS = [
        'inicio',
        'varinicio',
        'varfim',
        'escreva',
        'leia',
        'se',
        'entao',
        'senao',
        'fimse',
        'fim',
        'literal',
        'inteiro',
        'real'
    ]


    automato = [
        [0,0],
        [1,1]
    ]

    tabela_de_tokens = []

    def adicionar_item_a_tabela_de_tokens(self,token,lexema,tipo):
        self.tabela_de_tokens.append({'token': token, 'lexema': lexema,'tipo': tipo})

    def ler_arquivo(self,caminho):
        self.arquivo = open(caminho)

    def e_letra(self, caractere):
        if caractere in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
            return True
        else:
            return False

    def e_numero(self, caractere):
        if caractere in '0123456789':
            return True
        else:
            return False

    def e_ponto(self,caractere):
        if caractere == '.':
            return True
        else:
            return False

    def e_e(self, caractere):
        if caractere in 'eE':
            return True
        else:
            return False


    def e_aspas(self, caractere):
        if caractere == '"':
            return True
        else:
            return False

    def e_underline(self, caractere):
        if caractere == '_':
            return True
        else:
            return False


    def e_abrechave(self, caractere):
        if caractere == '{':
            return True
        else:
            return False


    def e_fechachave(self, caractere):
        if caractere == '}':
            return True
        else:
            return False

    def e_operador_relacional(self, cadeia):
        if cadeia in "< > = <= >= <>".split():
            return True
        else:
            return False

    def e_operador_aritmetico(self, cadeia):
        if cadeia in "+ - * /".split():
            return True
        else:
            return False

    def e_abre_parenteses(self, caractere):
        if caractere == "(":
            return True
        else:
            return False

    def e_fecha_parenteses(self, caractere):
        if caractere == ")":
            return True
        else:
            return False

    def e_pontovirgula(self, caractere):
        if caractere == ";":
            return True
        else:
            return False

    def e_caracterevalido(self, caractere):
        if caractere in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.<>=+-*/(),;?!#$%&|":
            return True
        else:
            return False

    def e_eof(self, caractere):
        if caractere == "":
            return True
        else:
            return False

    def e_tab(self, caractere):
        if caractere == "\t":
            return True
        else:
            return False

    def e_salto(self, caractere):
        if caractere == "\n":
            return True
        else:
            return False

    def e_espaco(self, caractere):
        if caractere == " ":
            return True
        else:
            return False


analisador = AnalisadorLexico()
analisador.adicionar_item_a_tabela_de_tokens('id','varuaas','literal')
analisador.ler_arquivo('fonte.mgol')
for i in range(50):
    print(analisador.e_salto(analisador.arquivo.read(1)))
