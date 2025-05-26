# Compiladores - Trabalho 2: Analisador Sintático da Linguagem LA

## Autores
* **Nataly Cristina da Silva** (RA: 812719)
* **Gabriel Cavalca Leite** (RA: 813615)

## 1. Descrição do Projeto

Este projeto consiste na implementação de um **Analisador Sintático** para a Linguagem LA (Linguagem Algorítmica), utilizando a ferramenta ANTLR 4. O analisador recebe como entrada um arquivo de código-fonte LA e verifica se sua estrutura sintática está correta de acordo com a gramática definida. Em caso de erros sintáticos, o analisador reporta a linha e o símbolo próximo ao erro, conforme especificado na disciplina.

---

## 2. Pré-requisitos e Software Necessário

Para compilar (gerar os arquivos do analisador) e executar (testar com o corretor automático) este trabalho, você precisará dos seguintes programas e bibliotecas instalados em seu sistema operacional Windows:

* **Java Development Kit (JDK):** Versão 11 ou superior (ex: OpenJDK 17). O Java é necessário para executar a ferramenta ANTLR e o corretor automático.
    * [Download JDK](https://www.oracle.com/java/technologies/downloads/) ou [OpenJDK](https://openjdk.java.net/install/)
* **Python 3:** Versão 3.8 ou superior. O analisador sintático foi implementado em Python.
    * [Download Python](https://www.python.org/downloads/)
* **ANTLR 4 Complete JAR:** Versão 4.13.2. Esta é a ferramenta que gera o lexer e o parser a partir da gramática `LA.g4`.
    * [Download ANTLR 4.13.2 Complete JAR](https://www.antlr.org/download.html) (Procure por "Complete ANTLR 4 JAR" e baixe a versão 4.13.2). O nome do arquivo deve ser `antlr-4.13.2-complete.jar`.
* **Python ANTLR4 Runtime:** Biblioteca Python para o ANTLR.
    * Instale via pip após instalar o Python: `pip install antlr4-python3-runtime`
* **Corretor Automático da Disciplina:** O arquivo JAR fornecido pelo professor, geralmente com nome similar a `compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar`.
* **Apache NetBeans IDE (Opcional, mas Recomendado para Desenvolvimento):** Ambiente de Desenvolvimento Integrado (IDE) comumente usado na disciplina para gerenciar projetos Java e Python (com plugins apropriados). As instruções de execução abaixo são dadas para o Prompt de Comando (CMD) padrão, mas **podem ser executadas diretamente no terminal integrado do NetBeans.**

---

## 3. Estrutura de Pastas e Configuração Inicial

Primeiro, clone o repositório para uma pasta de sua escolha. Por exemplo, se você clonar em `C:\Projetos\Compiladores\Compiladores.T2`, esta será a **pasta raiz do seu projeto**.
**Passos de Configuração:**

1.  **Clone o repositório:**
    ```bash
    git clone (https://github.com/gabrielcavalca/Compiladores.T2)
    ```
    *Exemplo:* `git clone https://github.com/gabrielcavalca/Compiladores.T2 C:\Users\SEU_USUARIO\Documents\Compiladores\Compiladores.T2`

2.  **Crie a pasta `C:\antlr`** e coloque o arquivo `antlr-4.13.2-complete.jar` dentro dela. **Certifique-se do nome exato do arquivo!**
3.  **Crie a pasta `C:\corretor`** e coloque o arquivo `compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar` (fornecido pela disciplina) dentro dela.
4.  **Crie a pasta `C:\temp`** na raiz do seu drive `C:`. Ela será usada para arquivos temporários.
5.  **Posicione a pasta `casos-de-teste`** (fornecida pela disciplina) na raiz do seu drive `C:` (`C:\casos-de-teste`).
6.  **Instale o Python ANTLR4 Runtime:**
    ```bash
    pip install antlr4-python3-runtime
    ```

---

## 4. Compilação (Geração dos Arquivos do Analisador)

Este passo envolve usar a ferramenta ANTLR para gerar os arquivos Python (`LALexer.py`, `LAParser.py`, `LAListener.py`, `LAVisitor.py`) a partir da gramática `LA.g4`. Esses arquivos são essenciais para que seu `analisador_sintatico.py` funcione.

1.  **Abra o Prompt de Comando (CMD) do Windows** (ou o terminal integrado do NetBeans).
2.  **Navegue até a pasta raiz do seu projeto.** Para isso, use o comando `cd` seguido do caminho completo onde você clonou o repositório:
    ```bash
    cd SEU_CAMINHO_PARA_O_PROJETO
    ```
    *Exemplo:* `cd C:\Users\SEU_USUARIO\Documents\Compiladores\Compiladores.T2`

3.  **Execute o comando ANTLR para gerar os arquivos Python:**
    ```bash
    java -jar C:\antlr\antlr-4.13.2-complete.jar -Dlanguage=Python3 LA.g4 -visitor -o .
    ```
    * **Saída Esperada:** Você deve ver o prompt de comando retornar sem mensagens de erro críticas.
    * **Verificação:** Após executar o comando, verifique se os arquivos `LALexer.py` e `LAParser.py` (além de `LAListener.py`, `LAVisitor.py` e outros `.interp`, `.tokens`) foram criados na pasta raiz do seu projeto.

---

## 5. Execução do Analisador (com o Corretor Automático)

Após a compilação (geração dos arquivos ANTLR Python), você pode executar seu analisador usando o corretor automático fornecido pela disciplina. O corretor se encarregará de passar os casos de teste para o seu analisador e verificar as saídas.

1.  **Abra o Prompt de Comando (CMD) do Windows** (ou o terminal integrado do NetBeans).
2.  **Navegue até a pasta raiz do seu projeto (se ainda não estiver lá):**
    ```bash
    cd SEU_CAMINHO_PARA_O_PROJETO
    ```
    *Exemplo:* `cd C:\Users\SEU_USUARIO\Documents\Compiladores\Compiladores.T2`

3.  **Execute o comando do corretor automático:**
    ```bash
    java -jar "C:\corretor\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar" "python SEU_CAMINHO_PARA_O_PROJETO\analisador_sintatico.py" gcc "C:\temp" "C:\casos-de-teste" "812719, 813615" t1 t2
    ```
    * **Substitua `SEU_CAMINHO_PARA_O_PROJETO`** pelo caminho completo da pasta onde você clonou o repositório (ex: `C:\Users\SEU_USUARIO\Documents\Compiladores\Compiladores.T2`).
    * **Parâmetros do Comando:**
        * `java -jar "C:\corretor\compiladores-corretor-automatico-1.0-SNAPSHOT-jar-with-dependencies.jar"`: Comando para executar o corretor.
        * `"python SEU_CAMINHO_PARA_O_PROJETO\analisador_sintatico.py"`: Este é o comando que o corretor irá chamar para executar seu analisador. Note que `python` no Windows geralmente se refere ao Python 3.
        * `gcc`: Um argumento que o corretor espera (pode ser um placeholder ou tipo de compilador).
        * `"C:\temp"`: Caminho para a pasta temporária.
        * `"C:\casos-de-teste"`: Caminho para a pasta que contém os casos de teste.
        * `"812719, 813615"`: Seus RAs (Nataly e Gabriel).
        * `t1 t2`: Grupos de testes a serem executados (ajuste conforme necessário).

    * **Saída Esperada:** O corretor irá processar os casos de teste e exibirá o resultado de cada um, indicando se seu analisador passou ou falhou.

---
