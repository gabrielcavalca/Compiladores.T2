from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from LALexer import LALexer
from LAParser import LAParser
import sys

class MeuErroListener(ErrorListener):
    """
    `MeuErroListener` é uma classe personalizada para o tratamento de erros do ANTLR4.
    Ela estende a classe padrão `ErrorListener` do ANTLR para fornecer mensagens de erro
    mais específicas e amigáveis para erros léxicos e sintáticos comuns na Linguagem de Algoritmos (LA).
    As mensagens de erro são escritas em um arquivo de saída especificado.

    **Propósito:**
    Centralizar e personalizar a forma como os erros são reportados durante a compilação,
    garantindo uma saída consistente e informativa para o usuário, ao invés das mensagens
    genéricas do ANTLR.
    """
    def __init__(self, output_file, lexer):
        """
        Construtor da classe `MeuErroListener`.

        Args:
            output_file (str): O caminho completo para o arquivo onde as mensagens de erro serão gravadas.
            lexer (LALexer): Uma instância do analisador léxico `LALexer`. É usada para acessar
                             os tipos de tokens específicos (ex: `CADEIA_NAO_FECHADA`, `CARACTERE_INVALIDO`)
                             e assim identificar e tratar erros léxicos de forma precisa.
        """
        super(MeuErroListener, self).__init__()
        self.output_file = output_file
        self.lexer = lexer

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        """
        Método responsável por tratar erros sintáticos reportados pelo parser ANTLR.
        Este método é automaticamente invocado pelo ANTLR sempre que um erro de sintaxe é detectado.

        Ele analisa o tipo do erro e o símbolo ofensivo para gerar uma mensagem
        de erro específica, que é então escrita no arquivo de saída. Após reportar o erro,
        o processo de compilação é encerrado.

        Args:
            recognizer (Parser): O objeto parser que identificou o erro.
            offendingSymbol (Token): O token (símbolo) no qual o erro sintático ocorreu.
                                     Este é o token que o parser não esperava ou não conseguiu processar.
            line (int): O número da linha no código-fonte onde o erro foi encontrado.
            column (int): O número da coluna na linha onde o erro foi encontrado.
            msg (str): A mensagem de erro padrão gerada pelo ANTLR.
            e (RecognitionException): A exceção original (do tipo `RecognitionException`) que causou o erro.
        """
        # Obtém o texto do símbolo que causou o erro.
        simbolo = offendingSymbol.text

        # Normaliza o símbolo de "fim de arquivo" (`<EOF>`) para uma representação mais limpa.
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
                # Caso o erro não se encaixe nas categorias léxicas específicas,
                # gera uma mensagem de erro sintático genérica, mas ainda útil.
                f.write(f"Linha {line}: erro sintatico proximo a {simbolo}\n")
                f.write("Fim da compilacao\n")
                
        # Encerra o programa imediatamente com um código de erro (1).
        # Isso impede que o processo continue com um código-fonte inválido,
        # e é uma prática comum para sinalizar falhas em scripts de linha de comando.
        sys.exit(1)

# ---
## Função `main()`: Ponto de Entrada do Programa
# ---
def main():
    """
    A função principal (`main`) orquestra o processo de análise sintática.
    Ela gerencia os argumentos de linha de comando, configura o analisador léxico (lexer)
    e o analisador sintático (parser) do ANTLR, integra o listener de erros personalizado,
    executa a análise e reporta o status final da compilação.

    **Etapas do Processo de Análise Sintática:**
    1.  **Validação dos Argumentos:** Verifica se os caminhos dos arquivos de entrada e saída
        foram fornecidos corretamente via linha de comando.
    2.  **Leitura do Arquivo de Entrada:** Abre e lê o código-fonte do arquivo especificado.
    3.  **Análise Léxica:** Instancia o `LALexer` para transformar o fluxo de caracteres
        do arquivo em um fluxo de tokens.
    4.  **Criação do Fluxo de Tokens:** Converte o fluxo de tokens do lexer em um
        `CommonTokenStream`, que é um buffer que o parser pode consumir.
    5.  **Inicialização do Parser:** Instancia o `LAParser` com o fluxo de tokens.
    6.  **Configuração do Listener de Erros:** Remove os listeners de erro padrão do ANTLR
        e adiciona a instância do nosso `MeuErroListener` para controle total sobre
        a saída de erros.
    7.  **Análise Sintática:** Invoca a regra inicial da gramática (`parser.programa()`),
        iniciando a construção da árvore de análise sintática.
    8.  **Reporte de Sucesso/Erro:** Se a análise sintática for concluída sem exceções,
        escreve uma mensagem de sucesso no arquivo de saída. Caso contrário, captura
        exceções gerais e reporta um erro de análise.
    """

    # 1. Validação dos Argumentos: Verifica se o número correto de argumentos foi fornecido.
    if len(sys.argv) < 3:
        # Se não houver argumentos suficientes (nome do script, arquivo de entrada, arquivo de saída),
        # imprime uma mensagem de uso e encerra o programa.
        print("Uso: python3 analisador_sintatico.py entrada.txt saida.txt")
        sys.exit(1)

    # Extrai os caminhos dos arquivos de entrada e saída dos argumentos da linha de comando.
    entrada_path = sys.argv[1]
    saida_path = sys.argv[2]

    try:
        # 2. Leitura do Arquivo de Entrada: Cria um fluxo de entrada de arquivo (`FileStream`)
        # a partir do caminho do arquivo de entrada, especificando a codificação UTF-8.
        input_stream = FileStream(entrada_path, encoding='utf-8')
        # 3. Análise Léxica: Instancia o `LALexer`, que é o gerador de tokens
        # para a gramática LA. Ele recebe o fluxo de entrada.
        lexer = LALexer(input_stream)
        # 4. Criação do Fluxo de Tokens: Cria um `CommonTokenStream`, que é uma
        # implementação de `TokenStream` que armazena todos os tokens do lexer em uma lista.
        token_stream = CommonTokenStream(lexer)
        # 5. Inicialização do Parser: Instancia o `LAParser`, que é o analisador sintático
        # para a gramática LA. Ele recebe o fluxo de tokens.
        parser = LAParser(token_stream)
        # Preenche o fluxo de tokens. Isso faz com que o lexer processe toda a entrada
        # e gere todos os tokens antes que o parser comece a consumi-los.
        token_stream.fill()

        # `token_names` é uma lista com os nomes simbólicos dos tokens, útil para depuração,
        # embora não seja usada diretamente neste fluxo principal.
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
        # 8. Reporte de Erro (Exceções Gerais): Captura quaisquer outras exceções
        # que possam ocorrer durante o processo (ex: arquivo de entrada não encontrado,
        # problemas de permissão, etc.) e as reporta no arquivo de saída.
        with open(saida_path, 'w', encoding='utf-8') as f:
            f.write(f"Erro durante a análise sintática: {str(e)}\n")
        sys.exit(1)

if __name__ == '__main__':
    main()
