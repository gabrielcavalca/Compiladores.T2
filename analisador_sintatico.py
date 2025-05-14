from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from LALexer import LALexer
from LAParser import LAParser
import sys

class MeuErroListener(ErrorListener):
    def __init__(self, output_file, lexer):
        super(MeuErroListener, self).__init__()
        self.output_file = output_file
        self.lexer = lexer

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        simbolo = offendingSymbol.text
        if simbolo == "<EOF>":
            simbolo = "EOF"
        if offendingSymbol.type == self.lexer.CADEIA_NAO_FECHADA:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(f"Linha {line}: cadeia literal nao fechada\n")
                f.write("Fim da compilacao\n")
        elif offendingSymbol.type == self.lexer.CARACTERE_INVALIDO:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(f"Linha {line}: {simbolo} - simbolo nao identificado\n")
                f.write("Fim da compilacao\n")
        elif offendingSymbol.type == self.lexer.COMENTARIO_NAO_FECHADO:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(f"Linha {line}: comentario nao fechado\n")
                f.write("Fim da compilacao\n")
        else:
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(f"Linha {line}: erro sintatico proximo a {simbolo}\n")
                f.write("Fim da compilacao\n")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 analisador_sintatico.py entrada.txt saida.txt")
        sys.exit(1)

    entrada_path = sys.argv[1]
    saida_path = sys.argv[2]

    try:
        input_stream = FileStream(entrada_path, encoding='utf-8')
        lexer = LALexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = LAParser(token_stream)
        token_stream.fill()

        token_names = lexer.symbolicNames   

        # Substitui os listeners de erro padrão
        parser.removeErrorListeners()
        parser.addErrorListener(MeuErroListener(saida_path, lexer))           

        # Tenta fazer o parsing
        parser.programa()  # regra inicial da sua gramática

        # Se chegou aqui, é porque está sintaticamente correto
        with open(saida_path, 'w', encoding='utf-8') as f:
            f.write("Programa sintaticamente correto.\n")

    except Exception as e:
        with open(saida_path, 'w', encoding='utf-8') as f:
            f.write(f"Erro durante a análise sintática: {str(e)}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
