// Generated from /Users/emilio/Desktop/Tec/Semestres/Octavo Semestre/Bloques/(Aplicaciones Avanzadas) Desarrollo de Aplicaciones Avanzadas de Ciencias Computacionales/M3 - Compiladores/Compilador/Patito/patito/src/syntax/Patito.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PatitoParser}.
 */
public interface PatitoListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PatitoParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(PatitoParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(PatitoParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(PatitoParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(PatitoParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_var}.
	 * @param ctx the parse tree
	 */
	void enterOpc_var(PatitoParser.Opc_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_var}.
	 * @param ctx the parse tree
	 */
	void exitOpc_var(PatitoParser.Opc_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#extension_var}.
	 * @param ctx the parse tree
	 */
	void enterExtension_var(PatitoParser.Extension_varContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#extension_var}.
	 * @param ctx the parse tree
	 */
	void exitExtension_var(PatitoParser.Extension_varContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void enterCuerpo(PatitoParser.CuerpoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#cuerpo}.
	 * @param ctx the parse tree
	 */
	void exitCuerpo(PatitoParser.CuerpoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void enterEstatuto(PatitoParser.EstatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#estatuto}.
	 * @param ctx the parse tree
	 */
	void exitEstatuto(PatitoParser.EstatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_lista_estatuto}.
	 * @param ctx the parse tree
	 */
	void enterOpc_lista_estatuto(PatitoParser.Opc_lista_estatutoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_lista_estatuto}.
	 * @param ctx the parse tree
	 */
	void exitOpc_lista_estatuto(PatitoParser.Opc_lista_estatutoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#imprime}.
	 * @param ctx the parse tree
	 */
	void enterImprime(PatitoParser.ImprimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#imprime}.
	 * @param ctx the parse tree
	 */
	void exitImprime(PatitoParser.ImprimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#expresion_o_letrero}.
	 * @param ctx the parse tree
	 */
	void enterExpresion_o_letrero(PatitoParser.Expresion_o_letreroContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#expresion_o_letrero}.
	 * @param ctx the parse tree
	 */
	void exitExpresion_o_letrero(PatitoParser.Expresion_o_letreroContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_expresion_o_letrero}.
	 * @param ctx the parse tree
	 */
	void enterLista_expresion_o_letrero(PatitoParser.Lista_expresion_o_letreroContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_expresion_o_letrero}.
	 * @param ctx the parse tree
	 */
	void exitLista_expresion_o_letrero(PatitoParser.Lista_expresion_o_letreroContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_expresion_o_letrero_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_expresion_o_letrero_1(PatitoParser.Lista_expresion_o_letrero_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_expresion_o_letrero_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_expresion_o_letrero_1(PatitoParser.Lista_expresion_o_letrero_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#asigna}.
	 * @param ctx the parse tree
	 */
	void enterAsigna(PatitoParser.AsignaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#asigna}.
	 * @param ctx the parse tree
	 */
	void exitAsigna(PatitoParser.AsignaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void enterCiclo(PatitoParser.CicloContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#ciclo}.
	 * @param ctx the parse tree
	 */
	void exitCiclo(PatitoParser.CicloContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#expresion}.
	 * @param ctx the parse tree
	 */
	void enterExpresion(PatitoParser.ExpresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#expresion}.
	 * @param ctx the parse tree
	 */
	void exitExpresion(PatitoParser.ExpresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_operador_relacional_expresion}.
	 * @param ctx the parse tree
	 */
	void enterOpc_operador_relacional_expresion(PatitoParser.Opc_operador_relacional_expresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_operador_relacional_expresion}.
	 * @param ctx the parse tree
	 */
	void exitOpc_operador_relacional_expresion(PatitoParser.Opc_operador_relacional_expresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_expresion}.
	 * @param ctx the parse tree
	 */
	void enterLista_expresion(PatitoParser.Lista_expresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_expresion}.
	 * @param ctx the parse tree
	 */
	void exitLista_expresion(PatitoParser.Lista_expresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_expresion_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_expresion_1(PatitoParser.Lista_expresion_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_expresion_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_expresion_1(PatitoParser.Lista_expresion_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_lista_expresion}.
	 * @param ctx the parse tree
	 */
	void enterOpc_lista_expresion(PatitoParser.Opc_lista_expresionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_lista_expresion}.
	 * @param ctx the parse tree
	 */
	void exitOpc_lista_expresion(PatitoParser.Opc_lista_expresionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#exp}.
	 * @param ctx the parse tree
	 */
	void enterExp(PatitoParser.ExpContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#exp}.
	 * @param ctx the parse tree
	 */
	void exitExp(PatitoParser.ExpContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#termino}.
	 * @param ctx the parse tree
	 */
	void enterTermino(PatitoParser.TerminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#termino}.
	 * @param ctx the parse tree
	 */
	void exitTermino(PatitoParser.TerminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_termino}.
	 * @param ctx the parse tree
	 */
	void enterLista_termino(PatitoParser.Lista_terminoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_termino}.
	 * @param ctx the parse tree
	 */
	void exitLista_termino(PatitoParser.Lista_terminoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_termino_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_termino_1(PatitoParser.Lista_termino_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_termino_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_termino_1(PatitoParser.Lista_termino_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#factor}.
	 * @param ctx the parse tree
	 */
	void enterFactor(PatitoParser.FactorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#factor}.
	 * @param ctx the parse tree
	 */
	void exitFactor(PatitoParser.FactorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_factor}.
	 * @param ctx the parse tree
	 */
	void enterLista_factor(PatitoParser.Lista_factorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_factor}.
	 * @param ctx the parse tree
	 */
	void exitLista_factor(PatitoParser.Lista_factorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_factor_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_factor_1(PatitoParser.Lista_factor_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_factor_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_factor_1(PatitoParser.Lista_factor_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void enterTipo(PatitoParser.TipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#tipo}.
	 * @param ctx the parse tree
	 */
	void exitTipo(PatitoParser.TipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_id}.
	 * @param ctx the parse tree
	 */
	void enterLista_id(PatitoParser.Lista_idContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_id}.
	 * @param ctx the parse tree
	 */
	void exitLista_id(PatitoParser.Lista_idContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_id_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_id_1(PatitoParser.Lista_id_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_id_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_id_1(PatitoParser.Lista_id_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#id_tipo}.
	 * @param ctx the parse tree
	 */
	void enterId_tipo(PatitoParser.Id_tipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#id_tipo}.
	 * @param ctx the parse tree
	 */
	void exitId_tipo(PatitoParser.Id_tipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_id_tipo}.
	 * @param ctx the parse tree
	 */
	void enterLista_id_tipo(PatitoParser.Lista_id_tipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_id_tipo}.
	 * @param ctx the parse tree
	 */
	void exitLista_id_tipo(PatitoParser.Lista_id_tipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#lista_id_tipo_1}.
	 * @param ctx the parse tree
	 */
	void enterLista_id_tipo_1(PatitoParser.Lista_id_tipo_1Context ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#lista_id_tipo_1}.
	 * @param ctx the parse tree
	 */
	void exitLista_id_tipo_1(PatitoParser.Lista_id_tipo_1Context ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_lista_id_tipo}.
	 * @param ctx the parse tree
	 */
	void enterOpc_lista_id_tipo(PatitoParser.Opc_lista_id_tipoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_lista_id_tipo}.
	 * @param ctx the parse tree
	 */
	void exitOpc_lista_id_tipo(PatitoParser.Opc_lista_id_tipoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#func}.
	 * @param ctx the parse tree
	 */
	void enterFunc(PatitoParser.FuncContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#func}.
	 * @param ctx the parse tree
	 */
	void exitFunc(PatitoParser.FuncContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_lista_func}.
	 * @param ctx the parse tree
	 */
	void enterOpc_lista_func(PatitoParser.Opc_lista_funcContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_lista_func}.
	 * @param ctx the parse tree
	 */
	void exitOpc_lista_func(PatitoParser.Opc_lista_funcContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#llamada}.
	 * @param ctx the parse tree
	 */
	void enterLlamada(PatitoParser.LlamadaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#llamada}.
	 * @param ctx the parse tree
	 */
	void exitLlamada(PatitoParser.LlamadaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#cte}.
	 * @param ctx the parse tree
	 */
	void enterCte(PatitoParser.CteContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#cte}.
	 * @param ctx the parse tree
	 */
	void exitCte(PatitoParser.CteContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(PatitoParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(PatitoParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_sino}.
	 * @param ctx the parse tree
	 */
	void enterOpc_sino(PatitoParser.Opc_sinoContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_sino}.
	 * @param ctx the parse tree
	 */
	void exitOpc_sino(PatitoParser.Opc_sinoContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#operador_relacional}.
	 * @param ctx the parse tree
	 */
	void enterOperador_relacional(PatitoParser.Operador_relacionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#operador_relacional}.
	 * @param ctx the parse tree
	 */
	void exitOperador_relacional(PatitoParser.Operador_relacionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#suma_o_resta}.
	 * @param ctx the parse tree
	 */
	void enterSuma_o_resta(PatitoParser.Suma_o_restaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#suma_o_resta}.
	 * @param ctx the parse tree
	 */
	void exitSuma_o_resta(PatitoParser.Suma_o_restaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#opc_suma_o_resta}.
	 * @param ctx the parse tree
	 */
	void enterOpc_suma_o_resta(PatitoParser.Opc_suma_o_restaContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#opc_suma_o_resta}.
	 * @param ctx the parse tree
	 */
	void exitOpc_suma_o_resta(PatitoParser.Opc_suma_o_restaContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#multiplicacion_o_division}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicacion_o_division(PatitoParser.Multiplicacion_o_divisionContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#multiplicacion_o_division}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicacion_o_division(PatitoParser.Multiplicacion_o_divisionContext ctx);
	/**
	 * Enter a parse tree produced by {@link PatitoParser#id_o_cte}.
	 * @param ctx the parse tree
	 */
	void enterId_o_cte(PatitoParser.Id_o_cteContext ctx);
	/**
	 * Exit a parse tree produced by {@link PatitoParser#id_o_cte}.
	 * @param ctx the parse tree
	 */
	void exitId_o_cte(PatitoParser.Id_o_cteContext ctx);
}