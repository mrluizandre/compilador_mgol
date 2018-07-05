# -*- coding: utf-8 -*-

'''
Univesidade Federal de Goiás
Engenharia de Computação
Compiladores 1
Professora: Déborah Fernandes

ANALISADOR LÉXICO e ANALISADOR SINTÁTICO
Desenvolvidor por
    Andre Luiz Cardoso da Costa
    João Paulo Pacheco Potenciano

Como executar: (Passos testados no sistema Ubuntu Linux 16.04 atualizado)
    python3 compilador.py fonte.mgol
       / \        / \          / \
        |          |            |Arquivo fonte a ser compilado
        |          |
        |          |Compilador desenvolvido
        |
        |Chama o interpretador python
'''

import sys

def busca(lista, chave, valor):
    for item in lista:
        if item[chave] == valor:
            return item
    return False

def busca_completo(lista, elemento):
    for item in lista:
        if item == elemento:
            return elemento
    return False

def chamar_funcao_por_string(objeto, nome_funcao):
    return getattr(objeto, nome_funcao)

def is_int(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        x = float(s)
        return True
    except ValueError:
        return False


class AnalisadorLexico():

    def e_letra(caractere):
        return caractere in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def e_numero(caractere):
        return caractere in '0123456789'
    def e_e(caractere):
        return caractere in 'eE'
    def e_caracterevalido(caractere):
        return caractere in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.<>=+-*/(),:;?!#$%&|\\ \n"
    def e_ponto(caractere):
        return "." == caractere
    def e_aspas(caractere):
        return "\"" == caractere
    def e_underline(caractere):
        return "_" == caractere
    def e_abrechave(caractere):
        return "{" == caractere
    def e_fechachave(caractere):
        return "}" == caractere
    def e_menorque(caractere):
        return "<" == caractere
    def e_maiorque(caractere):
        return ">" == caractere
    def e_igual(caractere):
        return "=" == caractere
    def e_mais(caractere):
        return "+" == caractere
    def e_menos(caractere):
        return "-" == caractere
    def e_vezes(caractere):
        return "*" == caractere
    def e_dividir(caractere):
        return "/" == caractere
    def e_abreparenteses(caractere):
        return "(" == caractere
    def e_fechaparenteses(caractere):
        return ")" == caractere
    def e_pontovirgula(caractere):
        return ";" == caractere
    def e_eof(caractere):
        return "" == caractere
    def e_tab(caractere):
        return "\t" == caractere
    def e_salto(caractere):
        return "\n" == caractere
    def e_espaco(caractere):
        return " " == caractere

    mapa_funcoes = {
        0: e_letra,
        1: e_numero,
        2: e_ponto,
        3: e_e,
        4: e_e,
        5: e_aspas,
        6: e_underline,
        7: e_abrechave,
        8: e_fechachave,
        9: e_menorque,
        10: e_maiorque,
        11: e_igual,
        12: e_mais,
        13: e_menos,
        14: e_vezes,
        15: e_dividir,
        16: e_abreparenteses,
        17: e_fechaparenteses,
        18: e_pontovirgula,
        19: e_caracterevalido,
        20: e_eof,
        21: e_tab,
        22: e_salto,
        23: e_espaco
    }

    tabela_de_estados = [
        [9,1,None,None,None,7,None,10,None,13,14,15,18,18,18,18,19,20,21,None,12,0,0,0],
        [None,1,2,4,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,3,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,3,None,4,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,6,None,None,None,None,None,None,None,None,None,None,5,5,None,None,None,None,None,None,None,None,None,None],
        [None,6,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,6,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,8,None,None,None,None,None,None,None,None,None,None,None,None,None,7,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [9,9,None,None,None,None,9,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,11,None,None,None,None,None,None,None,None,None,None,10,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,17,17,None,16,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,17,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    ]

    estados_finais = [
      {'estado': 1, 'tipo': 'Num'},
      {'estado': 3, 'tipo': 'Num'},
      {'estado': 6, 'tipo': 'Num'},
      {'estado': 8, 'tipo': 'Literal'},
      {'estado': 9, 'tipo': 'id'},
      {'estado': 11, 'tipo': 'Comentário'},
      {'estado': 12, 'tipo': 'EOF'},
      {'estado': 13, 'tipo': 'OPR'},
      {'estado': 14, 'tipo': 'OPR'},
      {'estado': 15, 'tipo': 'OPR'},
      {'estado': 17, 'tipo': 'OPR'},
      {'estado': 16, 'tipo': 'RCB'},
      {'estado': 18, 'tipo': 'OPM'},
      {'estado': 19, 'tipo': 'AB_P'},
      {'estado': 20, 'tipo': 'FC_P'},
      {'estado': 21, 'tipo': 'PT_V'},
    ]

    estados_nao_finais = [
        {'estado': 0, 'mensagem': 'Caractere não é válido como primeiro caractere de uma palavra da linguagem'},
        {'estado': 2, 'mensagem': 'Número com formato inválido - ponto não seguido por dígito'},
        {'estado': 4, 'mensagem': 'Número com formato inválido - \"e\" não seguido por sinal ou dígito'},
        {'estado': 5, 'mensagem': 'Número com formato inválido - sinal não seguito por dígito'},
        {'estado': 7, 'mensagem': 'Literal com formato inválido - sem fechamento'},
        {'estado': 10, 'mensagem': 'Comentário com formato inválido - sem fechamento'},
    ]

    tabela_de_simbolos = [
        {'token': 'inicio', 'lexema': 'inicio', 'tipo': ''},
        {'token': 'varinicio', 'lexema': 'varinicio', 'tipo': ''},
        {'token': 'varfim', 'lexema': 'varfim', 'tipo': ''},
        {'token': 'escreva', 'lexema': 'escreva', 'tipo': ''},
        {'token': 'leia', 'lexema': 'leia', 'tipo': ''},
        {'token': 'se', 'lexema': 'se', 'tipo': ''},
        {'token': 'entao', 'lexema': 'entao', 'tipo': ''},
        {'token': 'senao', 'lexema': 'senao', 'tipo': ''},
        {'token': 'fimse', 'lexema': 'fimse', 'tipo': ''},
        {'token': 'fim', 'lexema': 'fim', 'tipo': ''},
        {'token': 'lit', 'lexema': 'lit', 'tipo': ''},
        {'token': 'int', 'lexema': 'int', 'tipo': ''},
        {'token': 'real', 'lexema': 'real', 'tipo': ''},
    ]

    analise_inicializada = False
    estado = 0
    palavra = ""

    def mostrar_tabela_de_simbolos(self):
        print('')
        print("-----------------------------------------------------------")
        print("|{}|".format("TABELA DE SÍMBOLOS".center(57)))
        print("-----------------------------------------------------------")
        print("|{}|{}|{}|".format("TOKEN".center(15),"LEXEMA".center(30),"TIPO".center(10)))
        print("-----------------------------------------------------------")
        for item in self.tabela_de_simbolos:
            print("|{}|{}|{}|".format(item['token'].center(15),item['lexema'].center(30),item['tipo'].center(10)))
        print("-----------------------------------------------------------")

    def adicionar_item_a_tabela_de_simbolos(self,token,lexema,tipo=''):
        if token == 'id':
            if {'token': token, 'lexema': lexema,'tipo': tipo} in self.tabela_de_simbolos:
                self.tabela_de_simbolos.remove({'token': token, 'lexema': lexema,'tipo': tipo})
                self.tabela_de_simbolos.append({'token': token, 'lexema': lexema,'tipo': tipo})
            else:
                self.tabela_de_simbolos.append({'token': token, 'lexema': lexema,'tipo': tipo})

        item_lista = busca(self.tabela_de_simbolos, 'lexema', lexema)

        # if(item_lista):
        #     print("|{}|{}|{}|".format(item_lista['token'].center(15),item_lista['lexema'].center(30),item_lista['tipo'].center(10)))

    def ler_arquivo(self,caminho):
        try:
            self.arquivo = open(caminho[1],'rb')
            print("Arquivo encontrado")
            print()
        except FileNotFoundError:
            print("Algo deu errado.\n\"{}\" - Arquivo não encontrado. Verifique o caminho informado.".format(caminho[1]))
            print()
            sys.exit()
        except IndexError:
            print("Algo deu errado.\nInforme o arquivo como parametro ao chamar o compilador.")
            print("Exemplo:\npython3 compilador.py fonte.mgol")
            print("   / \        / \          / \\")
            print("    |          |            |Arquivo fonte a ser compilado")
            print("    |          |")
            print("    |          |Compilador")
            print("    |")
            print("    |Chama o interpretador python")
            print()
            sys.exit()

    def e_final(self,estado):
        final = busca(self.estados_finais,'estado',estado)
        if final:
            if self.palavra in ['inicio','varinicio','varfim','escreva','leia','se','entao','senao','fimse','fim','lit','int','real']:
                self.adicionar_item_a_tabela_de_simbolos(self.palavra,self.palavra)
                retorno = {'token': self.palavra, 'lexema': self.palavra, 'tipo': ''}
            else:
                self.adicionar_item_a_tabela_de_simbolos(final['tipo'],self.palavra)
                retorno = {'token': final['tipo'], 'lexema': self.palavra, 'tipo': ''}
            self.palavra = ''
            self.estado = 0
            return retorno
        return False

    def setar_estado(self,estado):
        self.estado = estado
        if estado == 0: self.palavra = ''

    def mostrar_cabecalho_de_tokens_lidos(self):
        print("|{}|".format("TOKENS LIDOS".center(57)))
        print("-----------------------------------------------------------")
        print("|{}|{}|{}|".format("TOKEN".center(15),"LEXEMA".center(30),"TIPO".center(10)))
        print("-----------------------------------------------------------")

    def proximo_caractere(self):
        self.caractere_atual = self.arquivo.read(1).decode('ascii')
        if self.caractere_atual == "":
            self.adicionar_item_a_tabela_de_simbolos('EOF','EOF')
            return{'token': 'EOF', 'lexema': 'EOF', 'tipo': ''}

        self.contador_caracteres += 1

        # Avalia quais expressões serão avaliadas baseado nas possibilidades do estadoa atual
        tipos_avaliar = []
        for i in range(len(self.tabela_de_estados[self.estado])):
            if not self.tabela_de_estados[self.estado][i] == None:
                tipos_avaliar.append({'funcao': i, 'ir_para': self.tabela_de_estados[self.estado][i]})

        # Avalia o caractere atual de acordo com os resultados obtidos acima
        respostas = []
        for j in tipos_avaliar:
            respostas.append({
                'resposta': self.mapa_funcoes[j['funcao']](self.caractere_atual),
                'estado': j['ir_para'],
                'caractere_atual':self.caractere_atual
            })

        # Verifica se em alguma das avaliações o retorno foi positivo
        tem_true = busca(respostas,'resposta',True)

        # Concatena caractere a palavra atual se teve retorno positivo muda o estado
        if tem_true != False:
            self.palavra += self.caractere_atual
            self.setar_estado(tem_true['estado'])
            # adiciona 1 linha a contagem
            if self.caractere_atual == "\n":
                self.contador_linhas += 1
                self.contador_caracteres = 0
        else:
            # volta 1 caractere ao caso de calabouço para reanalisá-lo
            self.arquivo.seek(-1,1)
            retorno_e_final = self.e_final(self.estado)
            if not retorno_e_final:
                self.adicionar_item_a_tabela_de_simbolos("ERRO","Erro encontrado")
                print("")
                print("ERRO LÉXICO: {}".format(busca(self.estados_nao_finais, 'estado',self.estado)['mensagem']))
                print("LINHA: {}".format(self.contador_linhas))
                print("COLUNA: {}".format(self.contador_caracteres-2))
                sys.exit()
            return retorno_e_final

    def analisa_um_token(self):
        condicao_de_parada = False
        while not condicao_de_parada:
            condicao_de_parada = self.proximo_caractere()
        return condicao_de_parada

    def analisa_arquivo_completo(self):
        while self.caractere_atual != "":
            print(self.analisa_um_token())

    def inicializa_analise(self):
        self.contador_linhas = 1;
        self.contador_caracteres = 0;
        self.caractere_atual = ":)"

        # self.mostrar_cabecalho_de_tokens_lidos()

        self.analise_inicializada = True

    def get_linha(self):
        return self.contador_linhas

    def get_coluna(self):
        return self.contador_caracteres - 2

class Pilha():
    pilha = []

    def empilha(self, valor):
        self.pilha.append(valor)

    def desempilha(self,valor):
        self.pilha.pop()

    def topo(self):
        return self.pilha[len(self.pilha)-1]

    def sem_elementos(self):
        return len(self.pilha) == 0

    def print_reduce(self,n):
        retorno = ''
        for i in range(0, n):
            if type(self.pilha[-n+i]) is str:
                retorno += self.pilha[-n+i] + " "
            if not self.sem_elementos():
                self.pilha.pop(-n+i)
        return retorno

    def mostra(self):
        print(self.pilha)

class AnalisadorSintatico():
    tabela_acao = [["s2",'erro0', 'erro0','erro0', 'erro0','erro0', 'erro0','erro0', 'erro0','erro0', 'erro0','erro0'],
                    ["Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc","Acc"],
                    ['erro2',"s4",'erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2','erro2'],
                    ['erro3','erro3','erro3','erro3',"s12",'erro3','erro3','erro3',"s10","s11",'erro3','erro3','erro3','erro3',"s14",'erro3','erro3','erro3','erro3','erro3',"s9",'erro3'],
                    ['erro4','erro4',"s17",'erro4',"s18",'erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4','erro4'],
                    ['erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5','erro5',"R2"],
                    ['erro6','erro6','erro6','erro6',"s12",'erro6','erro6','erro6',"s10","s11",'erro6','erro6','erro6','erro6',"s14",'erro6','erro6','erro6','erro6','erro6',"s9",'erro6'],
                    ['erro7','erro7','erro7','erro7',"s12",'erro7','erro7','erro7',"s10","s11",'erro7','erro7','erro7','erro7',"s14",'erro7','erro7','erro7','erro7','erro7',"s9","R16"],
                    ['erro8','erro8','erro8','erro8',"s12",'erro8','erro8','erro8',"s10","s11",'erro8','erro8','erro8','erro8',"s14",'erro8','erro8','erro8','erro8','erro8',"s9",'erro8'],
                    ['erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9','erro9',"R30"],
                    ['erro10','erro10','erro10','erro10',"s22",'erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10','erro10'],
                    ['erro11','erro11','erro11','erro11',"s26",'erro11','erro11','erro11','erro11','erro11',"s24","s25",'erro11','erro11','erro11','erro11','erro11','erro11','erro11','erro11','erro11','erro11'],
                    ['erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12',"s27",'erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12','erro12'],
                    ['erro13','erro13','erro13','erro13',"s12",'erro13','erro13','erro13',"s10","s11",'erro13','erro13','erro13','erro13',"s14",'erro13','erro13','erro13','erro13',"s32",'erro13','erro13'],
                    ['erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14','erro14',"s33",'erro14','erro14','erro14','erro14','erro14','erro14'],
                    ['errr15','errr15','errr15','errr15',"R3",'errr15','errr15','errr15',"R3","R3",'errr15','errr15','errr15','errr15',"R3",'errr15','errr15','errr15','errr15','errr15',"R3",'errr15'],
                    ['erro16','erro16',"s17",'erro16',"s18",'erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16','erro16'],
                    ['erro17','erro17','erro17',"s35",'erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17','erro17'],
                    ['erro18','erro18','erro18','erro18','erro18',"s37","s38","s39",'erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18','erro18'],
                    ['erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19','erro19',"R10"],
                    ['erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20','erro20',"R16"],
                    ['erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21','erro21',"R22"],
                    ['erro22','erro22','erro22',"s40",'erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22','erro22'],
                    ['erro23','erro23','erro23',"s41",'erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23','erro23'],
                    ['erro24','erro24','erro24',"R13",'erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24','erro24'],
                    ['erro25','erro25','erro25',"R14",'erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25','erro25'],
                    ['erro26','erro26','erro26',"R15",'erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26','erro26'],
                    ['erro27','erro27','erro27','erro27',"s44",'erro27','erro27','erro27','erro27','erro27','erro27',"s45",'erro27','erro27','erro27','erro27','erro27','erro27','erro27','erro27','erro27','erro27'],
                    ['erro28','erro28','erro28','erro28',"R23",'erro28','erro28','erro28',"R23","R23",'erro28','erro28','erro28','erro28',"R23",'erro28','erro28','erro28','erro28',"R23","R23",'erro28'],
                    ['erro29','erro29','erro29','erro29',"s12",'erro29','erro29','erro29',"s10","s11",'erro29','erro29','erro29','erro29',"s14",'erro29','erro29','erro29','erro29',"s32",'erro29','erro29'],
                    ['erro30','erro30','erro30','erro30',"s12",'erro30','erro30','erro30',"s10","s11",'erro30','erro30','erro30','erro30',"s14",'erro30','erro30','erro30','erro30',"s32",'erro30','erro30'],
                    ['erro31','erro31','erro31','erro31',"s12",'erro31','erro31','erro31',"s10","s11",'erro31','erro31','erro31','erro31',"s14",'erro31','erro31','erro31','erro31',"s32",'erro31','erro31'],
                    ['erro32','erro32','erro32','erro32',"R29",'erro32','erro32','erro32',"R29","R29",'erro32','erro32','erro32','erro32',"R29",'erro32','erro32','erro32','erro32',"R29","R29",'erro32'],
                    ['erro33','erro33','erro33','erro33',"s44",'erro33','erro33','erro33','erro33','erro33','erro33',"s45",'erro33','erro33','erro33','erro33','erro33','erro33','erro33','erro33','erro33','erro33'],
                    ['erro34','erro34','erro34','erro34',"R4",'erro34','erro34','erro34',"R4","R4",'erro34','erro34','erro34','erro34',"R4",'erro34','erro34','erro34','erro34','erro34',"R4",'erro34'],
                    ['erro35','erro35','erro35','erro35',"R5",'erro35','erro35','erro35',"R5","R5",'erro35','erro35','erro35','erro35',"R5",'erro35','erro35','erro35','erro35','erro35',"R5",'erro35'],
                    ['erro36','erro36','erro36',"s51",'erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36','erro36'],
                    ['erro37','erro37','erro37',"R7",'erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37','erro37'],
                    ['erro38','erro38','erro38',"R8",'erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38','erro38'],
                    ['erro39','erro39','erro39',"R9",'erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39','erro39'],
                    ['erro40','erro40','erro40','erro40',"R11",'erro40','erro40','erro40',"R11","R11",'erro40','erro40','erro40','erro40',"R11",'erro40','erro40','erro40','erro40',"R11","R11",'erro40'],
                    ['erro41','erro41','erro41','erro41',"R12",'erro41','erro41','erro41',"R12","R12",'erro41','erro41','erro41','erro41',"R12",'erro41','erro41','erro41','erro41',"R12","R12",'erro41'],
                    ['erro42','erro42','erro42',"s52",'erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42','erro42'],
                    ['erro43','erro43','erro43',"R19",'erro43','erro43','erro43','erro43','erro43','erro43','erro43','erro43','erro43',"s53",'erro43','erro43','erro43','erro43','erro43','erro43','erro43','erro43'],
                    ['erro44','erro44','erro44',"R20",'erro44','erro44','erro44','erro44','erro44','erro44','erro44','erro44','erro44',"R20",'erro44','erro44',"R20",'erro44',"R20",'erro44','erro44','erro44'],
                    ['erro45','erro45','erro45',"R21",'erro45','erro45','erro45','erro45','erro45','erro45','erro45','erro45','erro45',"R21",'erro45','erro45',"R21",'erro45',"R21",'erro45','erro45','erro45'],
                    ['erro46','erro46','erro46','erro46',"R26",'erro46','erro46','<err></err>o46',"R26","R26",'erro46','erro46','erro46','erro46',"R26",'erro46','erro46','erro46','erro46',"R26","R26",'erro46'],
                    ['erro47','erro47','erro47','erro47',"R27",'erro47','erro47','erro47',"R27","R27",'erro47','erro47','erro47','erro47',"R27",'erro47','erro47','erro47','erro47',"R27","R27",'erro47'],
                    ['erro48','erro48','erro48','erro48',"R28",'erro48','erro48','erro48',"R28","R28",'erro48','erro48','erro48','erro48',"R28",'erro48','erro48','erro48','erro48',"R28","R28",'erro48'],
                    ['erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49','erro49',"s54",'erro49','erro49','erro49','erro49','erro49'],
                    ['erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50','erro50',"s55",'erro50','erro50','erro50'],
                    ['erro51','erro51',"R6",'erro51',"R6",'erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51','erro51'],
                    ['erro52','erro52','erro52','erro52',"R17",'erro52','erro52','erro52',"R17","R17",'erro52','erro52','erro52','erro52',"R17",'erro52','erro52','erro52','erro52','erro52',"R17",'erro52'],
                    ['erro53','erro53','erro53','erro53',"s44",'erro53','erro53','erro53','erro53','erro53','erro53',"s45",'erro53','erro53','erro53','erro53','erro53','erro53','erro53','erro53','erro53','erro53'],
                    ['erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54','erro54',"s57",'erro54','erro54','erro54','erro54'],
                    ['erro55','erro55','erro55','erro55',"s44",'erro55','erro55','erro55','erro55','erro55','erro55',"s45",'erro55','erro55','erro55','erro55','erro55','erro55','erro55','erro55','erro55','erro55'],
                    ['erro56','erro56','erro56',"R18",'erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56','erro56'],
                    ['erro57','erro57','erro57','erro57',"R24",'erro57','erro57','erro57',"R24","R24",'erro57','erro57','erro57','erro57',"R24",'erro57','erro57','erro57','erro57',"R24","R24",'erro57'],
                    ['erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58','erro58',"R25",'erro58','erro58','erro58','erro58','erro58']]

    erros = {
        'erro0': '"inicio" não encontrado',
        'erro2': '"varinicio" não encontrado',
        'erro3': '"fim", "leia", "escreva", "id" ou "se" não encontrado',
        'erro4': '"varfim" ou "id" não encontrado',
        'erro5': 'erro5',
        'erro6': '"fim", "se", "escreva", "leia" ou "id" não encontrado',
        'erro7': '"fim", "se", "escreva", "leia" ou "id" não encontrado',
        'erro8': '"fim", "se", "escreva", "leia" ou "id" não encontrado',
        'erro9': 'Caracteres inseridos após tag de fechamento "fim"',
        'erro10': '"id" não encontrado',
        'erro11': 'literal, número ou "id" não encontrado',
        'erro12': '"<-" não encontrado',
        'erro13': '"fimse", "leia", "escreva", "id" ou "se" não encontrado',
        'erro14': '"(" não encontrado',
        'erro15': 'erro15',
        'erro16': '"varfim" ou "id" não encontrado',
        'erro17': '";" não encontrado',
        'erro18': '"int", "real" ou "lit" não encontrado',
        'erro19': 'erro19',
        'erro20': 'erro20',
        'erro21': 'erro21',
        'erro22': '";" não encontrado',
        'erro23': '";" não encontrado',
        'erro24': '";" não encontrado',
        'erro25': 'erro25',
        'erro26': '";" não encontrado',
        'erro27': '"id" ou "Num" não encontrado',
        'erro28': 'erro28',
        'erro29': '"fimse", "escreva", "id" ou "se" não encontrado',
        'erro30': '"fimse", "escreva", "id" ou "se" não encontrado',
        'erro31': '"fimse", "escreva", "id" ou "se" não encontrado',
        'erro32': 'Não válido após "fimse"',
        'erro33': '"id"  ou "Num" não encontrado',
        'erro34': 'erro34',
        'erro35': 'erro35',
        'erro36': '";" não encontrado',
        'erro37': 'erro37',
        'erro38': 'erro38',
        'erro39': 'erro39',
        'erro40': 'erro40',
        'erro41': '";" não encontrado',
        'erro42': '";" não encontrado',
        'erro43': '"operador matemático" não encontrado',
        'erro44': '";" não encontrado',
        'erro45': '";" não encontrado',
        'erro46': 'erro46',
        'erro47': 'erro47',
        'erro48': 'erro48',
        'erro49': '")" não encontrado',
        'erro50': '"opr relacional" não encontrado',
        'erro51': 'erro51',
        'erro52': 'Não válido após fechamento de atribuição',
        'erro53': '"id" ou "Num" não encontrado',
        'erro54': '"entao" não encontrado',
        'erro55': '"id" ou "Num" não encontrado',
        'erro56': 'erro56',
        'erro57': 'Não válido após "entao"',
        'erro58': 'erro58',
    }

    tabela_trasicao = [[1,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,3,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,5,None,None,None,6,None,7,None,None,8,13,None,None],
                        [None,None,None,15,16,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,19,None,None,None,6,None,7,None,None,8,13,None,None],
                        [None,None,20,None,None,None,6,None,7,None,None,8,13,None,None],
                        [None,None,21,None,None,None,6,None,7,None,None,8,13,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,23,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,29,None,30,None,None,31,13,28,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,34,16,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,36,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,42,43,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,29,None,30,None,None,31,13,46,None],
                        [None,None,None,None,None,None,29,None,30,None,None,31,13,47,None],
                        [None,None,None,None,None,None,29,None,30,None,None,31,13,48,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,50,None,None,None,49],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,56,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,58,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
                        [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
    ]

    terminais = {
        "inicio": 0,
        "varinicio": 1,
        "varfim": 2,
        "PT_V": 3,
        "id": 4,
        "int": 5,
        "real": 6,
        "lit": 7,
        "leia": 8,
        "escreva": 9,
        "Literal": 10,
        "Num": 11,
        "RCB": 12,
        "OPM": 13,
        "se": 14,
        "AB_P": 15,
        "FC_P": 16,
        "entao": 17,
        "OPR": 18,
        "fimse": 19,
        "fim": 20,
        "EOF": 21
    }

    nao_terminais = {
        "P": 0,
        "V": 1,
        "A": 2,
        "LV": 3,
        "D": 4,
        "TIPO": 5,
        "ES": 6,
        "ARG": 7,
        "CMD": 8,
        "LD": 9,
        "OPRD":10 ,
        "COND": 11,
        "CABEÇALHO": 12,
        "CORPO": 13,
        "EXP_R": 14
    }

    numero_producoes = {
        # nº da regra : [número de itens a tirar da pilha, redição do lado direito, tem regra semântica],
        2: [6, "P", False],
        3: [4, "V", False],
        4: [4, "LV", False],
        5: [4, "LV", True],
        6: [6, "D", True],
        7: [2, "TIPO", True],
        8: [2, "TIPO", True],
        9: [2, "TIPO", True],
        10: [4, "A", False],
        11: [6, "ES", True],
        12: [6, "ES", True],
        13: [2, "ARG", True],
        14: [2, "ARG", True],
        15: [2, "ARG", True],
        16: [4, "A", False],
        17: [8, "CMD", True],
        18: [6, "LD", True],
        19: [2, "LD", True],
        20: [2, "OPRD", True],
        21: [2, "OPRD", True],
        22: [4, "A", False],
        23: [4, "COND", True],
        24: [10, "CABEÇALHO", True],
        25: [6, "EXP_R", True],
        26: [4, "CORPO", False],
        27: [4, "CORPO", False],
        28: [4, "CORPO", False],
        29: [2, "CORPO", False],
        30: [2, "A", False]
    }

    def analisa(self):
        # Inicializa Sintático
        lexico = AnalisadorLexico()
        lexico.ler_arquivo(sys.argv)
        lexico.inicializa_analise()


        # Inicializa Semântico
        semantico = AnalisadorSemantico(lexico)
        print("\nAção semântica - inicializa escrita no arquivo de saída\n")


        # Inicializa pilha
        pilha = Pilha()
        pilha.empilha(0)

        # Pede primeiro token ao léxico
        token = lexico.analisa_um_token()

        while(True):
            s = pilha.topo()
            resposta_acao = self.tabela_acao[s][self.terminais[token['token']]]
            if(resposta_acao[0] == 's'):
                pilha.empilha(token['lexema']) #empilha lexeme
                pilha.empilha(int(resposta_acao[1:])) # empilha estado seguinte
                token = lexico.analisa_um_token() #pega primeiro token
            elif(resposta_acao[0] == 'R'):
                producao_numero = self.numero_producoes[int(resposta_acao[1:])]
                producao = "{} => ".format(producao_numero[1]) + pilha.print_reduce(producao_numero[0])
                print(producao)
                topo = pilha.topo()
                pilha.empilha(producao_numero[1]) #empilha produção
                pilha.empilha(self.tabela_trasicao[topo][self.nao_terminais[producao_numero[1]]])

                # verfica e chama semântico
                if producao_numero[2]:
                    numero_regra = resposta_acao[1:]

                    print("Ação semântica - regra {}\n".format(numero_regra))
                    chamar_funcao_por_string(semantico,'regra' + numero_regra)(producao)


            elif(resposta_acao == "Acc"):
                print("P' => P")
                semantico.fechar_arquivo()
                print("\nAção semântica - finaliza escrita no arquivo de saída\n")
                print()
                print("Compilação comcluída com sucesso!")
                print("Arquivo de saída => \"programa.c\"")
                break;
            else:
                print("")
                print("ERRO SINTÁTICO: {}".format(self.erros[resposta_acao]))
                print("LINHA: {}".format(lexico.get_linha()))
                print("COLUNA: {}".format(lexico.get_coluna()))
                break;

class AnalisadorSemantico():

    temp_tipo = ''
    temp_arg = ''
    temp_oprd = []
    temp_ld = ''
    temp_exp_r = ''
    cont_variavel_t = 0
    variaveis_t = []

    def __init__(self, lexico):
        self.lexico = lexico
        self.arquivo = open('programa.c','w')
        self.arquivo.write('#include <stdio.h>\n\n')
        self.arquivo.write('typedef int bool;\n')
        self.arquivo.write('typedef char lit[256];\n\n')
        self.arquivo.write('void main(void)\n')
        self.arquivo.write('{\n')
        self.arquivo.write('/*----Variáveis temporárias----*/\n')

    def fechar_arquivo(self):
        self.arquivo.write("}")
        self.arquivo.close() #fechar o arquivo


        # gera as linhas de declaração das variáveis temporárias
        vs_temp = ''
        for item in self.variaveis_t:
            vs_temp += "{} {};\n".format(item['tipo'], item['lexema'])
        vs_temp += '/*-----------------------------*/\n'

        #lê o arquivo antes de inserir as variáveis temporários como um array, 1 linha por item
        arquivo = open('programa.c','r')
        conteudo = arquivo.readlines()
        arquivo.close()

        #insere as declarações no array lido no item anterior
        conteudo.insert(8,vs_temp)

        #escreve o novo conteúdo já com as declarações
        arquivo = open('programa.c','w')
        conteudo = "".join(conteudo)
        arquivo.write(conteudo)
        arquivo.close()

    def regra5(self, expressao = ''):
        self.arquivo.write("\n\n\n")

    def regra6(self, expressao = ''):
        id_lexema = expressao.split()[2]
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',id_lexema)
        self.lexico.adicionar_item_a_tabela_de_simbolos(token['token'], token['lexema'], self.temp_tipo)
        self.arquivo.write("{} {};\n".format(self.temp_tipo,id_lexema))


    def regra7(self, expressao = ''):
        self.temp_tipo = expressao.split()[2]

    def regra8(self, expressao = ''):
        self.temp_tipo = 'double'

    def regra9(self, expressao = ''):
        self.temp_tipo = expressao.split()[2]

    def regra11(self, expressao = ''):
        id_lexema = expressao.split()[3]
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',id_lexema)

        if token['tipo'] != '':
            if token['tipo'] == 'lit':
                self.arquivo.write("scanf(\"%s\", {});\n".format(token['lexema']))
            if token['tipo'] == 'int':
                self.arquivo.write("scanf(\"%d\", &{});\n".format(token['lexema']))
            if token['tipo'] == 'real':
                self.arquivo.write("scanf(\"%lf\", &{});\n".format(token['lexema']))
        else:
            self.mostrar_erro("Variável não declarada")

    def regra12(self, expressao = ''):
        # self.arquivo.write("printf({});\n".format(self.temp_arg))
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',self.temp_arg)
        if token:
            if token['tipo'] == 'double':
                self.arquivo.write("printf(\"%lf\",{});\n".format(self.temp_arg))
            elif token['tipo'] == 'int':
                self.arquivo.write("printf(\"%d\",{});\n".format(self.temp_arg))
        else:
            self.arquivo.write("printf(\"%s\",{});\n".format(self.temp_arg))

    def regra13(self, expressao = ''):
        self.temp_arg = expressao.split(' => ')[1]

    def regra14(self, expressao = ''):
        self.temp_arg = expressao.split()[2]

    def regra15(self, expressao = ''):
        id_lexema = expressao.split()[2]
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',id_lexema)

        if token['tipo'] != '':
            self.temp_arg = token['lexema']
        else:
            self.mostrar_erro("Variável não declarada")

    def regra17(self, expressao = ''):
        id_lexema = expressao.split()[2]
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',id_lexema)

        if token['tipo'] != '':
            if token['tipo'] == self.temp_ld['tipo']:
                self.arquivo.write("{} = {};\n".format(token['lexema'], self.temp_ld['lexema']))
            else:
                self.mostrar_erro("Tipos diferentes para atribuição")
        else:
            self.mostrar_erro("Variável não declarada")

    def regra18(self, expressao = ''):
        opm = expressao.split()[3]
        oprd1 = self.temp_oprd.pop()
        oprd2 = self.temp_oprd.pop()

        if (oprd1['tipo'] == oprd2['tipo']) and oprd1['tipo'] != 'lit':
            v = "T{}".format(self.cont_variavel_t)
            self.cont_variavel_t+=1
            self.temp_ld = {'tipo': oprd1['tipo'], 'lexema': v}
            self.variaveis_t.append(self.temp_ld)
            self.arquivo.write("{} = {} {} {};\n".format(v, oprd2['lexema'], opm, oprd1['lexema']))
        else:
            self.mostrar_erro("Operandos com tipos incompatíveis")

    def regra19(self, expressao = ''):
        self.temp_ld = self.temp_oprd.pop()

    def regra20(self, expressao = ''):
        id_lexema = expressao.split()[2]
        token = busca(self.lexico.tabela_de_simbolos, 'lexema',id_lexema)

        if token['tipo'] != '':
            self.temp_oprd.append({'tipo': token['tipo'], 'lexema': token['lexema']})
        else:
            self.mostrar_erro("Variável não declarada")

    def regra21(self, expressao = ''):
        self.temp_oprd.append({'tipo': 'int' if is_int(expressao.split()[2]) else 'double', 'lexema': expressao.split()[2]})

    def regra23(self, expressao = ''):
        self.arquivo.write("}\n")

    def regra24(self, expressao = ''):
        self.arquivo.write("if({})".format(self.temp_exp_r)+"{\n")

    def regra25(self, expressao = ''):
        opr = expressao.split()[3]
        oprd1 = self.temp_oprd.pop()
        oprd2 = self.temp_oprd.pop()

        if (oprd1['tipo'] == oprd2['tipo']) and oprd1['tipo'] != 'lit':
            v = "T{}".format(self.cont_variavel_t)
            self.cont_variavel_t+=1
            self.variaveis_t.append({'tipo': 'bool', 'lexema': v})
            self.temp_exp_r = v
            self.arquivo.write("{} = {} {} {};\n".format(v, oprd2['lexema'], opr, oprd1['lexema']))
        else:
            self.mostrar_erro("Operandos com tipos incompatíveis")

    def mostrar_erro(self,mensagem):
        print("ERRO SEMÂNTICO: {}".format(mensagem))
        print("LINHA: {}".format(self.lexico.get_linha()))
        print("COLUNA: {}".format(self.lexico.get_coluna()))

def main():
    print(''.rjust(59,'-'))
    print('|{}|'.format('COMPILADOR v1.0'.center(57)))
    print('|{}|'.format('Desenvolvido por André Costa e João Paulo Potenciano'.center(57)))
    print(''.rjust(59,'-'))

    sintatico = AnalisadorSintatico()
    sintatico.analisa()

if __name__ == "__main__":
    main()
