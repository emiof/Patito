// Generated from /Users/emilio/Desktop/Tec/Semestres/Octavo Semestre/Bloques/(Aplicaciones Avanzadas) Desarrollo de Aplicaciones Avanzadas de Ciencias Computacionales/M3 - Compiladores/Compilador/Patito/patito/src/syntax/Patito.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PatitoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROGRAMA=1, INICIO=2, ENTERO=3, FLOTANTE=4, VAR=5, ESCRIBE=6, MIENTRAS=7, 
		HAZ=8, SINO=9, FIN=10, NULA=11, SI=12, MAYOR_A=13, MENOR_A=14, INIGUALDAD=15, 
		IGUALDAD=16, SUMA=17, RESTA=18, MULTIPLICACION=19, DIVISION=20, ASIGNACION=21, 
		PUNTO_COMA=22, PARENTESIS_APER=23, PARENTESIS_CLAU=24, DOS_PUNTOS=25, 
		COMA=26, CORCHETE_APER=27, CORCHETE_CLAU=28, ID=29, LETRERO=30, CTE_ENT=31, 
		CTE_FLOT=32, WS=33;
	public static final int
		RULE_programa = 0, RULE_var = 1, RULE_opc_var = 2, RULE_extension_var = 3, 
		RULE_cuerpo = 4, RULE_estatuto = 5, RULE_opc_lista_estatuto = 6, RULE_imprime = 7, 
		RULE_expresion_o_letrero = 8, RULE_lista_expresion_o_letrero = 9, RULE_lista_expresion_o_letrero_1 = 10, 
		RULE_asigna = 11, RULE_ciclo = 12, RULE_expresion = 13, RULE_opc_operador_relacional_expresion = 14, 
		RULE_lista_expresion = 15, RULE_lista_expresion_1 = 16, RULE_opc_lista_expresion = 17, 
		RULE_exp = 18, RULE_termino = 19, RULE_lista_termino = 20, RULE_lista_termino_1 = 21, 
		RULE_factor = 22, RULE_lista_factor = 23, RULE_lista_factor_1 = 24, RULE_tipo = 25, 
		RULE_lista_id = 26, RULE_lista_id_1 = 27, RULE_id_tipo = 28, RULE_lista_id_tipo = 29, 
		RULE_lista_id_tipo_1 = 30, RULE_opc_lista_id_tipo = 31, RULE_func = 32, 
		RULE_opc_lista_func = 33, RULE_llamada = 34, RULE_cte = 35, RULE_condicion = 36, 
		RULE_opc_sino = 37, RULE_operador_relacional = 38, RULE_suma_o_resta = 39, 
		RULE_opc_suma_o_resta = 40, RULE_multiplicacion_o_division = 41, RULE_id_o_cte = 42;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "var", "opc_var", "extension_var", "cuerpo", "estatuto", 
			"opc_lista_estatuto", "imprime", "expresion_o_letrero", "lista_expresion_o_letrero", 
			"lista_expresion_o_letrero_1", "asigna", "ciclo", "expresion", "opc_operador_relacional_expresion", 
			"lista_expresion", "lista_expresion_1", "opc_lista_expresion", "exp", 
			"termino", "lista_termino", "lista_termino_1", "factor", "lista_factor", 
			"lista_factor_1", "tipo", "lista_id", "lista_id_1", "id_tipo", "lista_id_tipo", 
			"lista_id_tipo_1", "opc_lista_id_tipo", "func", "opc_lista_func", "llamada", 
			"cte", "condicion", "opc_sino", "operador_relacional", "suma_o_resta", 
			"opc_suma_o_resta", "multiplicacion_o_division", "id_o_cte"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'programa'", "'inicio'", "'entero'", "'flotante'", "'var'", "'escribe'", 
			"'mientras'", "'haz'", "'sino'", "'fin'", "'nula'", "'si'", "'>'", "'<'", 
			"'!='", "'=='", "'+'", "'-'", "'*'", "'/'", "'='", "';'", "'('", "')'", 
			"':'", "','", "'{'", "'}'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROGRAMA", "INICIO", "ENTERO", "FLOTANTE", "VAR", "ESCRIBE", "MIENTRAS", 
			"HAZ", "SINO", "FIN", "NULA", "SI", "MAYOR_A", "MENOR_A", "INIGUALDAD", 
			"IGUALDAD", "SUMA", "RESTA", "MULTIPLICACION", "DIVISION", "ASIGNACION", 
			"PUNTO_COMA", "PARENTESIS_APER", "PARENTESIS_CLAU", "DOS_PUNTOS", "COMA", 
			"CORCHETE_APER", "CORCHETE_CLAU", "ID", "LETRERO", "CTE_ENT", "CTE_FLOT", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Patito.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PatitoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode PROGRAMA() { return getToken(PatitoParser.PROGRAMA, 0); }
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public Opc_varContext opc_var() {
			return getRuleContext(Opc_varContext.class,0);
		}
		public Opc_lista_funcContext opc_lista_func() {
			return getRuleContext(Opc_lista_funcContext.class,0);
		}
		public TerminalNode INICIO() { return getToken(PatitoParser.INICIO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode FIN() { return getToken(PatitoParser.FIN, 0); }
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(PROGRAMA);
			setState(87);
			match(ID);
			setState(88);
			match(PUNTO_COMA);
			setState(89);
			opc_var();
			setState(90);
			opc_lista_func();
			setState(91);
			match(INICIO);
			setState(92);
			cuerpo();
			setState(93);
			match(FIN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ParserRuleContext {
		public TerminalNode VAR() { return getToken(PatitoParser.VAR, 0); }
		public Lista_idContext lista_id() {
			return getRuleContext(Lista_idContext.class,0);
		}
		public TerminalNode DOS_PUNTOS() { return getToken(PatitoParser.DOS_PUNTOS, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public Extension_varContext extension_var() {
			return getRuleContext(Extension_varContext.class,0);
		}
		public VarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_var; }
	}

	public final VarContext var() throws RecognitionException {
		VarContext _localctx = new VarContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_var);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(95);
			match(VAR);
			setState(96);
			lista_id();
			setState(97);
			match(DOS_PUNTOS);
			setState(98);
			tipo();
			setState(99);
			match(PUNTO_COMA);
			setState(100);
			extension_var();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_varContext extends ParserRuleContext {
		public VarContext var() {
			return getRuleContext(VarContext.class,0);
		}
		public Opc_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_var; }
	}

	public final Opc_varContext opc_var() throws RecognitionException {
		Opc_varContext _localctx = new Opc_varContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_opc_var);
		try {
			setState(104);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case VAR:
				enterOuterAlt(_localctx, 1);
				{
				setState(102);
				var();
				}
				break;
			case INICIO:
			case NULA:
			case CORCHETE_APER:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Extension_varContext extends ParserRuleContext {
		public Lista_idContext lista_id() {
			return getRuleContext(Lista_idContext.class,0);
		}
		public TerminalNode DOS_PUNTOS() { return getToken(PatitoParser.DOS_PUNTOS, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public Extension_varContext extension_var() {
			return getRuleContext(Extension_varContext.class,0);
		}
		public Extension_varContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extension_var; }
	}

	public final Extension_varContext extension_var() throws RecognitionException {
		Extension_varContext _localctx = new Extension_varContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_extension_var);
		try {
			setState(113);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				lista_id();
				setState(107);
				match(DOS_PUNTOS);
				setState(108);
				tipo();
				setState(109);
				match(PUNTO_COMA);
				setState(110);
				extension_var();
				}
				break;
			case INICIO:
			case NULA:
			case CORCHETE_APER:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CuerpoContext extends ParserRuleContext {
		public TerminalNode CORCHETE_APER() { return getToken(PatitoParser.CORCHETE_APER, 0); }
		public Opc_lista_estatutoContext opc_lista_estatuto() {
			return getRuleContext(Opc_lista_estatutoContext.class,0);
		}
		public TerminalNode CORCHETE_CLAU() { return getToken(PatitoParser.CORCHETE_CLAU, 0); }
		public CuerpoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cuerpo; }
	}

	public final CuerpoContext cuerpo() throws RecognitionException {
		CuerpoContext _localctx = new CuerpoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_cuerpo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			match(CORCHETE_APER);
			setState(116);
			opc_lista_estatuto();
			setState(117);
			match(CORCHETE_CLAU);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EstatutoContext extends ParserRuleContext {
		public AsignaContext asigna() {
			return getRuleContext(AsignaContext.class,0);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public CicloContext ciclo() {
			return getRuleContext(CicloContext.class,0);
		}
		public LlamadaContext llamada() {
			return getRuleContext(LlamadaContext.class,0);
		}
		public ImprimeContext imprime() {
			return getRuleContext(ImprimeContext.class,0);
		}
		public EstatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_estatuto; }
	}

	public final EstatutoContext estatuto() throws RecognitionException {
		EstatutoContext _localctx = new EstatutoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_estatuto);
		try {
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(119);
				asigna();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(120);
				condicion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(121);
				ciclo();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(122);
				llamada();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(123);
				imprime();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_lista_estatutoContext extends ParserRuleContext {
		public EstatutoContext estatuto() {
			return getRuleContext(EstatutoContext.class,0);
		}
		public Opc_lista_estatutoContext opc_lista_estatuto() {
			return getRuleContext(Opc_lista_estatutoContext.class,0);
		}
		public Opc_lista_estatutoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_lista_estatuto; }
	}

	public final Opc_lista_estatutoContext opc_lista_estatuto() throws RecognitionException {
		Opc_lista_estatutoContext _localctx = new Opc_lista_estatutoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_opc_lista_estatuto);
		try {
			setState(130);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ESCRIBE:
			case MIENTRAS:
			case SI:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				estatuto();
				setState(127);
				opc_lista_estatuto();
				}
				break;
			case CORCHETE_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ImprimeContext extends ParserRuleContext {
		public TerminalNode ESCRIBE() { return getToken(PatitoParser.ESCRIBE, 0); }
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public Lista_expresion_o_letreroContext lista_expresion_o_letrero() {
			return getRuleContext(Lista_expresion_o_letreroContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public ImprimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_imprime; }
	}

	public final ImprimeContext imprime() throws RecognitionException {
		ImprimeContext _localctx = new ImprimeContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_imprime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(ESCRIBE);
			setState(133);
			match(PARENTESIS_APER);
			setState(134);
			lista_expresion_o_letrero();
			setState(135);
			match(PARENTESIS_CLAU);
			setState(136);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expresion_o_letreroContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode LETRERO() { return getToken(PatitoParser.LETRERO, 0); }
		public Expresion_o_letreroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion_o_letrero; }
	}

	public final Expresion_o_letreroContext expresion_o_letrero() throws RecognitionException {
		Expresion_o_letreroContext _localctx = new Expresion_o_letreroContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_expresion_o_letrero);
		try {
			setState(140);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
			case RESTA:
			case PARENTESIS_APER:
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(138);
				expresion();
				}
				break;
			case LETRERO:
				enterOuterAlt(_localctx, 2);
				{
				setState(139);
				match(LETRERO);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_expresion_o_letreroContext extends ParserRuleContext {
		public Expresion_o_letreroContext expresion_o_letrero() {
			return getRuleContext(Expresion_o_letreroContext.class,0);
		}
		public Lista_expresion_o_letrero_1Context lista_expresion_o_letrero_1() {
			return getRuleContext(Lista_expresion_o_letrero_1Context.class,0);
		}
		public Lista_expresion_o_letreroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_expresion_o_letrero; }
	}

	public final Lista_expresion_o_letreroContext lista_expresion_o_letrero() throws RecognitionException {
		Lista_expresion_o_letreroContext _localctx = new Lista_expresion_o_letreroContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_lista_expresion_o_letrero);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			expresion_o_letrero();
			setState(143);
			lista_expresion_o_letrero_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_expresion_o_letrero_1Context extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(PatitoParser.COMA, 0); }
		public Expresion_o_letreroContext expresion_o_letrero() {
			return getRuleContext(Expresion_o_letreroContext.class,0);
		}
		public Lista_expresion_o_letrero_1Context lista_expresion_o_letrero_1() {
			return getRuleContext(Lista_expresion_o_letrero_1Context.class,0);
		}
		public Lista_expresion_o_letrero_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_expresion_o_letrero_1; }
	}

	public final Lista_expresion_o_letrero_1Context lista_expresion_o_letrero_1() throws RecognitionException {
		Lista_expresion_o_letrero_1Context _localctx = new Lista_expresion_o_letrero_1Context(_ctx, getState());
		enterRule(_localctx, 20, RULE_lista_expresion_o_letrero_1);
		try {
			setState(150);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(145);
				match(COMA);
				setState(146);
				expresion_o_letrero();
				setState(147);
				lista_expresion_o_letrero_1();
				}
				break;
			case PARENTESIS_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public TerminalNode ASIGNACION() { return getToken(PatitoParser.ASIGNACION, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public AsignaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asigna; }
	}

	public final AsignaContext asigna() throws RecognitionException {
		AsignaContext _localctx = new AsignaContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_asigna);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(ID);
			setState(153);
			match(ASIGNACION);
			setState(154);
			expresion();
			setState(155);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CicloContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(PatitoParser.MIENTRAS, 0); }
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public TerminalNode HAZ() { return getToken(PatitoParser.HAZ, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public CicloContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ciclo; }
	}

	public final CicloContext ciclo() throws RecognitionException {
		CicloContext _localctx = new CicloContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_ciclo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(157);
			match(MIENTRAS);
			setState(158);
			match(PARENTESIS_APER);
			setState(159);
			expresion();
			setState(160);
			match(PARENTESIS_CLAU);
			setState(161);
			match(HAZ);
			setState(162);
			cuerpo();
			setState(163);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Opc_operador_relacional_expresionContext opc_operador_relacional_expresion() {
			return getRuleContext(Opc_operador_relacional_expresionContext.class,0);
		}
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		ExpresionContext _localctx = new ExpresionContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(165);
			exp();
			setState(166);
			opc_operador_relacional_expresion();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_operador_relacional_expresionContext extends ParserRuleContext {
		public Operador_relacionalContext operador_relacional() {
			return getRuleContext(Operador_relacionalContext.class,0);
		}
		public ExpContext exp() {
			return getRuleContext(ExpContext.class,0);
		}
		public Opc_operador_relacional_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_operador_relacional_expresion; }
	}

	public final Opc_operador_relacional_expresionContext opc_operador_relacional_expresion() throws RecognitionException {
		Opc_operador_relacional_expresionContext _localctx = new Opc_operador_relacional_expresionContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_opc_operador_relacional_expresion);
		try {
			setState(172);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MAYOR_A:
			case MENOR_A:
			case INIGUALDAD:
			case IGUALDAD:
				enterOuterAlt(_localctx, 1);
				{
				setState(168);
				operador_relacional();
				setState(169);
				exp();
				}
				break;
			case PUNTO_COMA:
			case PARENTESIS_CLAU:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_expresionContext extends ParserRuleContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Lista_expresion_1Context lista_expresion_1() {
			return getRuleContext(Lista_expresion_1Context.class,0);
		}
		public Lista_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_expresion; }
	}

	public final Lista_expresionContext lista_expresion() throws RecognitionException {
		Lista_expresionContext _localctx = new Lista_expresionContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_lista_expresion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(174);
			expresion();
			setState(175);
			lista_expresion_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_expresion_1Context extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(PatitoParser.COMA, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public Lista_expresion_1Context lista_expresion_1() {
			return getRuleContext(Lista_expresion_1Context.class,0);
		}
		public Lista_expresion_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_expresion_1; }
	}

	public final Lista_expresion_1Context lista_expresion_1() throws RecognitionException {
		Lista_expresion_1Context _localctx = new Lista_expresion_1Context(_ctx, getState());
		enterRule(_localctx, 32, RULE_lista_expresion_1);
		try {
			setState(182);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(177);
				match(COMA);
				setState(178);
				expresion();
				setState(179);
				lista_expresion_1();
				}
				break;
			case PARENTESIS_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_lista_expresionContext extends ParserRuleContext {
		public Lista_expresionContext lista_expresion() {
			return getRuleContext(Lista_expresionContext.class,0);
		}
		public Opc_lista_expresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_lista_expresion; }
	}

	public final Opc_lista_expresionContext opc_lista_expresion() throws RecognitionException {
		Opc_lista_expresionContext _localctx = new Opc_lista_expresionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_opc_lista_expresion);
		try {
			setState(186);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
			case RESTA:
			case PARENTESIS_APER:
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(184);
				lista_expresion();
				}
				break;
			case PARENTESIS_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpContext extends ParserRuleContext {
		public Lista_terminoContext lista_termino() {
			return getRuleContext(Lista_terminoContext.class,0);
		}
		public ExpContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_exp; }
	}

	public final ExpContext exp() throws RecognitionException {
		ExpContext _localctx = new ExpContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_exp);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			lista_termino();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TerminoContext extends ParserRuleContext {
		public Lista_factorContext lista_factor() {
			return getRuleContext(Lista_factorContext.class,0);
		}
		public TerminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termino; }
	}

	public final TerminoContext termino() throws RecognitionException {
		TerminoContext _localctx = new TerminoContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			lista_factor();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_terminoContext extends ParserRuleContext {
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public Lista_termino_1Context lista_termino_1() {
			return getRuleContext(Lista_termino_1Context.class,0);
		}
		public Lista_terminoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_termino; }
	}

	public final Lista_terminoContext lista_termino() throws RecognitionException {
		Lista_terminoContext _localctx = new Lista_terminoContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_lista_termino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(192);
			termino();
			setState(193);
			lista_termino_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_termino_1Context extends ParserRuleContext {
		public Suma_o_restaContext suma_o_resta() {
			return getRuleContext(Suma_o_restaContext.class,0);
		}
		public TerminoContext termino() {
			return getRuleContext(TerminoContext.class,0);
		}
		public Lista_termino_1Context lista_termino_1() {
			return getRuleContext(Lista_termino_1Context.class,0);
		}
		public Lista_termino_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_termino_1; }
	}

	public final Lista_termino_1Context lista_termino_1() throws RecognitionException {
		Lista_termino_1Context _localctx = new Lista_termino_1Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_lista_termino_1);
		try {
			setState(200);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
			case RESTA:
				enterOuterAlt(_localctx, 1);
				{
				setState(195);
				suma_o_resta();
				setState(196);
				termino();
				setState(197);
				lista_termino_1();
				}
				break;
			case MAYOR_A:
			case MENOR_A:
			case INIGUALDAD:
			case IGUALDAD:
			case PUNTO_COMA:
			case PARENTESIS_CLAU:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public Opc_suma_o_restaContext opc_suma_o_resta() {
			return getRuleContext(Opc_suma_o_restaContext.class,0);
		}
		public Id_o_cteContext id_o_cte() {
			return getRuleContext(Id_o_cteContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_factor);
		try {
			setState(209);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PARENTESIS_APER:
				enterOuterAlt(_localctx, 1);
				{
				setState(202);
				match(PARENTESIS_APER);
				setState(203);
				expresion();
				setState(204);
				match(PARENTESIS_CLAU);
				}
				break;
			case SUMA:
			case RESTA:
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(206);
				opc_suma_o_resta();
				setState(207);
				id_o_cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_factorContext extends ParserRuleContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Lista_factor_1Context lista_factor_1() {
			return getRuleContext(Lista_factor_1Context.class,0);
		}
		public Lista_factorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_factor; }
	}

	public final Lista_factorContext lista_factor() throws RecognitionException {
		Lista_factorContext _localctx = new Lista_factorContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_lista_factor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(211);
			factor();
			setState(212);
			lista_factor_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_factor_1Context extends ParserRuleContext {
		public Multiplicacion_o_divisionContext multiplicacion_o_division() {
			return getRuleContext(Multiplicacion_o_divisionContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Lista_factor_1Context lista_factor_1() {
			return getRuleContext(Lista_factor_1Context.class,0);
		}
		public Lista_factor_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_factor_1; }
	}

	public final Lista_factor_1Context lista_factor_1() throws RecognitionException {
		Lista_factor_1Context _localctx = new Lista_factor_1Context(_ctx, getState());
		enterRule(_localctx, 48, RULE_lista_factor_1);
		try {
			setState(219);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case MULTIPLICACION:
			case DIVISION:
				enterOuterAlt(_localctx, 1);
				{
				setState(214);
				multiplicacion_o_division();
				setState(215);
				factor();
				setState(216);
				lista_factor_1();
				}
				break;
			case MAYOR_A:
			case MENOR_A:
			case INIGUALDAD:
			case IGUALDAD:
			case SUMA:
			case RESTA:
			case PUNTO_COMA:
			case PARENTESIS_CLAU:
			case COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TipoContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(PatitoParser.ENTERO, 0); }
		public TerminalNode FLOTANTE() { return getToken(PatitoParser.FLOTANTE, 0); }
		public TipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipo; }
	}

	public final TipoContext tipo() throws RecognitionException {
		TipoContext _localctx = new TipoContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_tipo);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			_la = _input.LA(1);
			if ( !(_la==ENTERO || _la==FLOTANTE) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_idContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public Lista_id_1Context lista_id_1() {
			return getRuleContext(Lista_id_1Context.class,0);
		}
		public Lista_idContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_id; }
	}

	public final Lista_idContext lista_id() throws RecognitionException {
		Lista_idContext _localctx = new Lista_idContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_lista_id);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(223);
			match(ID);
			setState(224);
			lista_id_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_id_1Context extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(PatitoParser.COMA, 0); }
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public Lista_id_1Context lista_id_1() {
			return getRuleContext(Lista_id_1Context.class,0);
		}
		public Lista_id_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_id_1; }
	}

	public final Lista_id_1Context lista_id_1() throws RecognitionException {
		Lista_id_1Context _localctx = new Lista_id_1Context(_ctx, getState());
		enterRule(_localctx, 54, RULE_lista_id_1);
		try {
			setState(230);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(226);
				match(COMA);
				setState(227);
				match(ID);
				setState(228);
				lista_id_1();
				}
				break;
			case DOS_PUNTOS:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_tipoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public TerminalNode DOS_PUNTOS() { return getToken(PatitoParser.DOS_PUNTOS, 0); }
		public TipoContext tipo() {
			return getRuleContext(TipoContext.class,0);
		}
		public Id_tipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_tipo; }
	}

	public final Id_tipoContext id_tipo() throws RecognitionException {
		Id_tipoContext _localctx = new Id_tipoContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_id_tipo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(232);
			match(ID);
			setState(233);
			match(DOS_PUNTOS);
			setState(234);
			tipo();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_id_tipoContext extends ParserRuleContext {
		public Id_tipoContext id_tipo() {
			return getRuleContext(Id_tipoContext.class,0);
		}
		public Lista_id_tipo_1Context lista_id_tipo_1() {
			return getRuleContext(Lista_id_tipo_1Context.class,0);
		}
		public Lista_id_tipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_id_tipo; }
	}

	public final Lista_id_tipoContext lista_id_tipo() throws RecognitionException {
		Lista_id_tipoContext _localctx = new Lista_id_tipoContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_lista_id_tipo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(236);
			id_tipo();
			setState(237);
			lista_id_tipo_1();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Lista_id_tipo_1Context extends ParserRuleContext {
		public TerminalNode COMA() { return getToken(PatitoParser.COMA, 0); }
		public Id_tipoContext id_tipo() {
			return getRuleContext(Id_tipoContext.class,0);
		}
		public Lista_id_tipo_1Context lista_id_tipo_1() {
			return getRuleContext(Lista_id_tipo_1Context.class,0);
		}
		public Lista_id_tipo_1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lista_id_tipo_1; }
	}

	public final Lista_id_tipo_1Context lista_id_tipo_1() throws RecognitionException {
		Lista_id_tipo_1Context _localctx = new Lista_id_tipo_1Context(_ctx, getState());
		enterRule(_localctx, 60, RULE_lista_id_tipo_1);
		try {
			setState(244);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COMA:
				enterOuterAlt(_localctx, 1);
				{
				setState(239);
				match(COMA);
				setState(240);
				id_tipo();
				setState(241);
				lista_id_tipo_1();
				}
				break;
			case PARENTESIS_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_lista_id_tipoContext extends ParserRuleContext {
		public Lista_id_tipoContext lista_id_tipo() {
			return getRuleContext(Lista_id_tipoContext.class,0);
		}
		public Opc_lista_id_tipoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_lista_id_tipo; }
	}

	public final Opc_lista_id_tipoContext opc_lista_id_tipo() throws RecognitionException {
		Opc_lista_id_tipoContext _localctx = new Opc_lista_id_tipoContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_opc_lista_id_tipo);
		try {
			setState(248);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(246);
				lista_id_tipo();
				}
				break;
			case PARENTESIS_CLAU:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FuncContext extends ParserRuleContext {
		public TerminalNode NULA() { return getToken(PatitoParser.NULA, 0); }
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public Opc_lista_id_tipoContext opc_lista_id_tipo() {
			return getRuleContext(Opc_lista_id_tipoContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public TerminalNode CORCHETE_APER() { return getToken(PatitoParser.CORCHETE_APER, 0); }
		public Opc_varContext opc_var() {
			return getRuleContext(Opc_varContext.class,0);
		}
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public TerminalNode CORCHETE_CLAU() { return getToken(PatitoParser.CORCHETE_CLAU, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_func);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(250);
			match(NULA);
			setState(251);
			match(ID);
			setState(252);
			match(PARENTESIS_APER);
			setState(253);
			opc_lista_id_tipo();
			setState(254);
			match(PARENTESIS_CLAU);
			setState(255);
			match(CORCHETE_APER);
			setState(256);
			opc_var();
			setState(257);
			cuerpo();
			setState(258);
			match(CORCHETE_CLAU);
			setState(259);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_lista_funcContext extends ParserRuleContext {
		public FuncContext func() {
			return getRuleContext(FuncContext.class,0);
		}
		public Opc_lista_funcContext opc_lista_func() {
			return getRuleContext(Opc_lista_funcContext.class,0);
		}
		public Opc_lista_funcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_lista_func; }
	}

	public final Opc_lista_funcContext opc_lista_func() throws RecognitionException {
		Opc_lista_funcContext _localctx = new Opc_lista_funcContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_opc_lista_func);
		try {
			setState(265);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NULA:
				enterOuterAlt(_localctx, 1);
				{
				setState(261);
				func();
				setState(262);
				opc_lista_func();
				}
				break;
			case INICIO:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LlamadaContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public Opc_lista_expresionContext opc_lista_expresion() {
			return getRuleContext(Opc_lista_expresionContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public LlamadaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_llamada; }
	}

	public final LlamadaContext llamada() throws RecognitionException {
		LlamadaContext _localctx = new LlamadaContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_llamada);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(ID);
			setState(268);
			match(PARENTESIS_APER);
			setState(269);
			opc_lista_expresion();
			setState(270);
			match(PARENTESIS_CLAU);
			setState(271);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CteContext extends ParserRuleContext {
		public TerminalNode CTE_ENT() { return getToken(PatitoParser.CTE_ENT, 0); }
		public TerminalNode CTE_FLOT() { return getToken(PatitoParser.CTE_FLOT, 0); }
		public CteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cte; }
	}

	public final CteContext cte() throws RecognitionException {
		CteContext _localctx = new CteContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_cte);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(273);
			_la = _input.LA(1);
			if ( !(_la==CTE_ENT || _la==CTE_FLOT) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(PatitoParser.SI, 0); }
		public TerminalNode PARENTESIS_APER() { return getToken(PatitoParser.PARENTESIS_APER, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode PARENTESIS_CLAU() { return getToken(PatitoParser.PARENTESIS_CLAU, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Opc_sinoContext opc_sino() {
			return getRuleContext(Opc_sinoContext.class,0);
		}
		public TerminalNode PUNTO_COMA() { return getToken(PatitoParser.PUNTO_COMA, 0); }
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_condicion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(SI);
			setState(276);
			match(PARENTESIS_APER);
			setState(277);
			expresion();
			setState(278);
			match(PARENTESIS_CLAU);
			setState(279);
			cuerpo();
			setState(280);
			opc_sino();
			setState(281);
			match(PUNTO_COMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_sinoContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(PatitoParser.SINO, 0); }
		public CuerpoContext cuerpo() {
			return getRuleContext(CuerpoContext.class,0);
		}
		public Opc_sinoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_sino; }
	}

	public final Opc_sinoContext opc_sino() throws RecognitionException {
		Opc_sinoContext _localctx = new Opc_sinoContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_opc_sino);
		try {
			setState(286);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SINO:
				enterOuterAlt(_localctx, 1);
				{
				setState(283);
				match(SINO);
				setState(284);
				cuerpo();
				}
				break;
			case PUNTO_COMA:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Operador_relacionalContext extends ParserRuleContext {
		public TerminalNode MAYOR_A() { return getToken(PatitoParser.MAYOR_A, 0); }
		public TerminalNode MENOR_A() { return getToken(PatitoParser.MENOR_A, 0); }
		public TerminalNode INIGUALDAD() { return getToken(PatitoParser.INIGUALDAD, 0); }
		public TerminalNode IGUALDAD() { return getToken(PatitoParser.IGUALDAD, 0); }
		public Operador_relacionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operador_relacional; }
	}

	public final Operador_relacionalContext operador_relacional() throws RecognitionException {
		Operador_relacionalContext _localctx = new Operador_relacionalContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_operador_relacional);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 122880L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Suma_o_restaContext extends ParserRuleContext {
		public TerminalNode SUMA() { return getToken(PatitoParser.SUMA, 0); }
		public TerminalNode RESTA() { return getToken(PatitoParser.RESTA, 0); }
		public Suma_o_restaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_suma_o_resta; }
	}

	public final Suma_o_restaContext suma_o_resta() throws RecognitionException {
		Suma_o_restaContext _localctx = new Suma_o_restaContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_suma_o_resta);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			_la = _input.LA(1);
			if ( !(_la==SUMA || _la==RESTA) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Opc_suma_o_restaContext extends ParserRuleContext {
		public Suma_o_restaContext suma_o_resta() {
			return getRuleContext(Suma_o_restaContext.class,0);
		}
		public Opc_suma_o_restaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opc_suma_o_resta; }
	}

	public final Opc_suma_o_restaContext opc_suma_o_resta() throws RecognitionException {
		Opc_suma_o_restaContext _localctx = new Opc_suma_o_restaContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_opc_suma_o_resta);
		try {
			setState(294);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SUMA:
			case RESTA:
				enterOuterAlt(_localctx, 1);
				{
				setState(292);
				suma_o_resta();
				}
				break;
			case ID:
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Multiplicacion_o_divisionContext extends ParserRuleContext {
		public TerminalNode MULTIPLICACION() { return getToken(PatitoParser.MULTIPLICACION, 0); }
		public TerminalNode DIVISION() { return getToken(PatitoParser.DIVISION, 0); }
		public Multiplicacion_o_divisionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicacion_o_division; }
	}

	public final Multiplicacion_o_divisionContext multiplicacion_o_division() throws RecognitionException {
		Multiplicacion_o_divisionContext _localctx = new Multiplicacion_o_divisionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_multiplicacion_o_division);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(296);
			_la = _input.LA(1);
			if ( !(_la==MULTIPLICACION || _la==DIVISION) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Id_o_cteContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(PatitoParser.ID, 0); }
		public CteContext cte() {
			return getRuleContext(CteContext.class,0);
		}
		public Id_o_cteContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_id_o_cte; }
	}

	public final Id_o_cteContext id_o_cte() throws RecognitionException {
		Id_o_cteContext _localctx = new Id_o_cteContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_id_o_cte);
		try {
			setState(300);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(298);
				match(ID);
				}
				break;
			case CTE_ENT:
			case CTE_FLOT:
				enterOuterAlt(_localctx, 2);
				{
				setState(299);
				cte();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001!\u012f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0003\u0002i\b\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003r\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"}\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u0083\b\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0003\b\u008d\b\b\u0001\t\u0001\t\u0001\t"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u0097\b\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u00ad\b\u000e\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0003\u0010\u00b7\b\u0010\u0001\u0011\u0001\u0011\u0003"+
		"\u0011\u00bb\b\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0014\u0001\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0003\u0015\u00c9\b\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0003\u0016\u00d2"+
		"\b\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0003\u0018\u00dc\b\u0018\u0001\u0019\u0001"+
		"\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0001\u001b\u0003\u001b\u00e7\b\u001b\u0001\u001c\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u00f5\b\u001e\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u00f9\b\u001f\u0001 \u0001 \u0001 \u0001"+
		" \u0001 \u0001 \u0001 \u0001 \u0001 \u0001 \u0001 \u0001!\u0001!\u0001"+
		"!\u0001!\u0003!\u010a\b!\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001"+
		"\"\u0001#\u0001#\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001$\u0001"+
		"$\u0001%\u0001%\u0001%\u0003%\u011f\b%\u0001&\u0001&\u0001\'\u0001\'\u0001"+
		"(\u0001(\u0003(\u0127\b(\u0001)\u0001)\u0001*\u0001*\u0003*\u012d\b*\u0001"+
		"*\u0000\u0000+\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRT\u0000\u0005\u0001"+
		"\u0000\u0003\u0004\u0001\u0000\u001f \u0001\u0000\r\u0010\u0001\u0000"+
		"\u0011\u0012\u0001\u0000\u0013\u0014\u0119\u0000V\u0001\u0000\u0000\u0000"+
		"\u0002_\u0001\u0000\u0000\u0000\u0004h\u0001\u0000\u0000\u0000\u0006q"+
		"\u0001\u0000\u0000\u0000\bs\u0001\u0000\u0000\u0000\n|\u0001\u0000\u0000"+
		"\u0000\f\u0082\u0001\u0000\u0000\u0000\u000e\u0084\u0001\u0000\u0000\u0000"+
		"\u0010\u008c\u0001\u0000\u0000\u0000\u0012\u008e\u0001\u0000\u0000\u0000"+
		"\u0014\u0096\u0001\u0000\u0000\u0000\u0016\u0098\u0001\u0000\u0000\u0000"+
		"\u0018\u009d\u0001\u0000\u0000\u0000\u001a\u00a5\u0001\u0000\u0000\u0000"+
		"\u001c\u00ac\u0001\u0000\u0000\u0000\u001e\u00ae\u0001\u0000\u0000\u0000"+
		" \u00b6\u0001\u0000\u0000\u0000\"\u00ba\u0001\u0000\u0000\u0000$\u00bc"+
		"\u0001\u0000\u0000\u0000&\u00be\u0001\u0000\u0000\u0000(\u00c0\u0001\u0000"+
		"\u0000\u0000*\u00c8\u0001\u0000\u0000\u0000,\u00d1\u0001\u0000\u0000\u0000"+
		".\u00d3\u0001\u0000\u0000\u00000\u00db\u0001\u0000\u0000\u00002\u00dd"+
		"\u0001\u0000\u0000\u00004\u00df\u0001\u0000\u0000\u00006\u00e6\u0001\u0000"+
		"\u0000\u00008\u00e8\u0001\u0000\u0000\u0000:\u00ec\u0001\u0000\u0000\u0000"+
		"<\u00f4\u0001\u0000\u0000\u0000>\u00f8\u0001\u0000\u0000\u0000@\u00fa"+
		"\u0001\u0000\u0000\u0000B\u0109\u0001\u0000\u0000\u0000D\u010b\u0001\u0000"+
		"\u0000\u0000F\u0111\u0001\u0000\u0000\u0000H\u0113\u0001\u0000\u0000\u0000"+
		"J\u011e\u0001\u0000\u0000\u0000L\u0120\u0001\u0000\u0000\u0000N\u0122"+
		"\u0001\u0000\u0000\u0000P\u0126\u0001\u0000\u0000\u0000R\u0128\u0001\u0000"+
		"\u0000\u0000T\u012c\u0001\u0000\u0000\u0000VW\u0005\u0001\u0000\u0000"+
		"WX\u0005\u001d\u0000\u0000XY\u0005\u0016\u0000\u0000YZ\u0003\u0004\u0002"+
		"\u0000Z[\u0003B!\u0000[\\\u0005\u0002\u0000\u0000\\]\u0003\b\u0004\u0000"+
		"]^\u0005\n\u0000\u0000^\u0001\u0001\u0000\u0000\u0000_`\u0005\u0005\u0000"+
		"\u0000`a\u00034\u001a\u0000ab\u0005\u0019\u0000\u0000bc\u00032\u0019\u0000"+
		"cd\u0005\u0016\u0000\u0000de\u0003\u0006\u0003\u0000e\u0003\u0001\u0000"+
		"\u0000\u0000fi\u0003\u0002\u0001\u0000gi\u0001\u0000\u0000\u0000hf\u0001"+
		"\u0000\u0000\u0000hg\u0001\u0000\u0000\u0000i\u0005\u0001\u0000\u0000"+
		"\u0000jk\u00034\u001a\u0000kl\u0005\u0019\u0000\u0000lm\u00032\u0019\u0000"+
		"mn\u0005\u0016\u0000\u0000no\u0003\u0006\u0003\u0000or\u0001\u0000\u0000"+
		"\u0000pr\u0001\u0000\u0000\u0000qj\u0001\u0000\u0000\u0000qp\u0001\u0000"+
		"\u0000\u0000r\u0007\u0001\u0000\u0000\u0000st\u0005\u001b\u0000\u0000"+
		"tu\u0003\f\u0006\u0000uv\u0005\u001c\u0000\u0000v\t\u0001\u0000\u0000"+
		"\u0000w}\u0003\u0016\u000b\u0000x}\u0003H$\u0000y}\u0003\u0018\f\u0000"+
		"z}\u0003D\"\u0000{}\u0003\u000e\u0007\u0000|w\u0001\u0000\u0000\u0000"+
		"|x\u0001\u0000\u0000\u0000|y\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000}\u000b\u0001\u0000\u0000\u0000~\u007f"+
		"\u0003\n\u0005\u0000\u007f\u0080\u0003\f\u0006\u0000\u0080\u0083\u0001"+
		"\u0000\u0000\u0000\u0081\u0083\u0001\u0000\u0000\u0000\u0082~\u0001\u0000"+
		"\u0000\u0000\u0082\u0081\u0001\u0000\u0000\u0000\u0083\r\u0001\u0000\u0000"+
		"\u0000\u0084\u0085\u0005\u0006\u0000\u0000\u0085\u0086\u0005\u0017\u0000"+
		"\u0000\u0086\u0087\u0003\u0012\t\u0000\u0087\u0088\u0005\u0018\u0000\u0000"+
		"\u0088\u0089\u0005\u0016\u0000\u0000\u0089\u000f\u0001\u0000\u0000\u0000"+
		"\u008a\u008d\u0003\u001a\r\u0000\u008b\u008d\u0005\u001e\u0000\u0000\u008c"+
		"\u008a\u0001\u0000\u0000\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d"+
		"\u0011\u0001\u0000\u0000\u0000\u008e\u008f\u0003\u0010\b\u0000\u008f\u0090"+
		"\u0003\u0014\n\u0000\u0090\u0013\u0001\u0000\u0000\u0000\u0091\u0092\u0005"+
		"\u001a\u0000\u0000\u0092\u0093\u0003\u0010\b\u0000\u0093\u0094\u0003\u0014"+
		"\n\u0000\u0094\u0097\u0001\u0000\u0000\u0000\u0095\u0097\u0001\u0000\u0000"+
		"\u0000\u0096\u0091\u0001\u0000\u0000\u0000\u0096\u0095\u0001\u0000\u0000"+
		"\u0000\u0097\u0015\u0001\u0000\u0000\u0000\u0098\u0099\u0005\u001d\u0000"+
		"\u0000\u0099\u009a\u0005\u0015\u0000\u0000\u009a\u009b\u0003\u001a\r\u0000"+
		"\u009b\u009c\u0005\u0016\u0000\u0000\u009c\u0017\u0001\u0000\u0000\u0000"+
		"\u009d\u009e\u0005\u0007\u0000\u0000\u009e\u009f\u0005\u0017\u0000\u0000"+
		"\u009f\u00a0\u0003\u001a\r\u0000\u00a0\u00a1\u0005\u0018\u0000\u0000\u00a1"+
		"\u00a2\u0005\b\u0000\u0000\u00a2\u00a3\u0003\b\u0004\u0000\u00a3\u00a4"+
		"\u0005\u0016\u0000\u0000\u00a4\u0019\u0001\u0000\u0000\u0000\u00a5\u00a6"+
		"\u0003$\u0012\u0000\u00a6\u00a7\u0003\u001c\u000e\u0000\u00a7\u001b\u0001"+
		"\u0000\u0000\u0000\u00a8\u00a9\u0003L&\u0000\u00a9\u00aa\u0003$\u0012"+
		"\u0000\u00aa\u00ad\u0001\u0000\u0000\u0000\u00ab\u00ad\u0001\u0000\u0000"+
		"\u0000\u00ac\u00a8\u0001\u0000\u0000\u0000\u00ac\u00ab\u0001\u0000\u0000"+
		"\u0000\u00ad\u001d\u0001\u0000\u0000\u0000\u00ae\u00af\u0003\u001a\r\u0000"+
		"\u00af\u00b0\u0003 \u0010\u0000\u00b0\u001f\u0001\u0000\u0000\u0000\u00b1"+
		"\u00b2\u0005\u001a\u0000\u0000\u00b2\u00b3\u0003\u001a\r\u0000\u00b3\u00b4"+
		"\u0003 \u0010\u0000\u00b4\u00b7\u0001\u0000\u0000\u0000\u00b5\u00b7\u0001"+
		"\u0000\u0000\u0000\u00b6\u00b1\u0001\u0000\u0000\u0000\u00b6\u00b5\u0001"+
		"\u0000\u0000\u0000\u00b7!\u0001\u0000\u0000\u0000\u00b8\u00bb\u0003\u001e"+
		"\u000f\u0000\u00b9\u00bb\u0001\u0000\u0000\u0000\u00ba\u00b8\u0001\u0000"+
		"\u0000\u0000\u00ba\u00b9\u0001\u0000\u0000\u0000\u00bb#\u0001\u0000\u0000"+
		"\u0000\u00bc\u00bd\u0003(\u0014\u0000\u00bd%\u0001\u0000\u0000\u0000\u00be"+
		"\u00bf\u0003.\u0017\u0000\u00bf\'\u0001\u0000\u0000\u0000\u00c0\u00c1"+
		"\u0003&\u0013\u0000\u00c1\u00c2\u0003*\u0015\u0000\u00c2)\u0001\u0000"+
		"\u0000\u0000\u00c3\u00c4\u0003N\'\u0000\u00c4\u00c5\u0003&\u0013\u0000"+
		"\u00c5\u00c6\u0003*\u0015\u0000\u00c6\u00c9\u0001\u0000\u0000\u0000\u00c7"+
		"\u00c9\u0001\u0000\u0000\u0000\u00c8\u00c3\u0001\u0000\u0000\u0000\u00c8"+
		"\u00c7\u0001\u0000\u0000\u0000\u00c9+\u0001\u0000\u0000\u0000\u00ca\u00cb"+
		"\u0005\u0017\u0000\u0000\u00cb\u00cc\u0003\u001a\r\u0000\u00cc\u00cd\u0005"+
		"\u0018\u0000\u0000\u00cd\u00d2\u0001\u0000\u0000\u0000\u00ce\u00cf\u0003"+
		"P(\u0000\u00cf\u00d0\u0003T*\u0000\u00d0\u00d2\u0001\u0000\u0000\u0000"+
		"\u00d1\u00ca\u0001\u0000\u0000\u0000\u00d1\u00ce\u0001\u0000\u0000\u0000"+
		"\u00d2-\u0001\u0000\u0000\u0000\u00d3\u00d4\u0003,\u0016\u0000\u00d4\u00d5"+
		"\u00030\u0018\u0000\u00d5/\u0001\u0000\u0000\u0000\u00d6\u00d7\u0003R"+
		")\u0000\u00d7\u00d8\u0003,\u0016\u0000\u00d8\u00d9\u00030\u0018\u0000"+
		"\u00d9\u00dc\u0001\u0000\u0000\u0000\u00da\u00dc\u0001\u0000\u0000\u0000"+
		"\u00db\u00d6\u0001\u0000\u0000\u0000\u00db\u00da\u0001\u0000\u0000\u0000"+
		"\u00dc1\u0001\u0000\u0000\u0000\u00dd\u00de\u0007\u0000\u0000\u0000\u00de"+
		"3\u0001\u0000\u0000\u0000\u00df\u00e0\u0005\u001d\u0000\u0000\u00e0\u00e1"+
		"\u00036\u001b\u0000\u00e15\u0001\u0000\u0000\u0000\u00e2\u00e3\u0005\u001a"+
		"\u0000\u0000\u00e3\u00e4\u0005\u001d\u0000\u0000\u00e4\u00e7\u00036\u001b"+
		"\u0000\u00e5\u00e7\u0001\u0000\u0000\u0000\u00e6\u00e2\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e5\u0001\u0000\u0000\u0000\u00e77\u0001\u0000\u0000\u0000"+
		"\u00e8\u00e9\u0005\u001d\u0000\u0000\u00e9\u00ea\u0005\u0019\u0000\u0000"+
		"\u00ea\u00eb\u00032\u0019\u0000\u00eb9\u0001\u0000\u0000\u0000\u00ec\u00ed"+
		"\u00038\u001c\u0000\u00ed\u00ee\u0003<\u001e\u0000\u00ee;\u0001\u0000"+
		"\u0000\u0000\u00ef\u00f0\u0005\u001a\u0000\u0000\u00f0\u00f1\u00038\u001c"+
		"\u0000\u00f1\u00f2\u0003<\u001e\u0000\u00f2\u00f5\u0001\u0000\u0000\u0000"+
		"\u00f3\u00f5\u0001\u0000\u0000\u0000\u00f4\u00ef\u0001\u0000\u0000\u0000"+
		"\u00f4\u00f3\u0001\u0000\u0000\u0000\u00f5=\u0001\u0000\u0000\u0000\u00f6"+
		"\u00f9\u0003:\u001d\u0000\u00f7\u00f9\u0001\u0000\u0000\u0000\u00f8\u00f6"+
		"\u0001\u0000\u0000\u0000\u00f8\u00f7\u0001\u0000\u0000\u0000\u00f9?\u0001"+
		"\u0000\u0000\u0000\u00fa\u00fb\u0005\u000b\u0000\u0000\u00fb\u00fc\u0005"+
		"\u001d\u0000\u0000\u00fc\u00fd\u0005\u0017\u0000\u0000\u00fd\u00fe\u0003"+
		">\u001f\u0000\u00fe\u00ff\u0005\u0018\u0000\u0000\u00ff\u0100\u0005\u001b"+
		"\u0000\u0000\u0100\u0101\u0003\u0004\u0002\u0000\u0101\u0102\u0003\b\u0004"+
		"\u0000\u0102\u0103\u0005\u001c\u0000\u0000\u0103\u0104\u0005\u0016\u0000"+
		"\u0000\u0104A\u0001\u0000\u0000\u0000\u0105\u0106\u0003@ \u0000\u0106"+
		"\u0107\u0003B!\u0000\u0107\u010a\u0001\u0000\u0000\u0000\u0108\u010a\u0001"+
		"\u0000\u0000\u0000\u0109\u0105\u0001\u0000\u0000\u0000\u0109\u0108\u0001"+
		"\u0000\u0000\u0000\u010aC\u0001\u0000\u0000\u0000\u010b\u010c\u0005\u001d"+
		"\u0000\u0000\u010c\u010d\u0005\u0017\u0000\u0000\u010d\u010e\u0003\"\u0011"+
		"\u0000\u010e\u010f\u0005\u0018\u0000\u0000\u010f\u0110\u0005\u0016\u0000"+
		"\u0000\u0110E\u0001\u0000\u0000\u0000\u0111\u0112\u0007\u0001\u0000\u0000"+
		"\u0112G\u0001\u0000\u0000\u0000\u0113\u0114\u0005\f\u0000\u0000\u0114"+
		"\u0115\u0005\u0017\u0000\u0000\u0115\u0116\u0003\u001a\r\u0000\u0116\u0117"+
		"\u0005\u0018\u0000\u0000\u0117\u0118\u0003\b\u0004\u0000\u0118\u0119\u0003"+
		"J%\u0000\u0119\u011a\u0005\u0016\u0000\u0000\u011aI\u0001\u0000\u0000"+
		"\u0000\u011b\u011c\u0005\t\u0000\u0000\u011c\u011f\u0003\b\u0004\u0000"+
		"\u011d\u011f\u0001\u0000\u0000\u0000\u011e\u011b\u0001\u0000\u0000\u0000"+
		"\u011e\u011d\u0001\u0000\u0000\u0000\u011fK\u0001\u0000\u0000\u0000\u0120"+
		"\u0121\u0007\u0002\u0000\u0000\u0121M\u0001\u0000\u0000\u0000\u0122\u0123"+
		"\u0007\u0003\u0000\u0000\u0123O\u0001\u0000\u0000\u0000\u0124\u0127\u0003"+
		"N\'\u0000\u0125\u0127\u0001\u0000\u0000\u0000\u0126\u0124\u0001\u0000"+
		"\u0000\u0000\u0126\u0125\u0001\u0000\u0000\u0000\u0127Q\u0001\u0000\u0000"+
		"\u0000\u0128\u0129\u0007\u0004\u0000\u0000\u0129S\u0001\u0000\u0000\u0000"+
		"\u012a\u012d\u0005\u001d\u0000\u0000\u012b\u012d\u0003F#\u0000\u012c\u012a"+
		"\u0001\u0000\u0000\u0000\u012c\u012b\u0001\u0000\u0000\u0000\u012dU\u0001"+
		"\u0000\u0000\u0000\u0013hq|\u0082\u008c\u0096\u00ac\u00b6\u00ba\u00c8"+
		"\u00d1\u00db\u00e6\u00f4\u00f8\u0109\u011e\u0126\u012c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}