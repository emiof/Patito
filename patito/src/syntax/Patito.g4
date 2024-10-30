grammar Patito;

// Lexicon
// Reserved tokens
PROGRAMA: 'programa';
INICIO: 'inicio';
ENTERO: 'entero';
FLOTANTE: 'flotante';
VAR: 'var';
ESCRIBE: 'escribe';
MIENTRAS: 'mientras';
HAZ: 'haz';
SINO: 'sino';
FIN: 'fin';
NULA: 'nula';
SI: 'si';

// Operator tokens 
MAYOR_A: '>';
MENOR_A: '<';
INIGUALDAD: '!=';
IGUALDAD: '==';
SUMA: '+';
RESTA: '-';
MULTIPLICACION: '*';
DIVISION: '/';
ASIGNACION: '=';

// Separating and grouping tokens
PUNTO_COMA: ';';
PARENTESIS_APER: '(';
PARENTESIS_CLAU: ')';
DOS_PUNTOS: ':';
COMA: ',';
CORCHETE_APER: '{';
CORCHETE_CLAU: '}';

// Complex tokens
ID: [A-Za-z]+[_A-Za-z0-9]*;
LETRERO: '\''[a-zA-Z0-9_",;.: ]*'\'' | '"'[a-zA-Z0-9_',;.: ]*'"';
CTE_ENT: [0-9]+;
CTE_FLOT: [0-9]+'.'[0-9]+;

// Whitespaces 
WS: [ \t\r\n]+ -> skip;

// Grammar
// programa  
programa: PROGRAMA ID PUNTO_COMA opc_var opc_lista_func INICIO cuerpo FIN;

// var
var: VAR lista_id DOS_PUNTOS tipo PUNTO_COMA extension_var;
opc_var: var | ;
extension_var: lista_id DOS_PUNTOS tipo PUNTO_COMA extension_var | ;

// cuerpo 
cuerpo: CORCHETE_APER opc_lista_estatuto CORCHETE_CLAU;

// estatuto 
estatuto: asigna | condicion | ciclo | llamada | imprime;
opc_lista_estatuto: estatuto opc_lista_estatuto | ;

// imprime 
imprime: ESCRIBE PARENTESIS_APER lista_expresion_o_letrero PARENTESIS_CLAU PUNTO_COMA;
expresion_o_letrero: expresion | LETRERO;
lista_expresion_o_letrero: expresion_o_letrero lista_expresion_o_letrero_1;
lista_expresion_o_letrero_1: COMA expresion_o_letrero lista_expresion_o_letrero_1 | ;

// asigna 
asigna: ID ASIGNACION expresion PUNTO_COMA;

// ciclo 
ciclo: MIENTRAS PARENTESIS_APER expresion PARENTESIS_CLAU HAZ cuerpo PUNTO_COMA;

// expresion
expresion: exp opc_operador_relacional_expresion;
opc_operador_relacional_expresion: operador_relacional exp | ;
lista_expresion: expresion lista_expresion_1;
lista_expresion_1: COMA expresion lista_expresion_1 | ;
opc_lista_expresion: lista_expresion | ;

// exp
exp: lista_termino;

// termino
termino: lista_factor;
lista_termino: termino lista_termino_1;
lista_termino_1: suma_o_resta termino lista_termino_1 | ;

// factor
factor: PARENTESIS_APER expresion PARENTESIS_CLAU | opc_suma_o_resta id_o_cte;
lista_factor: factor lista_factor_1;
lista_factor_1: multiplicacion_o_division factor lista_factor_1 | ;

// tipo 
tipo: ENTERO | FLOTANTE;

// id 
lista_id: ID lista_id_1;
lista_id_1: COMA ID lista_id_1 | ;
id_tipo: ID DOS_PUNTOS tipo;
lista_id_tipo: id_tipo lista_id_tipo_1;
lista_id_tipo_1: COMA id_tipo lista_id_tipo_1 | ;
opc_lista_id_tipo: lista_id_tipo | ;

// func 
func: NULA ID PARENTESIS_APER opc_lista_id_tipo PARENTESIS_CLAU CORCHETE_APER opc_var cuerpo CORCHETE_CLAU PUNTO_COMA;
opc_lista_func: func opc_lista_func | ;

// llamada 
llamada: ID PARENTESIS_APER opc_lista_expresion PARENTESIS_CLAU PUNTO_COMA;

// cte 
cte: CTE_ENT | CTE_FLOT;

// condicion
condicion: SI PARENTESIS_APER expresion PARENTESIS_CLAU cuerpo opc_sino PUNTO_COMA;

// MISC
opc_sino: SINO cuerpo | ;
operador_relacional: MAYOR_A | MENOR_A | INIGUALDAD | IGUALDAD;
suma_o_resta: SUMA | RESTA;
opc_suma_o_resta: suma_o_resta | ;
multiplicacion_o_division: MULTIPLICACION | DIVISION;
id_o_cte: ID | cte;