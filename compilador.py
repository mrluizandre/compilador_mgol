# -*- coding: utf-8 -*-

'''
Univesidade Federal de Goiás
Engenharia de Computação
Compiladores 1
Professora: Déborah Fernandes

ANALISADOR LÉXICO
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

class AnalisadorLexico():

    def e_letra(caractere):
        return caractere in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def e_numero(caractere):
        return caractere in '0123456789'
    def e_e(caractere):
        return caractere in 'eE'
    def e_caracterevalido(caractere):
        return caractere in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.<>=+-*/(),:;?!#$%&|\\ "
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
        [None,1,2,None,4,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
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
        {'token': 'literal', 'lexema': 'literal', 'tipo': ''},
        {'token': 'inteiro', 'lexema': 'inteiro', 'tipo': ''},
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
        if {'token': token, 'lexema': lexema,'tipo': tipo} not in self.tabela_de_simbolos and token == 'id':
            self.tabela_de_simbolos.append({'token': token, 'lexema': lexema,'tipo': tipo})
        print("|{}|{}|{}|".format(token.center(15),lexema.center(30),tipo.center(10)))

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
            if self.palavra == '\n':
                self.adicionar_item_a_tabela_de_simbolos(final['tipo'],'Salto')
            elif self.palavra == '\t':
                self.adicionar_item_a_tabela_de_simbolos(final['tipo'],'Tab')
            elif self.palavra in ['inicio','varinicio','varfim','escreva','leia','se','entao','senao','fimse','fim','literal','inteiro','real']:
                self.adicionar_item_a_tabela_de_simbolos(self.palavra,self.palavra)
            else:
                self.adicionar_item_a_tabela_de_simbolos(final['tipo'],self.palavra)
            self.palavra = ''
            self.estado = 0
            return True
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
        if self.caractere_atual == "": return True

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
            if not self.e_final(self.estado):
                print("LINHA => {}".format(self.contador_linhas))
                print("COLUNA => {}".format(self.contador_caracteres))
                print("CONTEUDO: {}{}".format(self.palavra,self.arquivo.readline()))
                self.adicionar_item_a_tabela_de_simbolos("ERRO","Erro encontrado")
                self.op = '0'
            return True

    def analisa_um_token(self):
        condicao_de_parada = False
        while not condicao_de_parada:
            condicao_de_parada = self.proximo_caractere()

    def analisa_arquivo_completo(self):
        while self.caractere_atual != "":
            self.analisa_um_token()

    def inicializa_analise(self):
        self.contador_linhas = 1;
        self.contador_caracteres = 0;
        self.caractere_atual = ":)"

        self.mostrar_cabecalho_de_tokens_lidos()

        self.analise_inicializada = True

def main():
    print(''.rjust(59,'-'))
    print('|{}|'.format('ANALISADOR LÉXICO'.center(57)))
    print('|{}|'.format('Desenvolvido por André Costa e João Paulo Potenciano'.center(57,)))
    print(''.rjust(59,'-'))

    analisador = AnalisadorLexico()
    analisador.ler_arquivo(sys.argv)

    analisador.op = ''
    while analisador.op != '0':
        # print(''.rjust(59,'-'))
        print()
        print('1 - Mostrar tabela de símbolos')
        print('2 - Ler 1 token')
        print('3 - Ler arquivo completo')
        print('0 - Encerrar Analisador Léxico')
        # print(''.rjust(59,'-'))
        print()
        analisador.op = str(input('Informe a ação desejada:'))
        print()

        if analisador.op == '1':
            analisador.mostrar_tabela_de_simbolos()
        elif analisador.op == '2':
            if not analisador.analise_inicializada: analisador.inicializa_analise()
            analisador.analisa_um_token()
        elif analisador.op == '3':
            if not analisador.analise_inicializada: analisador.inicializa_analise()
            analisador.analisa_arquivo_completo()
        elif analisador.op == '0':
            print("👋 Até mais ver!")
        else:
            print("{} - Opção inválida".format(analisador.op))

if __name__ == "__main__":
    main()
