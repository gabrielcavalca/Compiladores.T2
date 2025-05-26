# Generated from LA.g4 by ANTLR 4.13.2
# encoding: utf-8

# Este arquivo Python foi gerado automaticamente pelo ANTLR 4.13.2 a partir da gramática 'LA.g4'.
# Ele atua como o parser principal para a Linguagem de Algoritmos (LA),
# convertendo o fluxo de tokens (gerado pelo lexer) em uma árvore de análise sintática.
# Essa árvore é a representação estruturada do código-fonte, essencial para as fases
# de análise semântica e geração de código.

from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

# A função serializedATN() retorna a representação serializada da ATN (Augmented Transition Network).
# A ATN é um grafo que representa a gramática de forma compacta e eficiente,
# usada pelo ANTLR para guiar o processo de análise sintática em tempo de execução.
def serializedATN():
    return [
        4,1,70,499,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,1,0,3,0,98,8,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,
        1,108,8,1,10,1,12,1,111,9,1,1,2,1,2,1,2,1,3,1,3,1,3,5,3,119,8,3,
        10,3,12,3,122,9,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,131,8,5,1,5,1,
        5,1,5,1,5,3,5,137,8,5,1,5,3,5,140,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,152,8,6,1,7,1,7,1,8,1,8,1,8,1,8,3,8,160,8,8,1,
        8,1,8,3,8,164,8,8,1,8,3,8,167,8,8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,175,
        8,9,10,9,12,9,178,9,9,1,10,3,10,181,8,10,1,10,1,10,1,10,1,10,3,10,
        187,8,10,1,11,1,11,4,11,191,8,11,11,11,12,11,192,1,12,1,12,1,12,
        1,12,1,12,3,12,200,8,12,1,13,1,13,1,13,5,13,205,8,13,10,13,12,13,
        208,9,13,1,14,1,14,1,14,5,14,213,8,14,10,14,12,14,216,9,14,1,14,
        1,14,1,14,3,14,221,8,14,1,15,3,15,224,8,15,1,15,1,15,3,15,228,8,
        15,1,15,1,15,3,15,232,8,15,1,16,3,16,235,8,16,1,16,1,16,1,17,3,17,
        240,8,17,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,3,19,250,8,19,1,
        19,5,19,253,8,19,10,19,12,19,256,9,19,1,20,1,20,1,20,5,20,261,8,
        20,10,20,12,20,264,9,20,1,20,1,20,1,20,1,21,1,21,1,21,4,21,272,8,
        21,11,21,12,21,273,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,
        1,22,3,22,286,8,22,1,23,1,23,1,23,1,24,1,24,1,24,3,24,294,8,24,1,
        24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,
        28,5,28,323,8,28,10,28,12,28,326,9,28,1,28,1,28,3,28,330,8,28,1,
        28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,5,30,341,8,30,10,30,12,
        30,344,9,30,1,31,1,31,1,31,1,31,3,31,350,8,31,1,32,1,32,1,32,1,32,
        1,32,1,32,3,32,358,8,32,1,32,1,32,1,33,5,33,363,8,33,10,33,12,33,
        366,9,33,1,34,1,34,1,34,1,34,1,34,1,35,1,35,3,35,375,8,35,1,35,1,
        35,1,35,3,35,380,8,35,5,35,382,8,35,10,35,12,35,385,9,35,1,36,1,
        36,1,36,1,36,3,36,391,8,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,
        37,5,37,401,8,37,10,37,12,37,404,9,37,1,37,1,37,1,38,1,38,1,38,1,
        38,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,
        40,1,40,1,41,1,41,1,41,1,41,1,41,5,41,431,8,41,10,41,12,41,434,9,
        41,1,42,1,42,1,42,3,42,439,8,42,1,43,1,43,1,43,5,43,444,8,43,10,
        43,12,43,447,9,43,1,44,1,44,1,44,5,44,452,8,44,10,44,12,44,455,9,
        44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,464,8,45,1,45,1,45,1,
        45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,45,1,
        45,3,45,482,8,45,1,46,1,46,1,46,3,46,487,8,46,1,46,1,46,1,47,1,47,
        1,47,5,47,494,8,47,10,47,12,47,497,9,47,1,47,0,0,48,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,0,5,
        3,0,7,8,47,48,50,50,1,0,13,16,1,0,60,61,1,0,40,41,1,0,42,44,528,
        0,97,1,0,0,0,2,109,1,0,0,0,4,112,1,0,0,0,6,120,1,0,0,0,8,123,1,0,
        0,0,10,126,1,0,0,0,12,144,1,0,0,0,14,153,1,0,0,0,16,155,1,0,0,0,
        18,171,1,0,0,0,20,180,1,0,0,0,22,190,1,0,0,0,24,194,1,0,0,0,26,201,
        1,0,0,0,28,209,1,0,0,0,30,231,1,0,0,0,32,234,1,0,0,0,34,239,1,0,
        0,0,36,243,1,0,0,0,38,247,1,0,0,0,40,257,1,0,0,0,42,268,1,0,0,0,
        44,285,1,0,0,0,46,287,1,0,0,0,48,290,1,0,0,0,50,297,1,0,0,0,52,302,
        1,0,0,0,54,308,1,0,0,0,56,318,1,0,0,0,58,333,1,0,0,0,60,337,1,0,
        0,0,62,349,1,0,0,0,64,351,1,0,0,0,66,364,1,0,0,0,68,367,1,0,0,0,
        70,374,1,0,0,0,72,390,1,0,0,0,74,395,1,0,0,0,76,407,1,0,0,0,78,416,
        1,0,0,0,80,423,1,0,0,0,82,425,1,0,0,0,84,435,1,0,0,0,86,440,1,0,
        0,0,88,448,1,0,0,0,90,481,1,0,0,0,92,483,1,0,0,0,94,490,1,0,0,0,
        96,98,3,2,1,0,97,96,1,0,0,0,97,98,1,0,0,0,98,99,1,0,0,0,99,100,3,
        4,2,0,100,101,5,1,0,0,101,1,1,0,0,0,102,108,3,8,4,0,103,108,3,24,
        12,0,104,108,3,16,8,0,105,108,3,10,5,0,106,108,3,12,6,0,107,102,
        1,0,0,0,107,103,1,0,0,0,107,104,1,0,0,0,107,105,1,0,0,0,107,106,
        1,0,0,0,108,111,1,0,0,0,109,107,1,0,0,0,109,110,1,0,0,0,110,3,1,
        0,0,0,111,109,1,0,0,0,112,113,5,2,0,0,113,114,3,6,3,0,114,5,1,0,
        0,0,115,119,3,44,22,0,116,119,3,8,4,0,117,119,3,12,6,0,118,115,1,
        0,0,0,118,116,1,0,0,0,118,117,1,0,0,0,119,122,1,0,0,0,120,118,1,
        0,0,0,120,121,1,0,0,0,121,7,1,0,0,0,122,120,1,0,0,0,123,124,5,3,
        0,0,124,125,3,26,13,0,125,9,1,0,0,0,126,127,5,4,0,0,127,128,5,68,
        0,0,128,130,5,55,0,0,129,131,3,18,9,0,130,129,1,0,0,0,130,131,1,
        0,0,0,131,132,1,0,0,0,132,133,5,56,0,0,133,134,5,58,0,0,134,136,
        3,34,17,0,135,137,5,51,0,0,136,135,1,0,0,0,136,137,1,0,0,0,137,139,
        1,0,0,0,138,140,3,22,11,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,
        1,0,0,0,141,142,3,66,33,0,142,143,5,5,0,0,143,11,1,0,0,0,144,145,
        5,6,0,0,145,146,5,68,0,0,146,147,5,58,0,0,147,148,3,34,17,0,148,
        149,5,60,0,0,149,151,3,14,7,0,150,152,5,51,0,0,151,150,1,0,0,0,151,
        152,1,0,0,0,152,13,1,0,0,0,153,154,7,0,0,0,154,15,1,0,0,0,155,156,
        5,9,0,0,156,157,5,68,0,0,157,159,5,55,0,0,158,160,3,18,9,0,159,158,
        1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,163,5,56,0,0,162,164,
        5,51,0,0,163,162,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,167,
        3,22,11,0,166,165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,169,
        3,66,33,0,169,170,5,10,0,0,170,17,1,0,0,0,171,176,3,20,10,0,172,
        173,5,57,0,0,173,175,3,20,10,0,174,172,1,0,0,0,175,178,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,19,1,0,0,0,178,176,1,0,0,0,179,181,
        5,11,0,0,180,179,1,0,0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,
        5,68,0,0,183,186,5,58,0,0,184,187,3,34,17,0,185,187,3,32,16,0,186,
        184,1,0,0,0,186,185,1,0,0,0,187,21,1,0,0,0,188,189,5,3,0,0,189,191,
        3,26,13,0,190,188,1,0,0,0,191,192,1,0,0,0,192,190,1,0,0,0,192,193,
        1,0,0,0,193,23,1,0,0,0,194,195,5,12,0,0,195,196,5,68,0,0,196,199,
        5,58,0,0,197,200,3,36,18,0,198,200,3,32,16,0,199,197,1,0,0,0,199,
        198,1,0,0,0,200,25,1,0,0,0,201,206,3,28,14,0,202,203,5,57,0,0,203,
        205,3,28,14,0,204,202,1,0,0,0,205,208,1,0,0,0,206,204,1,0,0,0,206,
        207,1,0,0,0,207,27,1,0,0,0,208,206,1,0,0,0,209,214,5,68,0,0,210,
        211,5,57,0,0,211,213,5,68,0,0,212,210,1,0,0,0,213,216,1,0,0,0,214,
        212,1,0,0,0,214,215,1,0,0,0,215,217,1,0,0,0,216,214,1,0,0,0,217,
        220,5,58,0,0,218,221,3,34,17,0,219,221,3,36,18,0,220,218,1,0,0,0,
        220,219,1,0,0,0,221,29,1,0,0,0,222,224,5,66,0,0,223,222,1,0,0,0,
        223,224,1,0,0,0,224,225,1,0,0,0,225,232,3,34,17,0,226,228,5,66,0,
        0,227,226,1,0,0,0,227,228,1,0,0,0,228,229,1,0,0,0,229,232,3,32,16,
        0,230,232,3,36,18,0,231,223,1,0,0,0,231,227,1,0,0,0,231,230,1,0,
        0,0,232,31,1,0,0,0,233,235,5,66,0,0,234,233,1,0,0,0,234,235,1,0,
        0,0,235,236,1,0,0,0,236,237,5,68,0,0,237,33,1,0,0,0,238,240,5,66,
        0,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,242,7,1,
        0,0,242,35,1,0,0,0,243,244,5,17,0,0,244,245,3,38,19,0,245,246,5,
        18,0,0,246,37,1,0,0,0,247,254,3,40,20,0,248,250,5,19,0,0,249,248,
        1,0,0,0,249,250,1,0,0,0,250,251,1,0,0,0,251,253,3,40,20,0,252,249,
        1,0,0,0,253,256,1,0,0,0,254,252,1,0,0,0,254,255,1,0,0,0,255,39,1,
        0,0,0,256,254,1,0,0,0,257,262,5,68,0,0,258,259,5,57,0,0,259,261,
        5,68,0,0,260,258,1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,
        1,0,0,0,263,265,1,0,0,0,264,262,1,0,0,0,265,266,5,58,0,0,266,267,
        3,34,17,0,267,41,1,0,0,0,268,271,5,68,0,0,269,270,5,63,0,0,270,272,
        5,68,0,0,271,269,1,0,0,0,272,273,1,0,0,0,273,271,1,0,0,0,273,274,
        1,0,0,0,274,43,1,0,0,0,275,286,3,72,36,0,276,286,3,68,34,0,277,286,
        3,74,37,0,278,286,3,64,32,0,279,286,3,56,28,0,280,286,3,54,27,0,
        281,286,3,52,26,0,282,286,3,50,25,0,283,286,3,48,24,0,284,286,3,
        46,23,0,285,275,1,0,0,0,285,276,1,0,0,0,285,277,1,0,0,0,285,278,
        1,0,0,0,285,279,1,0,0,0,285,280,1,0,0,0,285,281,1,0,0,0,285,282,
        1,0,0,0,285,283,1,0,0,0,285,284,1,0,0,0,286,45,1,0,0,0,287,288,5,
        20,0,0,288,289,3,80,40,0,289,47,1,0,0,0,290,291,5,68,0,0,291,293,
        5,55,0,0,292,294,3,94,47,0,293,292,1,0,0,0,293,294,1,0,0,0,294,295,
        1,0,0,0,295,296,5,56,0,0,296,49,1,0,0,0,297,298,5,21,0,0,298,299,
        3,66,33,0,299,300,5,22,0,0,300,301,3,80,40,0,301,51,1,0,0,0,302,
        303,5,23,0,0,303,304,3,80,40,0,304,305,5,21,0,0,305,306,3,66,33,
        0,306,307,5,24,0,0,307,53,1,0,0,0,308,309,5,25,0,0,309,310,5,68,
        0,0,310,311,5,59,0,0,311,312,3,80,40,0,312,313,5,22,0,0,313,314,
        3,80,40,0,314,315,5,21,0,0,315,316,3,66,33,0,316,317,5,26,0,0,317,
        55,1,0,0,0,318,319,5,27,0,0,319,320,3,80,40,0,320,324,5,28,0,0,321,
        323,3,58,29,0,322,321,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,
        325,1,0,0,0,325,329,1,0,0,0,326,324,1,0,0,0,327,328,5,29,0,0,328,
        330,3,66,33,0,329,327,1,0,0,0,329,330,1,0,0,0,330,331,1,0,0,0,331,
        332,5,30,0,0,332,57,1,0,0,0,333,334,3,60,30,0,334,335,5,58,0,0,335,
        336,3,66,33,0,336,59,1,0,0,0,337,342,3,62,31,0,338,339,5,57,0,0,
        339,341,3,62,31,0,340,338,1,0,0,0,341,344,1,0,0,0,342,340,1,0,0,
        0,342,343,1,0,0,0,343,61,1,0,0,0,344,342,1,0,0,0,345,350,5,47,0,
        0,346,347,5,47,0,0,347,348,5,67,0,0,348,350,5,47,0,0,349,345,1,0,
        0,0,349,346,1,0,0,0,350,63,1,0,0,0,351,352,5,31,0,0,352,353,3,80,
        40,0,353,354,5,32,0,0,354,357,3,66,33,0,355,356,5,29,0,0,356,358,
        3,66,33,0,357,355,1,0,0,0,357,358,1,0,0,0,358,359,1,0,0,0,359,360,
        5,33,0,0,360,65,1,0,0,0,361,363,3,44,22,0,362,361,1,0,0,0,363,366,
        1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,67,1,0,0,0,366,364,1,
        0,0,0,367,368,5,34,0,0,368,369,5,55,0,0,369,370,3,70,35,0,370,371,
        5,56,0,0,371,69,1,0,0,0,372,375,5,68,0,0,373,375,3,42,21,0,374,372,
        1,0,0,0,374,373,1,0,0,0,375,383,1,0,0,0,376,379,5,57,0,0,377,380,
        5,68,0,0,378,380,3,42,21,0,379,377,1,0,0,0,379,378,1,0,0,0,380,382,
        1,0,0,0,381,376,1,0,0,0,382,385,1,0,0,0,383,381,1,0,0,0,383,384,
        1,0,0,0,384,71,1,0,0,0,385,383,1,0,0,0,386,391,5,68,0,0,387,391,
        3,42,21,0,388,389,5,66,0,0,389,391,5,68,0,0,390,386,1,0,0,0,390,
        387,1,0,0,0,390,388,1,0,0,0,391,392,1,0,0,0,392,393,5,59,0,0,393,
        394,3,80,40,0,394,73,1,0,0,0,395,396,5,35,0,0,396,397,5,55,0,0,397,
        402,3,80,40,0,398,399,5,57,0,0,399,401,3,80,40,0,400,398,1,0,0,0,
        401,404,1,0,0,0,402,400,1,0,0,0,402,403,1,0,0,0,403,405,1,0,0,0,
        404,402,1,0,0,0,405,406,5,56,0,0,406,75,1,0,0,0,407,408,5,36,0,0,
        408,409,5,55,0,0,409,410,3,80,40,0,410,411,5,57,0,0,411,412,5,47,
        0,0,412,413,5,57,0,0,413,414,5,47,0,0,414,415,5,56,0,0,415,77,1,
        0,0,0,416,417,5,37,0,0,417,418,5,55,0,0,418,419,3,80,40,0,419,420,
        5,57,0,0,420,421,3,80,40,0,421,422,5,56,0,0,422,79,1,0,0,0,423,424,
        3,82,41,0,424,81,1,0,0,0,425,432,3,84,42,0,426,427,5,38,0,0,427,
        431,3,84,42,0,428,429,5,39,0,0,429,431,3,84,42,0,430,426,1,0,0,0,
        430,428,1,0,0,0,431,434,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,
        433,83,1,0,0,0,434,432,1,0,0,0,435,438,3,86,43,0,436,437,7,2,0,0,
        437,439,3,86,43,0,438,436,1,0,0,0,438,439,1,0,0,0,439,85,1,0,0,0,
        440,445,3,88,44,0,441,442,7,3,0,0,442,444,3,88,44,0,443,441,1,0,
        0,0,444,447,1,0,0,0,445,443,1,0,0,0,445,446,1,0,0,0,446,87,1,0,0,
        0,447,445,1,0,0,0,448,453,3,90,45,0,449,450,7,4,0,0,450,452,3,90,
        45,0,451,449,1,0,0,0,452,455,1,0,0,0,453,451,1,0,0,0,453,454,1,0,
        0,0,454,89,1,0,0,0,455,453,1,0,0,0,456,457,5,41,0,0,457,482,3,90,
        45,0,458,459,5,45,0,0,459,482,3,90,45,0,460,463,5,64,0,0,461,464,
        5,68,0,0,462,464,3,42,21,0,463,461,1,0,0,0,463,462,1,0,0,0,464,482,
        1,0,0,0,465,466,5,55,0,0,466,467,3,80,40,0,467,468,5,56,0,0,468,
        482,1,0,0,0,469,470,5,66,0,0,470,482,5,68,0,0,471,482,3,92,46,0,
        472,482,3,78,39,0,473,482,3,42,21,0,474,482,5,68,0,0,475,482,5,47,
        0,0,476,482,5,48,0,0,477,482,5,50,0,0,478,482,3,76,38,0,479,482,
        5,7,0,0,480,482,5,8,0,0,481,456,1,0,0,0,481,458,1,0,0,0,481,460,
        1,0,0,0,481,465,1,0,0,0,481,469,1,0,0,0,481,471,1,0,0,0,481,472,
        1,0,0,0,481,473,1,0,0,0,481,474,1,0,0,0,481,475,1,0,0,0,481,476,
        1,0,0,0,481,477,1,0,0,0,481,478,1,0,0,0,481,479,1,0,0,0,481,480,
        1,0,0,0,482,91,1,0,0,0,483,484,5,68,0,0,484,486,5,55,0,0,485,487,
        3,94,47,0,486,485,1,0,0,0,486,487,1,0,0,0,487,488,1,0,0,0,488,489,
        5,56,0,0,489,93,1,0,0,0,490,495,3,80,40,0,491,492,5,57,0,0,492,494,
        3,80,40,0,493,491,1,0,0,0,494,497,1,0,0,0,495,493,1,0,0,0,495,496,
        1,0,0,0,496,95,1,0,0,0,497,495,1,0,0,0,51,97,107,109,118,120,130,
        136,139,151,159,163,166,176,180,186,192,199,206,214,220,223,227,
        231,234,239,249,254,262,273,285,293,324,329,342,349,357,364,374,
        379,383,390,402,430,432,438,445,453,463,481,486,495
    ]

# A classe LAParser é a implementação do parser ANTLR para a gramática LA.
# Ela é responsável por analisar a sequência de tokens e construir a árvore de análise sintática.
class LAParser ( Parser ):

    # Define o nome do arquivo de gramática original.
    grammarFileName = "LA.g4"

    # Carrega a ATN (Augmented Transition Network) serializada. A ATN é um modelo de estado
    # finito que o parser utiliza para guiar sua análise, reconhecendo padrões definidos na gramática.
    atn = ATNDeserializer().deserialize(serializedATN())

    # Converte as decisões da ATN em DFAs (Deterministic Finite Automata) para otimização do parsing.
    # DFAs permitem decisões de parsing mais rápidas para regras sem ambiguidades.
    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    # Um cache compartilhado para contextos de predição. Ajuda a otimizar o desempenho
    # do parser ao evitar recalcular previsões para os mesmos estados de análise.
    sharedContextCache = PredictionContextCache()

    # literalNames: Uma lista de strings literais que correspondem diretamente aos tokens.
    # São os "nomes" dos tokens que representam palavras-chave e operadores fixos na linguagem.
    literalNames = [ "<INVALID>", "'fim_algoritmo'", "'algoritmo'", "'declare'", 
                     "'funcao'", "'fim_funcao'", "'constante'", "'verdadeiro'", 
                     "'falso'", "'procedimento'", "'fim_procedimento'", 
                     "'var'", "'tipo'", "'literal'", "'inteiro'", "'real'", 
                     "'logico'", "'registro'", "'fim_registro'", "';'", 
                     "'retorne'", "'faca'", "'ate'", "'enquanto'", "'fim_enquanto'", 
                     "'para'", "'fim_para'", "'caso'", "'seja'", "'senao'", 
                     "'fim_caso'", "'se'", "'entao'", "'fim_se'", "'leia'", 
                     "'escreva'", "'subLiteral'", "'pot'", "'e'", "'ou'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'nao'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\"'", "'('", 
                     "')'", "','", "':'", "'<-'", "'='", "<INVALID>", "<INVALID>", 
                     "'.'", "'&'", "<INVALID>", "'^'", "'..'" ]

    # symbolicNames: Uma lista de nomes simbólicos para os tokens.
    # Representam categorias de tokens (como identificadores, números, cadeias de texto)
    # ou tokens que não possuem uma representação literal fixa mas são importantes semanticamente.
    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "PALAVRA_CHAVE", "NUM_INT", 
                      "NUM_REAL", "CADEIA_NAO_FECHADA", "CADEIA", "COMENTARIO", 
                      "COMENTARIO_NAO_FECHADO", "WS", "ASPAS", "ABREPAR", 
                      "FECHAPAR", "VIRG", "DOIS_PONTOS", "ATRIBUICAO", "IGUAL", 
                      "OP_RELACIONAL", "OP_ARITMETICO", "PONTO", "E_COMERCIAL", 
                      "COLCHETES", "CIRCUNFLEXO", "PONTOS", "IDENT", "CARACTERE_INVALIDO", 
                      "ERRO" ]

    # Definição das regras de parsing e seus índices.
    # Cada número corresponde à ordem de definição da regra na gramática LA.g4.
    RULE_programa = 0
    RULE_declaracoes_preliminares = 1
    RULE_bloco_algoritmo = 2
    RULE_corpo_algoritmo = 3
    RULE_declaracao = 4
    RULE_declaracao_funcao = 5
    RULE_declaracao_constante = 6
    RULE_valor_constante = 7
    RULE_declaracao_procedimento = 8
    RULE_parametros = 9
    RULE_parametro = 10
    RULE_declaracoes_locais = 11
    RULE_declaracao_tipo = 12
    RULE_lista_variaveis = 13
    RULE_variavel = 14
    RULE_tipo = 15
    RULE_tipo_identificado = 16
    RULE_tipo_base = 17
    RULE_tipo_registro = 18
    RULE_lista_campos = 19
    RULE_campo = 20
    RULE_acesso_campo = 21
    RULE_comando = 22
    RULE_retorne = 23
    RULE_chamada_procedimento = 24
    RULE_comandofaca = 25
    RULE_comandoenquanto = 26
    RULE_comandopara = 27
    RULE_comandocaso = 28
    RULE_selecao = 29
    RULE_constantes = 30
    RULE_constante = 31
    RULE_comandose = 32
    RULE_comandos = 33
    RULE_leitura = 34
    RULE_lista_identificadores = 35
    RULE_atribuicao = 36
    RULE_escrita = 37
    RULE_subliteral = 38
    RULE_potencia = 39
    RULE_expressao = 40
    RULE_expressao_logica = 41
    RULE_expressao_relacional = 42
    RULE_expressao_aritmetica = 43
    RULE_termo = 44
    RULE_fator = 45
    RULE_chamada_funcao = 46
    RULE_lista_expressao = 47

    # Lista dos nomes das regras, correspondendo aos índices acima.
    ruleNames =  [ "programa", "declaracoes_preliminares", "bloco_algoritmo", 
                   "corpo_algoritmo", "declaracao", "declaracao_funcao", 
                   "declaracao_constante", "valor_constante", "declaracao_procedimento", 
                   "parametros", "parametro", "declaracoes_locais", "declaracao_tipo", 
                   "lista_variaveis", "variavel", "tipo", "tipo_identificado", 
                   "tipo_base", "tipo_registro", "lista_campos", "campo", 
                   "acesso_campo", "comando", "retorne", "chamada_procedimento", 
                   "comandofaca", "comandoenquanto", "comandopara", "comandocaso", 
                   "selecao", "constantes", "constante", "comandose", "comandos", 
                   "leitura", "lista_identificadores", "atribuicao", "escrita", 
                   "subliteral", "potencia", "expressao", "expressao_logica", 
                   "expressao_relacional", "expressao_aritmetica", "termo", 
                   "fator", "chamada_funcao", "lista_expressao" ]

    # Mapeamento de tokens literais para seus valores inteiros (usado internamente pelo ANTLR).
    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    PALAVRA_CHAVE=46
    NUM_INT=47
    NUM_REAL=48
    CADEIA_NAO_FECHADA=49
    CADEIA=50
    COMENTARIO=51
    COMENTARIO_NAO_FECHADO=52
    WS=53
    ASPAS=54
    ABREPAR=55
    FECHAPAR=56
    VIRG=57
    DOIS_PONTOS=58
    ATRIBUICAO=59
    IGUAL=60
    OP_RELACIONAL=61
    OP_ARITMETICO=62
    PONTO=63
    E_COMERCIAL=64
    COLCHETES=65
    CIRCUNFLEXO=66
    PONTOS=67
    IDENT=68
    CARACTERE_INVALIDO=69
    ERRO=70

    # O construtor do parser.
    # Inicializa o parser com o fluxo de tokens de entrada e configurações de saída.
    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    # Contexto para a regra 'programa'.
    # Representa a estrutura de um programa completo na Linguagem de Algoritmos.
    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

	# Retorna o contexto da regra 'bloco_algoritmo'. Um programa deve ter um bloco de algoritmo principal.
        def bloco_algoritmo(self):
            return self.getTypedRuleContext(LAParser.Bloco_algoritmoContext,0)

	# Retorna o contexto da regra 'declaracoes_preliminares'. Estas são declarações opcionais
        # que podem aparecer antes do bloco principal do algoritmo (funções, procedimentos, tipos).
        def declaracoes_preliminares(self):
            return self.getTypedRuleContext(LAParser.Declaracoes_preliminaresContext,0)

	# Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_programa

	# Métodos para o Listener Pattern:
        # enterPrograma é chamado ao entrar na regra 'programa'.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)
        # exitPrograma é chamado ao sair da regra 'programa'.
        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

    # Implementação da regra de parsing 'programa'.
    # Define a sequência esperada de tokens e sub-regras para formar um programa válido.
    def programa(self):
        # Cria um novo contexto para esta regra.
        localctx = LAParser.ProgramaContext(self, self._ctx, self.state)
	# Entra na regra 'programa'.
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
	    # Inicia o modo de alternativa externa, significando que esta é a primeira alternativa de uma regra.
            self.enterOuterAlt(localctx, 1)
	    # Tenta sincronizar o manipulador de erros.
            self.state = 97
            self._errHandler.sync(self)
	    # Prediz qual alternativa seguir (neste caso, se há declarações preliminares ou não).
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
		# Se houver, consome a regra 'declaracoes_preliminares'
                self.state = 96
                self.declaracoes_preliminares()


            self.state = 99
	    # Consome a regra 'bloco_algoritmo'.
            self.bloco_algoritmo()
            self.state = 100
	    # Espera o token 'fim_algoritmo'.
            self.match(LAParser.T__0)
        except RecognitionException as re:
	    # Em caso de erro de reconhecimento, reporta e tenta recuperar.
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
	    # Sai da regra, independentemente de sucesso ou falha.
            self.exitRule()
        return localctx

    # Contexto para a regra 'declaracoes_preliminares'.
    # Representa um conjunto de declarações (funções, procedimentos, tipos, constantes)
    # que podem aparecer no início do programa.
    class Declaracoes_preliminaresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

	# Retorna uma lista de contextos para a regra 'declaracao' (declarações de variáveis).
        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(LAParser.DeclaracaoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao_tipo' (declarações de tipos customizados).
        def declaracao_tipo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Declaracao_tipoContext)
            else:
                return self.getTypedRuleContext(LAParser.Declaracao_tipoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao_procedimento' (declarações de procedimentos).
        def declaracao_procedimento(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Declaracao_procedimentoContext)
            else:
                return self.getTypedRuleContext(LAParser.Declaracao_procedimentoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao_funcao' (declarações de funções).
        def declaracao_funcao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Declaracao_funcaoContext)
            else:
                return self.getTypedRuleContext(LAParser.Declaracao_funcaoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao_constante' (declarações de constantes).
        def declaracao_constante(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Declaracao_constanteContext)
            else:
                return self.getTypedRuleContext(LAParser.Declaracao_constanteContext,i)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_declaracoes_preliminares
		
        # Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes_preliminares" ):
                listener.enterDeclaracoes_preliminares(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes_preliminares" ):
                listener.exitDeclaracoes_preliminares(self)



    # Implementação da regra de parsing 'declaracoes_preliminares'.
    # Permite a repetição de diferentes tipos de declarações antes do bloco principal.
    def declaracoes_preliminares(self):

        localctx = LAParser.Declaracoes_preliminaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracoes_preliminares)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self._errHandler.sync(self)
	    # Loop que permite múltiplas declarações de diferentes tipos.
            _la = self._input.LA(1) # Obtém o tipo do próximo token.
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4696) != 0): # Condição que verifica se o próximo token é o início de uma das declarações permitidas.
                self.state = 107
                self._errHandler.sync(self)
                token = self._input.LA(1)
		# Seleciona qual tipo de declaração foi encontrada.
                if token in [3]: # 'declare'
                    self.state = 102
                    self.declaracao()
                    pass
                elif token in [12]:  # 'tipo'
                    self.state = 103
                    self.declaracao_tipo()
                    pass
                elif token in [9]: # 'procedimento'
                    self.state = 104
                    self.declaracao_procedimento()
                    pass
                elif token in [4]:  # 'funcao'
                    self.state = 105
                    self.declaracao_funcao()
                    pass
                elif token in [6]:  # 'constante'
                    self.state = 106
                    self.declaracao_constante()
                    pass
                else:
		    # Se nenhum dos tokens esperados for encontrado, levanta uma exceção.
                    raise NoViableAltException(self)

                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'bloco_algoritmo'.
    # Representa o corpo principal do programa, iniciando com 'algoritmo'.
    class Bloco_algoritmoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
        # Retorna o contexto da regra 'corpo_algoritmo', que contém os comandos e declarações dentro do bloco.
        def corpo_algoritmo(self):
            return self.getTypedRuleContext(LAParser.Corpo_algoritmoContext,0)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_bloco_algoritmo
		
        # Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco_algoritmo" ):
                listener.enterBloco_algoritmo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco_algoritmo" ):
                listener.exitBloco_algoritmo(self)



    # Implementação da regra de parsing 'bloco_algoritmo'.
    def bloco_algoritmo(self):

        localctx = LAParser.Bloco_algoritmoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco_algoritmo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LAParser.T__1)
            self.state = 113
	    # Consome a regra 'corpo_algoritmo'.
            self.corpo_algoritmo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'corpo_algoritmo'.
    # Representa o conteúdo principal do algoritmo, que pode incluir comandos e declarações.
    class Corpo_algoritmoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
		
        # Retorna uma lista de contextos para a regra 'comando'.
        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LAParser.ComandoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao' (declarações de variáveis).
        def declaracao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.DeclaracaoContext)
            else:
                return self.getTypedRuleContext(LAParser.DeclaracaoContext,i)

        # Retorna uma lista de contextos para a regra 'declaracao_constante'.
        def declaracao_constante(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Declaracao_constanteContext)
            else:
                return self.getTypedRuleContext(LAParser.Declaracao_constanteContext,i)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_corpo_algoritmo

	# Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCorpo_algoritmo" ):
                listener.enterCorpo_algoritmo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCorpo_algoritmo" ):
                listener.exitCorpo_algoritmo(self)



    # Implementação da regra de parsing 'corpo_algoritmo'.
    # Permite a repetição de comandos e algumas declarações dentro do corpo do algoritmo.
    def corpo_algoritmo(self):

        localctx = LAParser.Corpo_algoritmoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_corpo_algoritmo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
	    # Loop que permite comandos ou declarações.
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 53866397768) != 0) or _la==66 or _la==68:
                self.state = 118
                self._errHandler.sync(self)
                token = self._input.LA(1)
		# Seleciona qual item foi encontrado.
                if token in [20, 21, 23, 25, 27, 31, 34, 35, 66, 68]:
                    self.state = 115
                    self.comando()
                    pass
                elif token in [3]: # 'declare'
                    self.state = 116
                    self.declaracao()
                    pass
                elif token in [6]: # 'constante'
                    self.state = 117
                    self.declaracao_constante()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'declaracao'.
    # Representa a declaração de uma ou mais variáveis.
    class DeclaracaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

	# Retorna o contexto da regra 'lista_variaveis', que define as variáveis a serem declaradas.
        def lista_variaveis(self):
            return self.getTypedRuleContext(LAParser.Lista_variaveisContext,0)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_declaracao

	# Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao" ):
                listener.enterDeclaracao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao" ):
                listener.exitDeclaracao(self)



     # Implementação da regra de parsing 'declaracao'.
    def declaracao(self):

        localctx = LAParser.DeclaracaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declaracao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
	    # Espera o token 'declare'.
            self.match(LAParser.T__2)
            self.state = 124
	    # Consome a regra 'lista_variaveis'.
            self.lista_variaveis()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'declaracao_funcao'.
    # Representa a declaração completa de uma função, incluindo nome, parâmetros, tipo de retorno e corpo.
    class Declaracao_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

	# Retorna o token IDENT (nome da função).
        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

	# Retorna o token ABREPAR ('(').
        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

	# Retorna o token FECHAPAR (')').
        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

	# Retorna o token DOIS_PONTOS (':').
        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

	# Retorna o contexto da regra 'tipo_base' (tipo de retorno da função).
        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)

        # Retorna o contexto da regra 'comandos' (corpo da função).
        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)

        # Retorna o contexto da regra 'parametros' (parâmetros da função, opcional).
        def parametros(self):
            return self.getTypedRuleContext(LAParser.ParametrosContext,0)

        # Retorna o token COMENTARIO (opcional).
        def COMENTARIO(self):
            return self.getToken(LAParser.COMENTARIO, 0)

	# Retorna o contexto da regra 'declaracoes_locais' (variáveis locais, opcional).
        def declaracoes_locais(self):
            return self.getTypedRuleContext(LAParser.Declaracoes_locaisContext,0)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_declaracao_funcao

	# Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_funcao" ):
                listener.enterDeclaracao_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_funcao" ):
                listener.exitDeclaracao_funcao(self)



    # Implementação da regra de parsing 'declaracao_funcao'.
    def declaracao_funcao(self):

        localctx = LAParser.Declaracao_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declaracao_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
	    # Espera o token 'funcao'.
            self.match(LAParser.T__3)
            self.state = 127
            # Espera o IDENT (nome da função).
            self.match(LAParser.IDENT)
            self.state = 128
	    # Espera o ABREPAR '('.
            self.match(LAParser.ABREPAR)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
	    # Verifica se há parâmetros (opcional).
            if _la==11 or _la==68: # 'var' ou IDENT
                self.state = 129
                self.parametros()


            self.state = 132
	    # Espera o FECHAPAR ')'.
            self.match(LAParser.FECHAPAR)
            self.state = 133
           # Espera o DOIS_PONTOS ':'.
            self.match(LAParser.DOIS_PONTOS)
            self.state = 134
            # Consome a regra 'tipo_base' (tipo de retorno).
            self.tipo_base()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            # Verifica se há um COMENTARIO (opcional).
            if _la==51: # COMENTARIO
                self.state = 135
                self.match(LAParser.COMENTARIO)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            # Verifica se há declarações locais (opcional).
            if _la==3: # 'declare'
                self.state = 138
                self.declaracoes_locais()
            self.state = 141
            # Consome a regra 'comandos' (o corpo da função).
            self.comandos()
            self.state = 142
            # Espera o token 'fim_funcao'.
            self.match(LAParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'declaracao_constante'.
    # Representa a declaração de uma constante, com seu nome, tipo e valor inicial.
    class Declaracao_constanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

       # Retorna o token IDENT (nome da constante).
        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        # Retorna o token DOIS_PONTOS (':').
        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        # Retorna o contexto da regra 'tipo_base' (tipo da constante).
        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)

        # Retorna o token IGUAL ('=').
        def IGUAL(self):
            return self.getToken(LAParser.IGUAL, 0)

        # Retorna o contexto da regra 'valor_constante' (valor atribuído à constante).
        def valor_constante(self):
            return self.getTypedRuleContext(LAParser.Valor_constanteContext,0)

        # Retorna o token COMENTARIO (opcional).
        def COMENTARIO(self):
            return self.getToken(LAParser.COMENTARIO, 0)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_declaracao_constante

        # Métodos para o Listener Pattern.
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_constante" ):
                listener.enterDeclaracao_constante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_constante" ):
                listener.exitDeclaracao_constante(self)



    # Implementação da regra de parsing 'declaracao_constante'.
    def declaracao_constante(self):

        localctx = LAParser.Declaracao_constanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_declaracao_constante)
        self._la = 0 # Token type
        try:
           self.enterOuterAlt(localctx, 1)
            self.state = 144
            # Espera o token 'constante'.
            self.match(LAParser.T__5)
            self.state = 145
            # Espera o IDENT (nome da constante).
            self.match(LAParser.IDENT)
            self.state = 146
            # Espera o DOIS_PONTOS ':'.
            self.match(LAParser.DOIS_PONTOS)
            self.state = 147
            # Consome a regra 'tipo_base'.
            self.tipo_base()
            self.state = 148
            # Espera o IGUAL '='.
            self.match(LAParser.IGUAL)
            self.state = 149
            # Consome a regra 'valor_constante'.
            self.valor_constante()
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            # Verifica se há um COMENTARIO (opcional).
            if _la==51: # COMENTARIO
                self.state = 150
                self.match(LAParser.COMENTARIO)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    # Contexto para a regra 'valor_constante'.
    # Define os tipos de valores literais que uma constante pode assumir.
    class Valor_constanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        # Retorna o token NUM_INT (número inteiro).
        def NUM_INT(self):
            return self.getToken(LAParser.NUM_INT, 0)

        # Retorna o token NUM_REAL (número real/ponto flutuante).
        def NUM_REAL(self):
            return self.getToken(LAParser.NUM_REAL, 0)

        # Retorna o token CADEIA (string literal).
        def CADEIA(self):
            return self.getToken(LAParser.CADEIA, 0)

        # Retorna o índice desta regra.
        def getRuleIndex(self):
            return LAParser.RULE_valor_constante

        # Métodos para o Listener Pattern
        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValor_constante" ):
                listener.enterValor_constante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValor_constante" ):
                listener.exitValor_constante(self)



    # Implementação da regra de parsing 'valor_constante'.
    # Permite um dos vários tipos de literais ou palavras-chave booleanas.
    def valor_constante(self):

        localctx = LAParser.Valor_constanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_valor_constante)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1548112371908992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_procedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def parametros(self):
            return self.getTypedRuleContext(LAParser.ParametrosContext,0)


        def COMENTARIO(self):
            return self.getToken(LAParser.COMENTARIO, 0)

        def declaracoes_locais(self):
            return self.getTypedRuleContext(LAParser.Declaracoes_locaisContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_declaracao_procedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_procedimento" ):
                listener.enterDeclaracao_procedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_procedimento" ):
                listener.exitDeclaracao_procedimento(self)




    def declaracao_procedimento(self):

        localctx = LAParser.Declaracao_procedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declaracao_procedimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(LAParser.T__8)
            self.state = 156
            self.match(LAParser.IDENT)
            self.state = 157
            self.match(LAParser.ABREPAR)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11 or _la==68:
                self.state = 158
                self.parametros()


            self.state = 161
            self.match(LAParser.FECHAPAR)
            self.state = 163
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 162
                self.match(LAParser.COMENTARIO)


            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 165
                self.declaracoes_locais()


            self.state = 168
            self.comandos()
            self.state = 169
            self.match(LAParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ParametroContext)
            else:
                return self.getTypedRuleContext(LAParser.ParametroContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = LAParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.parametro()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 172
                self.match(LAParser.VIRG)
                self.state = 173
                self.parametro()
                self.state = 178
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)


        def tipo_identificado(self):
            return self.getTypedRuleContext(LAParser.Tipo_identificadoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)




    def parametro(self):

        localctx = LAParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 179
                self.match(LAParser.T__10)


            self.state = 182
            self.match(LAParser.IDENT)
            self.state = 183
            self.match(LAParser.DOIS_PONTOS)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 184
                self.tipo_base()
                pass

            elif la_ == 2:
                self.state = 185
                self.tipo_identificado()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracoes_locaisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_variaveis(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Lista_variaveisContext)
            else:
                return self.getTypedRuleContext(LAParser.Lista_variaveisContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_declaracoes_locais

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracoes_locais" ):
                listener.enterDeclaracoes_locais(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracoes_locais" ):
                listener.exitDeclaracoes_locais(self)




    def declaracoes_locais(self):

        localctx = LAParser.Declaracoes_locaisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaracoes_locais)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.match(LAParser.T__2)
                self.state = 189
                self.lista_variaveis()
                self.state = 192 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaracao_tipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        def tipo_registro(self):
            return self.getTypedRuleContext(LAParser.Tipo_registroContext,0)


        def tipo_identificado(self):
            return self.getTypedRuleContext(LAParser.Tipo_identificadoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_declaracao_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracao_tipo" ):
                listener.enterDeclaracao_tipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracao_tipo" ):
                listener.exitDeclaracao_tipo(self)




    def declaracao_tipo(self):

        localctx = LAParser.Declaracao_tipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declaracao_tipo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(LAParser.T__11)
            self.state = 195
            self.match(LAParser.IDENT)
            self.state = 196
            self.match(LAParser.DOIS_PONTOS)
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 197
                self.tipo_registro()
                pass
            elif token in [66, 68]:
                self.state = 198
                self.tipo_identificado()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_variaveisContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variavel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.VariavelContext)
            else:
                return self.getTypedRuleContext(LAParser.VariavelContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_lista_variaveis

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_variaveis" ):
                listener.enterLista_variaveis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_variaveis" ):
                listener.exitLista_variaveis(self)




    def lista_variaveis(self):

        localctx = LAParser.Lista_variaveisContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_lista_variaveis)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.variavel()
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 202
                self.match(LAParser.VIRG)
                self.state = 203
                self.variavel()
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariavelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.IDENT)
            else:
                return self.getToken(LAParser.IDENT, i)

        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)


        def tipo_registro(self):
            return self.getTypedRuleContext(LAParser.Tipo_registroContext,0)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_variavel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariavel" ):
                listener.enterVariavel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariavel" ):
                listener.exitVariavel(self)




    def variavel(self):

        localctx = LAParser.VariavelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_variavel)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(LAParser.IDENT)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 210
                self.match(LAParser.VIRG)
                self.state = 211
                self.match(LAParser.IDENT)
                self.state = 216
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 217
            self.match(LAParser.DOIS_PONTOS)
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14, 15, 16, 66]:
                self.state = 218
                self.tipo_base()
                pass
            elif token in [17]:
                self.state = 219
                self.tipo_registro()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LAParser.RULE_tipo

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TipoIdentificadoContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LAParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipo_identificado(self):
            return self.getTypedRuleContext(LAParser.Tipo_identificadoContext,0)

        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoIdentificado" ):
                listener.enterTipoIdentificado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoIdentificado" ):
                listener.exitTipoIdentificado(self)


    class TipoRegistroContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LAParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipo_registro(self):
            return self.getTypedRuleContext(LAParser.Tipo_registroContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoRegistro" ):
                listener.enterTipoRegistro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoRegistro" ):
                listener.exitTipoRegistro(self)


    class TipoPrimitivoContext(TipoContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LAParser.TipoContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)

        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoPrimitivo" ):
                listener.enterTipoPrimitivo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoPrimitivo" ):
                listener.exitTipoPrimitivo(self)



    def tipo(self):

        localctx = LAParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_tipo)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = LAParser.TipoPrimitivoContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 223
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 222
                    self.match(LAParser.CIRCUNFLEXO)


                self.state = 225
                self.tipo_base()
                pass

            elif la_ == 2:
                localctx = LAParser.TipoIdentificadoContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
                if la_ == 1:
                    self.state = 226
                    self.match(LAParser.CIRCUNFLEXO)


                self.state = 229
                self.tipo_identificado()
                pass

            elif la_ == 3:
                localctx = LAParser.TipoRegistroContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 230
                self.tipo_registro()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_identificadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def getRuleIndex(self):
            return LAParser.RULE_tipo_identificado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_identificado" ):
                listener.enterTipo_identificado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_identificado" ):
                listener.exitTipo_identificado(self)




    def tipo_identificado(self):

        localctx = LAParser.Tipo_identificadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tipo_identificado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 233
                self.match(LAParser.CIRCUNFLEXO)


            self.state = 236
            self.match(LAParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def getRuleIndex(self):
            return LAParser.RULE_tipo_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_base" ):
                listener.enterTipo_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_base" ):
                listener.exitTipo_base(self)




    def tipo_base(self):

        localctx = LAParser.Tipo_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tipo_base)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==66:
                self.state = 238
                self.match(LAParser.CIRCUNFLEXO)


            self.state = 241
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tipo_registroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lista_campos(self):
            return self.getTypedRuleContext(LAParser.Lista_camposContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_tipo_registro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo_registro" ):
                listener.enterTipo_registro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo_registro" ):
                listener.exitTipo_registro(self)




    def tipo_registro(self):

        localctx = LAParser.Tipo_registroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tipo_registro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(LAParser.T__16)
            self.state = 244
            self.lista_campos()
            self.state = 245
            self.match(LAParser.T__17)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_camposContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.CampoContext)
            else:
                return self.getTypedRuleContext(LAParser.CampoContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_lista_campos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_campos" ):
                listener.enterLista_campos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_campos" ):
                listener.exitLista_campos(self)




    def lista_campos(self):

        localctx = LAParser.Lista_camposContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lista_campos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.campo()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==68:
                self.state = 249
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==19:
                    self.state = 248
                    self.match(LAParser.T__18)


                self.state = 251
                self.campo()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CampoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.IDENT)
            else:
                return self.getToken(LAParser.IDENT, i)

        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        def tipo_base(self):
            return self.getTypedRuleContext(LAParser.Tipo_baseContext,0)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCampo" ):
                listener.enterCampo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCampo" ):
                listener.exitCampo(self)




    def campo(self):

        localctx = LAParser.CampoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_campo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(LAParser.IDENT)
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 258
                self.match(LAParser.VIRG)
                self.state = 259
                self.match(LAParser.IDENT)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 265
            self.match(LAParser.DOIS_PONTOS)
            self.state = 266
            self.tipo_base()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Acesso_campoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.IDENT)
            else:
                return self.getToken(LAParser.IDENT, i)

        def PONTO(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.PONTO)
            else:
                return self.getToken(LAParser.PONTO, i)

        def getRuleIndex(self):
            return LAParser.RULE_acesso_campo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcesso_campo" ):
                listener.enterAcesso_campo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcesso_campo" ):
                listener.exitAcesso_campo(self)




    def acesso_campo(self):

        localctx = LAParser.Acesso_campoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_acesso_campo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(LAParser.IDENT)
            self.state = 271 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.match(LAParser.PONTO)
                self.state = 270
                self.match(LAParser.IDENT)
                self.state = 273 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==63):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribuicao(self):
            return self.getTypedRuleContext(LAParser.AtribuicaoContext,0)


        def leitura(self):
            return self.getTypedRuleContext(LAParser.LeituraContext,0)


        def escrita(self):
            return self.getTypedRuleContext(LAParser.EscritaContext,0)


        def comandose(self):
            return self.getTypedRuleContext(LAParser.ComandoseContext,0)


        def comandocaso(self):
            return self.getTypedRuleContext(LAParser.ComandocasoContext,0)


        def comandopara(self):
            return self.getTypedRuleContext(LAParser.ComandoparaContext,0)


        def comandoenquanto(self):
            return self.getTypedRuleContext(LAParser.ComandoenquantoContext,0)


        def comandofaca(self):
            return self.getTypedRuleContext(LAParser.ComandofacaContext,0)


        def chamada_procedimento(self):
            return self.getTypedRuleContext(LAParser.Chamada_procedimentoContext,0)


        def retorne(self):
            return self.getTypedRuleContext(LAParser.RetorneContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = LAParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_comando)
        try:
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.atribuicao()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.leitura()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 277
                self.escrita()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 278
                self.comandose()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 279
                self.comandocaso()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 280
                self.comandopara()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 281
                self.comandoenquanto()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 282
                self.comandofaca()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 283
                self.chamada_procedimento()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 284
                self.retorne()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RetorneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_retorne

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetorne" ):
                listener.enterRetorne(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetorne" ):
                listener.exitRetorne(self)




    def retorne(self):

        localctx = LAParser.RetorneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_retorne)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(LAParser.T__19)
            self.state = 288
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chamada_procedimentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def lista_expressao(self):
            return self.getTypedRuleContext(LAParser.Lista_expressaoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_chamada_procedimento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamada_procedimento" ):
                listener.enterChamada_procedimento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamada_procedimento" ):
                listener.exitChamada_procedimento(self)




    def chamada_procedimento(self):

        localctx = LAParser.Chamada_procedimentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_chamada_procedimento)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(LAParser.IDENT)
            self.state = 291
            self.match(LAParser.ABREPAR)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & 3026712812865978371) != 0):
                self.state = 292
                self.lista_expressao()


            self.state = 295
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandofacaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_comandofaca

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandofaca" ):
                listener.enterComandofaca(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandofaca" ):
                listener.exitComandofaca(self)




    def comandofaca(self):

        localctx = LAParser.ComandofacaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comandofaca)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(LAParser.T__20)
            self.state = 298
            self.comandos()
            self.state = 299
            self.match(LAParser.T__21)
            self.state = 300
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoenquantoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_comandoenquanto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandoenquanto" ):
                listener.enterComandoenquanto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandoenquanto" ):
                listener.exitComandoenquanto(self)




    def comandoenquanto(self):

        localctx = LAParser.ComandoenquantoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_comandoenquanto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(LAParser.T__22)
            self.state = 303
            self.expressao()
            self.state = 304
            self.match(LAParser.T__20)
            self.state = 305
            self.comandos()
            self.state = 306
            self.match(LAParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoparaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def ATRIBUICAO(self):
            return self.getToken(LAParser.ATRIBUICAO, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAParser.ExpressaoContext,i)


        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_comandopara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandopara" ):
                listener.enterComandopara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandopara" ):
                listener.exitComandopara(self)




    def comandopara(self):

        localctx = LAParser.ComandoparaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_comandopara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(LAParser.T__24)
            self.state = 309
            self.match(LAParser.IDENT)
            self.state = 310
            self.match(LAParser.ATRIBUICAO)
            self.state = 311
            self.expressao()
            self.state = 312
            self.match(LAParser.T__21)
            self.state = 313
            self.expressao()
            self.state = 314
            self.match(LAParser.T__20)
            self.state = 315
            self.comandos()
            self.state = 316
            self.match(LAParser.T__25)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandocasoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def selecao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.SelecaoContext)
            else:
                return self.getTypedRuleContext(LAParser.SelecaoContext,i)


        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_comandocaso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandocaso" ):
                listener.enterComandocaso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandocaso" ):
                listener.exitComandocaso(self)




    def comandocaso(self):

        localctx = LAParser.ComandocasoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_comandocaso)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(LAParser.T__26)
            self.state = 319
            self.expressao()
            self.state = 320
            self.match(LAParser.T__27)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==47:
                self.state = 321
                self.selecao()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 327
                self.match(LAParser.T__28)
                self.state = 328
                self.comandos()


            self.state = 331
            self.match(LAParser.T__29)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelecaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constantes(self):
            return self.getTypedRuleContext(LAParser.ConstantesContext,0)


        def DOIS_PONTOS(self):
            return self.getToken(LAParser.DOIS_PONTOS, 0)

        def comandos(self):
            return self.getTypedRuleContext(LAParser.ComandosContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_selecao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelecao" ):
                listener.enterSelecao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelecao" ):
                listener.exitSelecao(self)




    def selecao(self):

        localctx = LAParser.SelecaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_selecao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.constantes()
            self.state = 334
            self.match(LAParser.DOIS_PONTOS)
            self.state = 335
            self.comandos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constante(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ConstanteContext)
            else:
                return self.getTypedRuleContext(LAParser.ConstanteContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_constantes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantes" ):
                listener.enterConstantes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantes" ):
                listener.exitConstantes(self)




    def constantes(self):

        localctx = LAParser.ConstantesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_constantes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.constante()
            self.state = 342
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 338
                self.match(LAParser.VIRG)
                self.state = 339
                self.constante()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstanteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.NUM_INT)
            else:
                return self.getToken(LAParser.NUM_INT, i)

        def PONTOS(self):
            return self.getToken(LAParser.PONTOS, 0)

        def getRuleIndex(self):
            return LAParser.RULE_constante

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstante" ):
                listener.enterConstante(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstante" ):
                listener.exitConstante(self)




    def constante(self):

        localctx = LAParser.ConstanteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_constante)
        try:
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(LAParser.NUM_INT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.match(LAParser.NUM_INT)
                self.state = 347
                self.match(LAParser.PONTOS)
                self.state = 348
                self.match(LAParser.NUM_INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def comandos(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ComandosContext)
            else:
                return self.getTypedRuleContext(LAParser.ComandosContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_comandose

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandose" ):
                listener.enterComandose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandose" ):
                listener.exitComandose(self)




    def comandose(self):

        localctx = LAParser.ComandoseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_comandose)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(LAParser.T__30)
            self.state = 352
            self.expressao()
            self.state = 353
            self.match(LAParser.T__31)
            self.state = 354
            self.comandos()
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 355
                self.match(LAParser.T__28)
                self.state = 356
                self.comandos()


            self.state = 359
            self.match(LAParser.T__32)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ComandoContext)
            else:
                return self.getTypedRuleContext(LAParser.ComandoContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_comandos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComandos" ):
                listener.enterComandos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComandos" ):
                listener.exitComandos(self)




    def comandos(self):

        localctx = LAParser.ComandosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_comandos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 20)) & ~0x3f) == 0 and ((1 << (_la - 20)) & 351843720939691) != 0):
                self.state = 361
                self.comando()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def lista_identificadores(self):
            return self.getTypedRuleContext(LAParser.Lista_identificadoresContext,0)


        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LAParser.RULE_leitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeitura" ):
                listener.enterLeitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeitura" ):
                listener.exitLeitura(self)




    def leitura(self):

        localctx = LAParser.LeituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_leitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(LAParser.T__33)
            self.state = 368
            self.match(LAParser.ABREPAR)
            self.state = 369
            self.lista_identificadores()
            self.state = 370
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_identificadoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.IDENT)
            else:
                return self.getToken(LAParser.IDENT, i)

        def acesso_campo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Acesso_campoContext)
            else:
                return self.getTypedRuleContext(LAParser.Acesso_campoContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_lista_identificadores

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_identificadores" ):
                listener.enterLista_identificadores(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_identificadores" ):
                listener.exitLista_identificadores(self)




    def lista_identificadores(self):

        localctx = LAParser.Lista_identificadoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_lista_identificadores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 372
                self.match(LAParser.IDENT)
                pass

            elif la_ == 2:
                self.state = 373
                self.acesso_campo()
                pass


            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 376
                self.match(LAParser.VIRG)
                self.state = 379
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 377
                    self.match(LAParser.IDENT)
                    pass

                elif la_ == 2:
                    self.state = 378
                    self.acesso_campo()
                    pass


                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATRIBUICAO(self):
            return self.getToken(LAParser.ATRIBUICAO, 0)

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def acesso_campo(self):
            return self.getTypedRuleContext(LAParser.Acesso_campoContext,0)


        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def getRuleIndex(self):
            return LAParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)




    def atribuicao(self):

        localctx = LAParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.state = 386
                self.match(LAParser.IDENT)
                pass

            elif la_ == 2:
                self.state = 387
                self.acesso_campo()
                pass

            elif la_ == 3:
                self.state = 388
                self.match(LAParser.CIRCUNFLEXO)
                self.state = 389
                self.match(LAParser.IDENT)
                pass


            self.state = 392
            self.match(LAParser.ATRIBUICAO)
            self.state = 393
            self.expressao()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAParser.ExpressaoContext,i)


        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_escrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscrita" ):
                listener.enterEscrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscrita" ):
                listener.exitEscrita(self)




    def escrita(self):

        localctx = LAParser.EscritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_escrita)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(LAParser.T__34)
            self.state = 396
            self.match(LAParser.ABREPAR)
            self.state = 397
            self.expressao()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 398
                self.match(LAParser.VIRG)
                self.state = 399
                self.expressao()
                self.state = 404
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 405
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubliteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def NUM_INT(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.NUM_INT)
            else:
                return self.getToken(LAParser.NUM_INT, i)

        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LAParser.RULE_subliteral

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubliteral" ):
                listener.enterSubliteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubliteral" ):
                listener.exitSubliteral(self)




    def subliteral(self):

        localctx = LAParser.SubliteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_subliteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 407
            self.match(LAParser.T__35)
            self.state = 408
            self.match(LAParser.ABREPAR)
            self.state = 409
            self.expressao()
            self.state = 410
            self.match(LAParser.VIRG)
            self.state = 411
            self.match(LAParser.NUM_INT)
            self.state = 412
            self.match(LAParser.VIRG)
            self.state = 413
            self.match(LAParser.NUM_INT)
            self.state = 414
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PotenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAParser.ExpressaoContext,i)


        def VIRG(self):
            return self.getToken(LAParser.VIRG, 0)

        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def getRuleIndex(self):
            return LAParser.RULE_potencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)




    def potencia(self):

        localctx = LAParser.PotenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_potencia)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(LAParser.T__36)
            self.state = 417
            self.match(LAParser.ABREPAR)
            self.state = 418
            self.expressao()
            self.state = 419
            self.match(LAParser.VIRG)
            self.state = 420
            self.expressao()
            self.state = 421
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_logica(self):
            return self.getTypedRuleContext(LAParser.Expressao_logicaContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)




    def expressao(self):

        localctx = LAParser.ExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expressao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.expressao_logica()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_logicaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Expressao_relacionalContext)
            else:
                return self.getTypedRuleContext(LAParser.Expressao_relacionalContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_expressao_logica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_logica" ):
                listener.enterExpressao_logica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_logica" ):
                listener.exitExpressao_logica(self)




    def expressao_logica(self):

        localctx = LAParser.Expressao_logicaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expressao_logica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.expressao_relacional()
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38 or _la==39:
                self.state = 430
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [38]:
                    self.state = 426
                    self.match(LAParser.T__37)
                    self.state = 427
                    self.expressao_relacional()
                    pass
                elif token in [39]:
                    self.state = 428
                    self.match(LAParser.T__38)
                    self.state = 429
                    self.expressao_relacional()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_relacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao_aritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.Expressao_aritmeticaContext)
            else:
                return self.getTypedRuleContext(LAParser.Expressao_aritmeticaContext,i)


        def OP_RELACIONAL(self):
            return self.getToken(LAParser.OP_RELACIONAL, 0)

        def IGUAL(self):
            return self.getToken(LAParser.IGUAL, 0)

        def getRuleIndex(self):
            return LAParser.RULE_expressao_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_relacional" ):
                listener.enterExpressao_relacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_relacional" ):
                listener.exitExpressao_relacional(self)




    def expressao_relacional(self):

        localctx = LAParser.Expressao_relacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expressao_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.expressao_aritmetica()
            self.state = 438
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==60 or _la==61:
                self.state = 436
                _la = self._input.LA(1)
                if not(_la==60 or _la==61):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.expressao_aritmetica()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expressao_aritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.TermoContext)
            else:
                return self.getTypedRuleContext(LAParser.TermoContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_expressao_aritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao_aritmetica" ):
                listener.enterExpressao_aritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao_aritmetica" ):
                listener.exitExpressao_aritmetica(self)




    def expressao_aritmetica(self):

        localctx = LAParser.Expressao_aritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expressao_aritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.termo()
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40 or _la==41:
                self.state = 441
                _la = self._input.LA(1)
                if not(_la==40 or _la==41):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 442
                self.termo()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.FatorContext)
            else:
                return self.getTypedRuleContext(LAParser.FatorContext,i)


        def getRuleIndex(self):
            return LAParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = LAParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_termo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.fator()
            self.state = 453
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0):
                self.state = 449
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30786325577728) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.fator()
                self.state = 455
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(LAParser.FatorContext,0)


        def E_COMERCIAL(self):
            return self.getToken(LAParser.E_COMERCIAL, 0)

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def acesso_campo(self):
            return self.getTypedRuleContext(LAParser.Acesso_campoContext,0)


        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def expressao(self):
            return self.getTypedRuleContext(LAParser.ExpressaoContext,0)


        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def CIRCUNFLEXO(self):
            return self.getToken(LAParser.CIRCUNFLEXO, 0)

        def chamada_funcao(self):
            return self.getTypedRuleContext(LAParser.Chamada_funcaoContext,0)


        def potencia(self):
            return self.getTypedRuleContext(LAParser.PotenciaContext,0)


        def NUM_INT(self):
            return self.getToken(LAParser.NUM_INT, 0)

        def NUM_REAL(self):
            return self.getToken(LAParser.NUM_REAL, 0)

        def CADEIA(self):
            return self.getToken(LAParser.CADEIA, 0)

        def subliteral(self):
            return self.getTypedRuleContext(LAParser.SubliteralContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = LAParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_fator)
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.match(LAParser.T__40)
                self.state = 457
                self.fator()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 458
                self.match(LAParser.T__44)
                self.state = 459
                self.fator()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 460
                self.match(LAParser.E_COMERCIAL)
                self.state = 463
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 461
                    self.match(LAParser.IDENT)
                    pass

                elif la_ == 2:
                    self.state = 462
                    self.acesso_campo()
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 465
                self.match(LAParser.ABREPAR)
                self.state = 466
                self.expressao()
                self.state = 467
                self.match(LAParser.FECHAPAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.match(LAParser.CIRCUNFLEXO)
                self.state = 470
                self.match(LAParser.IDENT)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.chamada_funcao()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 472
                self.potencia()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 473
                self.acesso_campo()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 474
                self.match(LAParser.IDENT)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 475
                self.match(LAParser.NUM_INT)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 476
                self.match(LAParser.NUM_REAL)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 477
                self.match(LAParser.CADEIA)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 478
                self.subliteral()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 479
                self.match(LAParser.T__6)
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 480
                self.match(LAParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Chamada_funcaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(LAParser.IDENT, 0)

        def ABREPAR(self):
            return self.getToken(LAParser.ABREPAR, 0)

        def FECHAPAR(self):
            return self.getToken(LAParser.FECHAPAR, 0)

        def lista_expressao(self):
            return self.getTypedRuleContext(LAParser.Lista_expressaoContext,0)


        def getRuleIndex(self):
            return LAParser.RULE_chamada_funcao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamada_funcao" ):
                listener.enterChamada_funcao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamada_funcao" ):
                listener.exitChamada_funcao(self)




    def chamada_funcao(self):

        localctx = LAParser.Chamada_funcaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_chamada_funcao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(LAParser.IDENT)
            self.state = 484
            self.match(LAParser.ABREPAR)
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 7)) & ~0x3f) == 0 and ((1 << (_la - 7)) & 3026712812865978371) != 0):
                self.state = 485
                self.lista_expressao()


            self.state = 488
            self.match(LAParser.FECHAPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lista_expressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LAParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(LAParser.ExpressaoContext,i)


        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(LAParser.VIRG)
            else:
                return self.getToken(LAParser.VIRG, i)

        def getRuleIndex(self):
            return LAParser.RULE_lista_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista_expressao" ):
                listener.enterLista_expressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista_expressao" ):
                listener.exitLista_expressao(self)




    def lista_expressao(self):

        localctx = LAParser.Lista_expressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_lista_expressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.expressao()
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==57:
                self.state = 491
                self.match(LAParser.VIRG)
                self.state = 492
                self.expressao()
                self.state = 497
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





