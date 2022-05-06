// Generated from /home/rr/repositorios/sigon/sigon/grammar/Agent.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AgentParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, CUSTOMLOGICALNAME=30, 
		CUSTOMFUNCTIONALNAME=31, NUMERAL=32, CONSTANT=33, VARIABLE=34, AND=35, 
		OR=36, LeftParen=37, RightParen=38, STRING=39, WS=40, BlockComment=41, 
		LineComment=42;
	public static final int
		RULE_agent = 0, RULE_context = 1, RULE_bridgeRule = 2, RULE_logicalContext = 3, 
		RULE_functionalContext = 4, RULE_communicationContext = 5, RULE_plannerContext = 6, 
		RULE_customFunctionalContext = 7, RULE_logicalContextName = 8, RULE_primitiveContextName = 9, 
		RULE_customLogicalContextName = 10, RULE_plan = 11, RULE_somethingToBeTrue = 12, 
		RULE_preConditions = 13, RULE_postConditions = 14, RULE_planConditions = 15, 
		RULE_condition = 16, RULE_conditionTerm = 17, RULE_planPostconditions = 18, 
		RULE_contextReference = 19, RULE_conditions = 20, RULE_conditions1 = 21, 
		RULE_action = 22, RULE_actionPreconditions = 23, RULE_actionPostconditions = 24, 
		RULE_functionInvocation = 25, RULE_functionName = 26, RULE_sensor = 27, 
		RULE_sensorIdentifier = 28, RULE_sensorImplementation = 29, RULE_actuator = 30, 
		RULE_actuatorIdentifier = 31, RULE_actuatorImplementation = 32, RULE_internalOperator = 33, 
		RULE_beliefAdition = 34, RULE_beliefRemotion = 35, RULE_desireAdition = 36, 
		RULE_desireRemotion = 37, RULE_argumentList = 38, RULE_expression = 39, 
		RULE_compoundAction = 40, RULE_plansFormulas = 41, RULE_contextName = 42, 
		RULE_head = 43, RULE_body = 44, RULE_otherBodyRules = 45, RULE_bodyTerm = 46, 
		RULE_logicalOperator = 47, RULE_term = 48, RULE_term2 = 49, RULE_formulas = 50, 
		RULE_atom = 51, RULE_operator = 52, RULE_negation = 53, RULE_annotation = 54, 
		RULE_preAction = 55, RULE_gradedValue = 56, RULE_cost = 57;
	private static String[] makeRuleNames() {
		return new String[] {
			"agent", "context", "bridgeRule", "logicalContext", "functionalContext", 
			"communicationContext", "plannerContext", "customFunctionalContext", 
			"logicalContextName", "primitiveContextName", "customLogicalContextName", 
			"plan", "somethingToBeTrue", "preConditions", "postConditions", "planConditions", 
			"condition", "conditionTerm", "planPostconditions", "contextReference", 
			"conditions", "conditions1", "action", "actionPreconditions", "actionPostconditions", 
			"functionInvocation", "functionName", "sensor", "sensorIdentifier", "sensorImplementation", 
			"actuator", "actuatorIdentifier", "actuatorImplementation", "internalOperator", 
			"beliefAdition", "beliefRemotion", "desireAdition", "desireRemotion", 
			"argumentList", "expression", "compoundAction", "plansFormulas", "contextName", 
			"head", "body", "otherBodyRules", "bodyTerm", "logicalOperator", "term", 
			"term2", "formulas", "atom", "operator", "negation", "annotation", "preAction", 
			"gradedValue", "cost"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "':-'", "'.'", "':'", "'communication'", "'planner'", "'beliefs'", 
			"'desires'", "'intentions'", "'plan'", "','", "'_'", "'['", "']'", "'action'", 
			"'sensor'", "'actuator'", "'+'", "'-'", "'+!'", "'-!'", "'!'", "'<'", 
			"'=<'", "'>'", "'>='", "'not '", "'~'", "'->0.'", "'0.'", null, null, 
			null, null, null, "'&'", "'|'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "CUSTOMLOGICALNAME", "CUSTOMFUNCTIONALNAME", 
			"NUMERAL", "CONSTANT", "VARIABLE", "AND", "OR", "LeftParen", "RightParen", 
			"STRING", "WS", "BlockComment", "LineComment"
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
	public String getGrammarFileName() { return "Agent.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AgentParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class AgentContext extends ParserRuleContext {
		public CommunicationContextContext communicationContext() {
			return getRuleContext(CommunicationContextContext.class,0);
		}
		public TerminalNode EOF() { return getToken(AgentParser.EOF, 0); }
		public List<ContextContext> context() {
			return getRuleContexts(ContextContext.class);
		}
		public ContextContext context(int i) {
			return getRuleContext(ContextContext.class,i);
		}
		public List<BridgeRuleContext> bridgeRule() {
			return getRuleContexts(BridgeRuleContext.class);
		}
		public BridgeRuleContext bridgeRule(int i) {
			return getRuleContext(BridgeRuleContext.class,i);
		}
		public AgentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_agent; }
	}

	public final AgentContext agent() throws RecognitionException {
		AgentContext _localctx = new AgentContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_agent);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			communicationContext();
			setState(121);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__3) | (1L << T__4) | (1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << T__20) | (1L << CUSTOMLOGICALNAME) | (1L << CUSTOMFUNCTIONALNAME))) != 0)) {
				{
				setState(119);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__3:
				case T__4:
				case T__5:
				case T__6:
				case T__7:
				case CUSTOMLOGICALNAME:
				case CUSTOMFUNCTIONALNAME:
					{
					setState(117);
					context();
					}
					break;
				case T__20:
					{
					setState(118);
					bridgeRule();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(123);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(124);
			match(EOF);
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

	public static class ContextContext extends ParserRuleContext {
		public LogicalContextContext logicalContext() {
			return getRuleContext(LogicalContextContext.class,0);
		}
		public FunctionalContextContext functionalContext() {
			return getRuleContext(FunctionalContextContext.class,0);
		}
		public ContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_context; }
	}

	public final ContextContext context() throws RecognitionException {
		ContextContext _localctx = new ContextContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_context);
		try {
			setState(128);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__6:
			case T__7:
			case CUSTOMLOGICALNAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(126);
				logicalContext();
				}
				break;
			case T__3:
			case T__4:
			case CUSTOMFUNCTIONALNAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(127);
				functionalContext();
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

	public static class BridgeRuleContext extends ParserRuleContext {
		public HeadContext head() {
			return getRuleContext(HeadContext.class,0);
		}
		public BodyContext body() {
			return getRuleContext(BodyContext.class,0);
		}
		public BridgeRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bridgeRule; }
	}

	public final BridgeRuleContext bridgeRule() throws RecognitionException {
		BridgeRuleContext _localctx = new BridgeRuleContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_bridgeRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(130);
			head();
			setState(131);
			match(T__0);
			setState(132);
			body();
			setState(133);
			match(T__1);
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

	public static class LogicalContextContext extends ParserRuleContext {
		public LogicalContextNameContext logicalContextName() {
			return getRuleContext(LogicalContextNameContext.class,0);
		}
		public FormulasContext formulas() {
			return getRuleContext(FormulasContext.class,0);
		}
		public LogicalContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalContext; }
	}

	public final LogicalContextContext logicalContext() throws RecognitionException {
		LogicalContextContext _localctx = new LogicalContextContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_logicalContext);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			logicalContextName();
			setState(136);
			match(T__2);
			setState(137);
			formulas();
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

	public static class FunctionalContextContext extends ParserRuleContext {
		public CommunicationContextContext communicationContext() {
			return getRuleContext(CommunicationContextContext.class,0);
		}
		public PlannerContextContext plannerContext() {
			return getRuleContext(PlannerContextContext.class,0);
		}
		public CustomFunctionalContextContext customFunctionalContext() {
			return getRuleContext(CustomFunctionalContextContext.class,0);
		}
		public FunctionalContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionalContext; }
	}

	public final FunctionalContextContext functionalContext() throws RecognitionException {
		FunctionalContextContext _localctx = new FunctionalContextContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_functionalContext);
		try {
			setState(142);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__3:
				enterOuterAlt(_localctx, 1);
				{
				setState(139);
				communicationContext();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(140);
				plannerContext();
				}
				break;
			case CUSTOMFUNCTIONALNAME:
				enterOuterAlt(_localctx, 3);
				{
				setState(141);
				customFunctionalContext();
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

	public static class CommunicationContextContext extends ParserRuleContext {
		public List<SensorContext> sensor() {
			return getRuleContexts(SensorContext.class);
		}
		public SensorContext sensor(int i) {
			return getRuleContext(SensorContext.class,i);
		}
		public List<ActuatorContext> actuator() {
			return getRuleContexts(ActuatorContext.class);
		}
		public ActuatorContext actuator(int i) {
			return getRuleContext(ActuatorContext.class,i);
		}
		public CommunicationContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_communicationContext; }
	}

	public final CommunicationContextContext communicationContext() throws RecognitionException {
		CommunicationContextContext _localctx = new CommunicationContextContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_communicationContext);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			match(T__3);
			setState(145);
			match(T__2);
			setState(148); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				setState(148);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__14:
					{
					setState(146);
					sensor();
					}
					break;
				case T__15:
					{
					setState(147);
					actuator();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				setState(150); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__14 || _la==T__15 );
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

	public static class PlannerContextContext extends ParserRuleContext {
		public PlansFormulasContext plansFormulas() {
			return getRuleContext(PlansFormulasContext.class,0);
		}
		public PlannerContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plannerContext; }
	}

	public final PlannerContextContext plannerContext() throws RecognitionException {
		PlannerContextContext _localctx = new PlannerContextContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_plannerContext);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(T__4);
			setState(153);
			match(T__2);
			setState(154);
			plansFormulas();
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

	public static class CustomFunctionalContextContext extends ParserRuleContext {
		public TerminalNode CUSTOMFUNCTIONALNAME() { return getToken(AgentParser.CUSTOMFUNCTIONALNAME, 0); }
		public CustomFunctionalContextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_customFunctionalContext; }
	}

	public final CustomFunctionalContextContext customFunctionalContext() throws RecognitionException {
		CustomFunctionalContextContext _localctx = new CustomFunctionalContextContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_customFunctionalContext);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(156);
			match(CUSTOMFUNCTIONALNAME);
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

	public static class LogicalContextNameContext extends ParserRuleContext {
		public PrimitiveContextNameContext primitiveContextName() {
			return getRuleContext(PrimitiveContextNameContext.class,0);
		}
		public CustomLogicalContextNameContext customLogicalContextName() {
			return getRuleContext(CustomLogicalContextNameContext.class,0);
		}
		public LogicalContextNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalContextName; }
	}

	public final LogicalContextNameContext logicalContextName() throws RecognitionException {
		LogicalContextNameContext _localctx = new LogicalContextNameContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_logicalContextName);
		try {
			setState(160);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__6:
			case T__7:
				enterOuterAlt(_localctx, 1);
				{
				setState(158);
				primitiveContextName();
				}
				break;
			case CUSTOMLOGICALNAME:
				enterOuterAlt(_localctx, 2);
				{
				setState(159);
				customLogicalContextName();
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

	public static class PrimitiveContextNameContext extends ParserRuleContext {
		public PrimitiveContextNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primitiveContextName; }
	}

	public final PrimitiveContextNameContext primitiveContextName() throws RecognitionException {
		PrimitiveContextNameContext _localctx = new PrimitiveContextNameContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_primitiveContextName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(162);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7))) != 0)) ) {
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

	public static class CustomLogicalContextNameContext extends ParserRuleContext {
		public TerminalNode CUSTOMLOGICALNAME() { return getToken(AgentParser.CUSTOMLOGICALNAME, 0); }
		public CustomLogicalContextNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_customLogicalContextName; }
	}

	public final CustomLogicalContextNameContext customLogicalContextName() throws RecognitionException {
		CustomLogicalContextNameContext _localctx = new CustomLogicalContextNameContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_customLogicalContextName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(164);
			match(CUSTOMLOGICALNAME);
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

	public static class PlanContext extends ParserRuleContext {
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public SomethingToBeTrueContext somethingToBeTrue() {
			return getRuleContext(SomethingToBeTrueContext.class,0);
		}
		public CompoundActionContext compoundAction() {
			return getRuleContext(CompoundActionContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public PreConditionsContext preConditions() {
			return getRuleContext(PreConditionsContext.class,0);
		}
		public PostConditionsContext postConditions() {
			return getRuleContext(PostConditionsContext.class,0);
		}
		public CostContext cost() {
			return getRuleContext(CostContext.class,0);
		}
		public InternalOperatorContext internalOperator() {
			return getRuleContext(InternalOperatorContext.class,0);
		}
		public PlanContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plan; }
	}

	public final PlanContext plan() throws RecognitionException {
		PlanContext _localctx = new PlanContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_plan);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			match(T__8);
			setState(167);
			match(LeftParen);
			setState(168);
			somethingToBeTrue();
			setState(169);
			match(T__9);
			setState(170);
			compoundAction();
			setState(179);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(171);
				match(T__9);
				setState(172);
				preConditions();
				setState(173);
				match(T__9);
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) {
					{
					setState(174);
					internalOperator();
					}
				}

				setState(177);
				postConditions();
				}
				break;
			}
			setState(183);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(181);
				match(T__9);
				setState(182);
				cost();
				}
			}

			setState(185);
			match(RightParen);
			setState(186);
			match(T__1);
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

	public static class SomethingToBeTrueContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public SomethingToBeTrueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_somethingToBeTrue; }
	}

	public final SomethingToBeTrueContext somethingToBeTrue() throws RecognitionException {
		SomethingToBeTrueContext _localctx = new SomethingToBeTrueContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_somethingToBeTrue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(188);
			term(0);
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

	public static class PreConditionsContext extends ParserRuleContext {
		public PlanConditionsContext planConditions() {
			return getRuleContext(PlanConditionsContext.class,0);
		}
		public PreConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preConditions; }
	}

	public final PreConditionsContext preConditions() throws RecognitionException {
		PreConditionsContext _localctx = new PreConditionsContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_preConditions);
		try {
			setState(195);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(190);
				match(T__10);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(191);
				match(T__11);
				setState(192);
				planConditions();
				setState(193);
				match(T__12);
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

	public static class PostConditionsContext extends ParserRuleContext {
		public PlanConditionsContext planConditions() {
			return getRuleContext(PlanConditionsContext.class,0);
		}
		public PostConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_postConditions; }
	}

	public final PostConditionsContext postConditions() throws RecognitionException {
		PostConditionsContext _localctx = new PostConditionsContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_postConditions);
		try {
			setState(202);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				enterOuterAlt(_localctx, 1);
				{
				setState(197);
				match(T__10);
				}
				break;
			case T__11:
				enterOuterAlt(_localctx, 2);
				{
				setState(198);
				match(T__11);
				setState(199);
				planConditions();
				setState(200);
				match(T__12);
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

	public static class PlanConditionsContext extends ParserRuleContext {
		public List<ConditionContext> condition() {
			return getRuleContexts(ConditionContext.class);
		}
		public ConditionContext condition(int i) {
			return getRuleContext(ConditionContext.class,i);
		}
		public PlanConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_planConditions; }
	}

	public final PlanConditionsContext planConditions() throws RecognitionException {
		PlanConditionsContext _localctx = new PlanConditionsContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_planConditions);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(205); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(204);
				condition();
				}
				}
				setState(207); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__5) | (1L << T__6) | (1L << T__7) | (1L << CUSTOMLOGICALNAME))) != 0) );
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

	public static class ConditionContext extends ParserRuleContext {
		public ContextReferenceContext contextReference() {
			return getRuleContext(ContextReferenceContext.class,0);
		}
		public ConditionTermContext conditionTerm() {
			return getRuleContext(ConditionTermContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_condition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(209);
			contextReference();
			setState(210);
			match(T__2);
			setState(211);
			conditionTerm();
			setState(213);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(212);
				match(T__9);
				}
			}

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

	public static class ConditionTermContext extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public NegationContext negation() {
			return getRuleContext(NegationContext.class,0);
		}
		public AnnotationContext annotation() {
			return getRuleContext(AnnotationContext.class,0);
		}
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public List<ConditionTermContext> conditionTerm() {
			return getRuleContexts(ConditionTermContext.class);
		}
		public ConditionTermContext conditionTerm(int i) {
			return getRuleContext(ConditionTermContext.class,i);
		}
		public TerminalNode AND() { return getToken(AgentParser.AND, 0); }
		public TerminalNode OR() { return getToken(AgentParser.OR, 0); }
		public ConditionTermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionTerm; }
	}

	public final ConditionTermContext conditionTerm() throws RecognitionException {
		ConditionTermContext _localctx = new ConditionTermContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_conditionTerm);
		int _la;
		try {
			setState(242);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
			case CONSTANT:
				enterOuterAlt(_localctx, 1);
				{
				setState(216);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25 || _la==T__26) {
					{
					setState(215);
					negation();
					}
				}

				setState(218);
				match(CONSTANT);
				setState(234);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__11:
				case T__27:
					{
					setState(219);
					annotation();
					}
					break;
				case LeftParen:
					{
					{
					setState(220);
					match(LeftParen);
					setState(221);
					atom();
					setState(226);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__9) {
						{
						{
						setState(222);
						match(T__9);
						setState(223);
						atom();
						}
						}
						setState(228);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(229);
					match(RightParen);
					}
					setState(232);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__11 || _la==T__27) {
						{
						setState(231);
						annotation();
						}
					}

					}
					break;
				case T__0:
				case T__5:
				case T__6:
				case T__7:
				case T__9:
				case T__12:
				case CUSTOMLOGICALNAME:
				case AND:
				case OR:
				case RightParen:
					break;
				default:
					break;
				}
				}
				break;
			case LeftParen:
				enterOuterAlt(_localctx, 2);
				{
				setState(236);
				match(LeftParen);
				setState(237);
				conditionTerm();
				setState(238);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__0) | (1L << AND) | (1L << OR))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(239);
				conditionTerm();
				setState(240);
				match(RightParen);
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

	public static class PlanPostconditionsContext extends ParserRuleContext {
		public ConditionsContext conditions() {
			return getRuleContext(ConditionsContext.class,0);
		}
		public PlanPostconditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_planPostconditions; }
	}

	public final PlanPostconditionsContext planPostconditions() throws RecognitionException {
		PlanPostconditionsContext _localctx = new PlanPostconditionsContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_planPostconditions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			conditions();
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

	public static class ContextReferenceContext extends ParserRuleContext {
		public PrimitiveContextNameContext primitiveContextName() {
			return getRuleContext(PrimitiveContextNameContext.class,0);
		}
		public CustomLogicalContextNameContext customLogicalContextName() {
			return getRuleContext(CustomLogicalContextNameContext.class,0);
		}
		public ContextReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextReference; }
	}

	public final ContextReferenceContext contextReference() throws RecognitionException {
		ContextReferenceContext _localctx = new ContextReferenceContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_contextReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(248);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__6:
			case T__7:
				{
				setState(246);
				primitiveContextName();
				}
				break;
			case CUSTOMLOGICALNAME:
				{
				setState(247);
				customLogicalContextName();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ConditionsContext extends ParserRuleContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public ConditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditions; }
	}

	public final ConditionsContext conditions() throws RecognitionException {
		ConditionsContext _localctx = new ConditionsContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_conditions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(252);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				{
				setState(250);
				match(T__10);
				}
				break;
			case T__11:
			case T__25:
			case T__26:
			case CONSTANT:
				{
				setState(251);
				term(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class Conditions1Context extends ParserRuleContext {
		public Term2Context term2() {
			return getRuleContext(Term2Context.class,0);
		}
		public Conditions1Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditions1; }
	}

	public final Conditions1Context conditions1() throws RecognitionException {
		Conditions1Context _localctx = new Conditions1Context(_ctx, getState());
		enterRule(_localctx, 42, RULE_conditions1);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(256);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__10:
				{
				setState(254);
				match(T__10);
				}
				break;
			case T__25:
			case T__26:
			case CONSTANT:
				{
				setState(255);
				term2();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class ActionContext extends ParserRuleContext {
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public FunctionInvocationContext functionInvocation() {
			return getRuleContext(FunctionInvocationContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public ActionPreconditionsContext actionPreconditions() {
			return getRuleContext(ActionPreconditionsContext.class,0);
		}
		public ActionPostconditionsContext actionPostconditions() {
			return getRuleContext(ActionPostconditionsContext.class,0);
		}
		public CostContext cost() {
			return getRuleContext(CostContext.class,0);
		}
		public InternalOperatorContext internalOperator() {
			return getRuleContext(InternalOperatorContext.class,0);
		}
		public ActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_action; }
	}

	public final ActionContext action() throws RecognitionException {
		ActionContext _localctx = new ActionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_action);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(258);
			match(T__13);
			setState(259);
			match(LeftParen);
			setState(260);
			functionInvocation();
			setState(269);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				{
				setState(261);
				match(T__9);
				setState(262);
				actionPreconditions();
				setState(263);
				match(T__9);
				setState(265);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << T__18))) != 0)) {
					{
					setState(264);
					internalOperator();
					}
				}

				setState(267);
				actionPostconditions();
				}
				break;
			}
			setState(273);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__9) {
				{
				setState(271);
				match(T__9);
				setState(272);
				cost();
				}
			}

			setState(275);
			match(RightParen);
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

	public static class ActionPreconditionsContext extends ParserRuleContext {
		public ConditionsContext conditions() {
			return getRuleContext(ConditionsContext.class,0);
		}
		public ActionPreconditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actionPreconditions; }
	}

	public final ActionPreconditionsContext actionPreconditions() throws RecognitionException {
		ActionPreconditionsContext _localctx = new ActionPreconditionsContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_actionPreconditions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			conditions();
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

	public static class ActionPostconditionsContext extends ParserRuleContext {
		public ConditionsContext conditions() {
			return getRuleContext(ConditionsContext.class,0);
		}
		public ActionPostconditionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actionPostconditions; }
	}

	public final ActionPostconditionsContext actionPostconditions() throws RecognitionException {
		ActionPostconditionsContext _localctx = new ActionPostconditionsContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_actionPostconditions);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(279);
			conditions();
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

	public static class FunctionInvocationContext extends ParserRuleContext {
		public FunctionNameContext functionName() {
			return getRuleContext(FunctionNameContext.class,0);
		}
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionInvocationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionInvocation; }
	}

	public final FunctionInvocationContext functionInvocation() throws RecognitionException {
		FunctionInvocationContext _localctx = new FunctionInvocationContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_functionInvocation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			functionName();
			setState(282);
			match(LeftParen);
			setState(284);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONSTANT || _la==VARIABLE) {
				{
				setState(283);
				argumentList();
				}
			}

			setState(286);
			match(RightParen);
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

	public static class FunctionNameContext extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public FunctionNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionName; }
	}

	public final FunctionNameContext functionName() throws RecognitionException {
		FunctionNameContext _localctx = new FunctionNameContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_functionName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(288);
			match(CONSTANT);
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

	public static class SensorContext extends ParserRuleContext {
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public SensorIdentifierContext sensorIdentifier() {
			return getRuleContext(SensorIdentifierContext.class,0);
		}
		public SensorImplementationContext sensorImplementation() {
			return getRuleContext(SensorImplementationContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public SensorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sensor; }
	}

	public final SensorContext sensor() throws RecognitionException {
		SensorContext _localctx = new SensorContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_sensor);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(290);
			match(T__14);
			setState(291);
			match(LeftParen);
			setState(292);
			sensorIdentifier();
			setState(293);
			match(T__9);
			setState(294);
			sensorImplementation();
			setState(295);
			match(RightParen);
			setState(296);
			match(T__1);
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

	public static class SensorIdentifierContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(AgentParser.STRING, 0); }
		public SensorIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sensorIdentifier; }
	}

	public final SensorIdentifierContext sensorIdentifier() throws RecognitionException {
		SensorIdentifierContext _localctx = new SensorIdentifierContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_sensorIdentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(298);
			match(STRING);
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

	public static class SensorImplementationContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(AgentParser.STRING, 0); }
		public SensorImplementationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sensorImplementation; }
	}

	public final SensorImplementationContext sensorImplementation() throws RecognitionException {
		SensorImplementationContext _localctx = new SensorImplementationContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_sensorImplementation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(STRING);
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

	public static class ActuatorContext extends ParserRuleContext {
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public ActuatorIdentifierContext actuatorIdentifier() {
			return getRuleContext(ActuatorIdentifierContext.class,0);
		}
		public ActuatorImplementationContext actuatorImplementation() {
			return getRuleContext(ActuatorImplementationContext.class,0);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public ActuatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actuator; }
	}

	public final ActuatorContext actuator() throws RecognitionException {
		ActuatorContext _localctx = new ActuatorContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_actuator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			match(T__15);
			setState(303);
			match(LeftParen);
			setState(304);
			actuatorIdentifier();
			setState(305);
			match(T__9);
			setState(306);
			actuatorImplementation();
			setState(307);
			match(RightParen);
			setState(308);
			match(T__1);
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

	public static class ActuatorIdentifierContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(AgentParser.STRING, 0); }
		public ActuatorIdentifierContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actuatorIdentifier; }
	}

	public final ActuatorIdentifierContext actuatorIdentifier() throws RecognitionException {
		ActuatorIdentifierContext _localctx = new ActuatorIdentifierContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_actuatorIdentifier);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(310);
			match(STRING);
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

	public static class ActuatorImplementationContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(AgentParser.STRING, 0); }
		public ActuatorImplementationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_actuatorImplementation; }
	}

	public final ActuatorImplementationContext actuatorImplementation() throws RecognitionException {
		ActuatorImplementationContext _localctx = new ActuatorImplementationContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_actuatorImplementation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(312);
			match(STRING);
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

	public static class InternalOperatorContext extends ParserRuleContext {
		public BeliefAditionContext beliefAdition() {
			return getRuleContext(BeliefAditionContext.class,0);
		}
		public BeliefRemotionContext beliefRemotion() {
			return getRuleContext(BeliefRemotionContext.class,0);
		}
		public DesireAditionContext desireAdition() {
			return getRuleContext(DesireAditionContext.class,0);
		}
		public InternalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_internalOperator; }
	}

	public final InternalOperatorContext internalOperator() throws RecognitionException {
		InternalOperatorContext _localctx = new InternalOperatorContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_internalOperator);
		try {
			setState(318);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,26,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(314);
				beliefAdition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(315);
				beliefRemotion();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(316);
				desireAdition();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(317);
				desireAdition();
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

	public static class BeliefAditionContext extends ParserRuleContext {
		public BeliefAditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_beliefAdition; }
	}

	public final BeliefAditionContext beliefAdition() throws RecognitionException {
		BeliefAditionContext _localctx = new BeliefAditionContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_beliefAdition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			match(T__16);
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

	public static class BeliefRemotionContext extends ParserRuleContext {
		public BeliefRemotionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_beliefRemotion; }
	}

	public final BeliefRemotionContext beliefRemotion() throws RecognitionException {
		BeliefRemotionContext _localctx = new BeliefRemotionContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_beliefRemotion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(322);
			match(T__17);
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

	public static class DesireAditionContext extends ParserRuleContext {
		public DesireAditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_desireAdition; }
	}

	public final DesireAditionContext desireAdition() throws RecognitionException {
		DesireAditionContext _localctx = new DesireAditionContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_desireAdition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(324);
			match(T__18);
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

	public static class DesireRemotionContext extends ParserRuleContext {
		public DesireRemotionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_desireRemotion; }
	}

	public final DesireRemotionContext desireRemotion() throws RecognitionException {
		DesireRemotionContext _localctx = new DesireRemotionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_desireRemotion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(326);
			match(T__19);
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

	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(328);
			expression();
			setState(333);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__9) {
				{
				{
				setState(329);
				match(T__9);
				setState(330);
				expression();
				}
				}
				setState(335);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class ExpressionContext extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public TerminalNode VARIABLE() { return getToken(AgentParser.VARIABLE, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_expression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(336);
			_la = _input.LA(1);
			if ( !(_la==CONSTANT || _la==VARIABLE) ) {
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

	public static class CompoundActionContext extends ParserRuleContext {
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public CompoundActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundAction; }
	}

	public final CompoundActionContext compoundAction() throws RecognitionException {
		CompoundActionContext _localctx = new CompoundActionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_compoundAction);
		int _la;
		try {
			setState(350);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(338);
				match(T__11);
				setState(339);
				action();
				setState(344);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__9) {
					{
					{
					setState(340);
					match(T__9);
					setState(341);
					action();
					}
					}
					setState(346);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(347);
				match(T__12);
				}
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 2);
				{
				setState(349);
				match(T__10);
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

	public static class PlansFormulasContext extends ParserRuleContext {
		public List<PlanContext> plan() {
			return getRuleContexts(PlanContext.class);
		}
		public PlanContext plan(int i) {
			return getRuleContext(PlanContext.class,i);
		}
		public List<ActionContext> action() {
			return getRuleContexts(ActionContext.class);
		}
		public ActionContext action(int i) {
			return getRuleContext(ActionContext.class,i);
		}
		public PlansFormulasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_plansFormulas; }
	}

	public final PlansFormulasContext plansFormulas() throws RecognitionException {
		PlansFormulasContext _localctx = new PlansFormulasContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_plansFormulas);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__8 || _la==T__13) {
				{
				{
				setState(354);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case T__8:
					{
					setState(352);
					plan();
					}
					break;
				case T__13:
					{
					setState(353);
					action();
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				}
				}
				setState(360);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class ContextNameContext extends ParserRuleContext {
		public LogicalContextNameContext logicalContextName() {
			return getRuleContext(LogicalContextNameContext.class,0);
		}
		public ContextNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextName; }
	}

	public final ContextNameContext contextName() throws RecognitionException {
		ContextNameContext _localctx = new ContextNameContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_contextName);
		try {
			setState(364);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__5:
			case T__6:
			case T__7:
			case CUSTOMLOGICALNAME:
				enterOuterAlt(_localctx, 1);
				{
				setState(361);
				logicalContextName();
				}
				break;
			case T__4:
				enterOuterAlt(_localctx, 2);
				{
				setState(362);
				match(T__4);
				}
				break;
			case T__3:
				enterOuterAlt(_localctx, 3);
				{
				setState(363);
				match(T__3);
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

	public static class HeadContext extends ParserRuleContext {
		public ContextNameContext contextName() {
			return getRuleContext(ContextNameContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode VARIABLE() { return getToken(AgentParser.VARIABLE, 0); }
		public List<NegationContext> negation() {
			return getRuleContexts(NegationContext.class);
		}
		public NegationContext negation(int i) {
			return getRuleContext(NegationContext.class,i);
		}
		public HeadContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_head; }
	}

	public final HeadContext head() throws RecognitionException {
		HeadContext _localctx = new HeadContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_head);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			match(T__20);
			setState(368);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25 || _la==T__26) {
				{
				setState(367);
				negation();
				}
			}

			setState(370);
			contextName();
			setState(376);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,35,_ctx) ) {
			case 1:
				{
				setState(371);
				term(0);
				}
				break;
			case 2:
				{
				setState(373);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25 || _la==T__26) {
					{
					setState(372);
					negation();
					}
				}

				setState(375);
				match(VARIABLE);
				}
				break;
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

	public static class BodyContext extends ParserRuleContext {
		public ContextNameContext contextName() {
			return getRuleContext(ContextNameContext.class,0);
		}
		public BodyTermContext bodyTerm() {
			return getRuleContext(BodyTermContext.class,0);
		}
		public OtherBodyRulesContext otherBodyRules() {
			return getRuleContext(OtherBodyRulesContext.class,0);
		}
		public NegationContext negation() {
			return getRuleContext(NegationContext.class,0);
		}
		public BodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_body; }
	}

	public final BodyContext body() throws RecognitionException {
		BodyContext _localctx = new BodyContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_body);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(379);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25 || _la==T__26) {
				{
				setState(378);
				negation();
				}
			}

			setState(381);
			contextName();
			setState(382);
			bodyTerm();
			}
			setState(385);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AND || _la==OR) {
				{
				setState(384);
				otherBodyRules();
				}
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

	public static class OtherBodyRulesContext extends ParserRuleContext {
		public List<ContextNameContext> contextName() {
			return getRuleContexts(ContextNameContext.class);
		}
		public ContextNameContext contextName(int i) {
			return getRuleContext(ContextNameContext.class,i);
		}
		public List<BodyTermContext> bodyTerm() {
			return getRuleContexts(BodyTermContext.class);
		}
		public BodyTermContext bodyTerm(int i) {
			return getRuleContext(BodyTermContext.class,i);
		}
		public List<LogicalOperatorContext> logicalOperator() {
			return getRuleContexts(LogicalOperatorContext.class);
		}
		public LogicalOperatorContext logicalOperator(int i) {
			return getRuleContext(LogicalOperatorContext.class,i);
		}
		public List<NegationContext> negation() {
			return getRuleContexts(NegationContext.class);
		}
		public NegationContext negation(int i) {
			return getRuleContext(NegationContext.class,i);
		}
		public OtherBodyRulesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_otherBodyRules; }
	}

	public final OtherBodyRulesContext otherBodyRules() throws RecognitionException {
		OtherBodyRulesContext _localctx = new OtherBodyRulesContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_otherBodyRules);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(394); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				{
				setState(387);
				logicalOperator();
				}
				setState(389);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25 || _la==T__26) {
					{
					setState(388);
					negation();
					}
				}

				setState(391);
				contextName();
				setState(392);
				bodyTerm();
				}
				}
				setState(396); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==AND || _la==OR );
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

	public static class BodyTermContext extends ParserRuleContext {
		public PlanContext plan() {
			return getRuleContext(PlanContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public TerminalNode VARIABLE() { return getToken(AgentParser.VARIABLE, 0); }
		public NegationContext negation() {
			return getRuleContext(NegationContext.class,0);
		}
		public BodyTermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bodyTerm; }
	}

	public final BodyTermContext bodyTerm() throws RecognitionException {
		BodyTermContext _localctx = new BodyTermContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_bodyTerm);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(406);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
			case T__25:
			case T__26:
			case CONSTANT:
			case VARIABLE:
				{
				setState(403);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,41,_ctx) ) {
				case 1:
					{
					setState(398);
					term(0);
					}
					break;
				case 2:
					{
					setState(400);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==T__25 || _la==T__26) {
						{
						setState(399);
						negation();
						}
					}

					setState(402);
					match(VARIABLE);
					}
					break;
				}
				}
				break;
			case T__8:
				{
				setState(405);
				plan();
				}
				break;
			default:
				throw new NoViableAltException(this);
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

	public static class LogicalOperatorContext extends ParserRuleContext {
		public TerminalNode AND() { return getToken(AgentParser.AND, 0); }
		public TerminalNode OR() { return getToken(AgentParser.OR, 0); }
		public LogicalOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOperator; }
	}

	public final LogicalOperatorContext logicalOperator() throws RecognitionException {
		LogicalOperatorContext _localctx = new LogicalOperatorContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_logicalOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(408);
			_la = _input.LA(1);
			if ( !(_la==AND || _la==OR) ) {
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

	public static class TermContext extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public NegationContext negation() {
			return getRuleContext(NegationContext.class,0);
		}
		public AnnotationContext annotation() {
			return getRuleContext(AnnotationContext.class,0);
		}
		public TerminalNode LeftParen() { return getToken(AgentParser.LeftParen, 0); }
		public List<AtomContext> atom() {
			return getRuleContexts(AtomContext.class);
		}
		public AtomContext atom(int i) {
			return getRuleContext(AtomContext.class,i);
		}
		public TerminalNode RightParen() { return getToken(AgentParser.RightParen, 0); }
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public TerminalNode AND() { return getToken(AgentParser.AND, 0); }
		public TerminalNode OR() { return getToken(AgentParser.OR, 0); }
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 96;
		enterRecursionRule(_localctx, 96, RULE_term, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(443);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
			case CONSTANT:
				{
				setState(412);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==T__25 || _la==T__26) {
					{
					setState(411);
					negation();
					}
				}

				setState(414);
				match(CONSTANT);
				setState(430);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,46,_ctx) ) {
				case 1:
					{
					setState(415);
					annotation();
					}
					break;
				case 2:
					{
					{
					setState(416);
					match(LeftParen);
					setState(417);
					atom();
					setState(422);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__9) {
						{
						{
						setState(418);
						match(T__9);
						setState(419);
						atom();
						}
						}
						setState(424);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(425);
					match(RightParen);
					}
					setState(428);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
					case 1:
						{
						setState(427);
						annotation();
						}
						break;
					}
					}
					break;
				}
				}
				break;
			case T__11:
				{
				{
				setState(432);
				match(T__11);
				setState(433);
				term(0);
				setState(438);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__9) {
					{
					{
					setState(434);
					match(T__9);
					setState(435);
					term(0);
					}
					}
					setState(440);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(441);
				match(T__12);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(453);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(451);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,49,_ctx) ) {
					case 1:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(445);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(446);
						_la = _input.LA(1);
						if ( !(_la==AND || _la==OR) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(447);
						term(4);
						}
						break;
					case 2:
						{
						_localctx = new TermContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(448);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(449);
						match(T__0);
						setState(450);
						term(2);
						}
						break;
					}
					} 
				}
				setState(455);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,50,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Term2Context extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public NegationContext negation() {
			return getRuleContext(NegationContext.class,0);
		}
		public Term2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term2; }
	}

	public final Term2Context term2() throws RecognitionException {
		Term2Context _localctx = new Term2Context(_ctx, getState());
		enterRule(_localctx, 98, RULE_term2);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(457);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__25 || _la==T__26) {
				{
				setState(456);
				negation();
				}
			}

			setState(459);
			match(CONSTANT);
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

	public static class FormulasContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public FormulasContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formulas; }
	}

	public final FormulasContext formulas() throws RecognitionException {
		FormulasContext _localctx = new FormulasContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_formulas);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(466);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__11) | (1L << T__25) | (1L << T__26) | (1L << CONSTANT))) != 0)) {
				{
				{
				setState(461);
				term(0);
				setState(462);
				match(T__1);
				}
				}
				setState(468);
				_errHandler.sync(this);
				_la = _input.LA(1);
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

	public static class AtomContext extends ParserRuleContext {
		public List<TerminalNode> NUMERAL() { return getTokens(AgentParser.NUMERAL); }
		public TerminalNode NUMERAL(int i) {
			return getToken(AgentParser.NUMERAL, i);
		}
		public List<TerminalNode> CONSTANT() { return getTokens(AgentParser.CONSTANT); }
		public TerminalNode CONSTANT(int i) {
			return getToken(AgentParser.CONSTANT, i);
		}
		public List<TerminalNode> VARIABLE() { return getTokens(AgentParser.VARIABLE); }
		public TerminalNode VARIABLE(int i) {
			return getToken(AgentParser.VARIABLE, i);
		}
		public OperatorContext operator() {
			return getRuleContext(OperatorContext.class,0);
		}
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_atom);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(469);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << NUMERAL) | (1L << CONSTANT) | (1L << VARIABLE))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24))) != 0)) {
				{
				setState(470);
				operator();
				setState(471);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__10) | (1L << NUMERAL) | (1L << CONSTANT) | (1L << VARIABLE))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
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

	public static class OperatorContext extends ParserRuleContext {
		public OperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operator; }
	}

	public final OperatorContext operator() throws RecognitionException {
		OperatorContext _localctx = new OperatorContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(475);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__16) | (1L << T__17) | (1L << T__21) | (1L << T__22) | (1L << T__23) | (1L << T__24))) != 0)) ) {
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

	public static class NegationContext extends ParserRuleContext {
		public NegationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_negation; }
	}

	public final NegationContext negation() throws RecognitionException {
		NegationContext _localctx = new NegationContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_negation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(477);
			_la = _input.LA(1);
			if ( !(_la==T__25 || _la==T__26) ) {
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

	public static class AnnotationContext extends ParserRuleContext {
		public PreActionContext preAction() {
			return getRuleContext(PreActionContext.class,0);
		}
		public GradedValueContext gradedValue() {
			return getRuleContext(GradedValueContext.class,0);
		}
		public AnnotationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_annotation; }
	}

	public final AnnotationContext annotation() throws RecognitionException {
		AnnotationContext _localctx = new AnnotationContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_annotation);
		try {
			setState(484);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(479);
				preAction();
				setState(481);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
				case 1:
					{
					setState(480);
					gradedValue();
					}
					break;
				}
				}
				}
				break;
			case T__27:
				enterOuterAlt(_localctx, 2);
				{
				setState(483);
				gradedValue();
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

	public static class PreActionContext extends ParserRuleContext {
		public TerminalNode CONSTANT() { return getToken(AgentParser.CONSTANT, 0); }
		public PreActionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preAction; }
	}

	public final PreActionContext preAction() throws RecognitionException {
		PreActionContext _localctx = new PreActionContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_preAction);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(486);
			match(T__11);
			setState(487);
			match(CONSTANT);
			setState(488);
			match(T__12);
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

	public static class GradedValueContext extends ParserRuleContext {
		public TerminalNode NUMERAL() { return getToken(AgentParser.NUMERAL, 0); }
		public GradedValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_gradedValue; }
	}

	public final GradedValueContext gradedValue() throws RecognitionException {
		GradedValueContext _localctx = new GradedValueContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_gradedValue);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(490);
			match(T__27);
			setState(491);
			match(NUMERAL);
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

	public static class CostContext extends ParserRuleContext {
		public TerminalNode NUMERAL() { return getToken(AgentParser.NUMERAL, 0); }
		public CostContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cost; }
	}

	public final CostContext cost() throws RecognitionException {
		CostContext _localctx = new CostContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_cost);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(493);
			match(T__28);
			setState(494);
			match(NUMERAL);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 48:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,\u01f3\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4"+
		",\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t"+
		"\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t;\3\2\3\2\3\2"+
		"\7\2z\n\2\f\2\16\2}\13\2\3\2\3\2\3\3\3\3\5\3\u0083\n\3\3\4\3\4\3\4\3\4"+
		"\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u0091\n\6\3\7\3\7\3\7\3\7\6\7\u0097"+
		"\n\7\r\7\16\7\u0098\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\5\n\u00a3\n\n\3\13"+
		"\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5\r\u00b2\n\r\3\r\3"+
		"\r\5\r\u00b6\n\r\3\r\3\r\5\r\u00ba\n\r\3\r\3\r\3\r\3\16\3\16\3\17\3\17"+
		"\3\17\3\17\3\17\5\17\u00c6\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u00cd\n"+
		"\20\3\21\6\21\u00d0\n\21\r\21\16\21\u00d1\3\22\3\22\3\22\3\22\5\22\u00d8"+
		"\n\22\3\23\5\23\u00db\n\23\3\23\3\23\3\23\3\23\3\23\3\23\7\23\u00e3\n"+
		"\23\f\23\16\23\u00e6\13\23\3\23\3\23\3\23\5\23\u00eb\n\23\5\23\u00ed\n"+
		"\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00f5\n\23\3\24\3\24\3\25\3\25"+
		"\5\25\u00fb\n\25\3\26\3\26\5\26\u00ff\n\26\3\27\3\27\5\27\u0103\n\27\3"+
		"\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u010c\n\30\3\30\3\30\5\30\u0110"+
		"\n\30\3\30\3\30\5\30\u0114\n\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33"+
		"\3\33\5\33\u011f\n\33\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35"+
		"\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3\"\3\"\3"+
		"#\3#\3#\3#\5#\u0141\n#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\7(\u014e\n("+
		"\f(\16(\u0151\13(\3)\3)\3*\3*\3*\3*\7*\u0159\n*\f*\16*\u015c\13*\3*\3"+
		"*\3*\5*\u0161\n*\3+\3+\5+\u0165\n+\7+\u0167\n+\f+\16+\u016a\13+\3,\3,"+
		"\3,\5,\u016f\n,\3-\3-\5-\u0173\n-\3-\3-\3-\5-\u0178\n-\3-\5-\u017b\n-"+
		"\3.\5.\u017e\n.\3.\3.\3.\3.\5.\u0184\n.\3/\3/\5/\u0188\n/\3/\3/\3/\6/"+
		"\u018d\n/\r/\16/\u018e\3\60\3\60\5\60\u0193\n\60\3\60\5\60\u0196\n\60"+
		"\3\60\5\60\u0199\n\60\3\61\3\61\3\62\3\62\5\62\u019f\n\62\3\62\3\62\3"+
		"\62\3\62\3\62\3\62\7\62\u01a7\n\62\f\62\16\62\u01aa\13\62\3\62\3\62\3"+
		"\62\5\62\u01af\n\62\5\62\u01b1\n\62\3\62\3\62\3\62\3\62\7\62\u01b7\n\62"+
		"\f\62\16\62\u01ba\13\62\3\62\3\62\5\62\u01be\n\62\3\62\3\62\3\62\3\62"+
		"\3\62\3\62\7\62\u01c6\n\62\f\62\16\62\u01c9\13\62\3\63\5\63\u01cc\n\63"+
		"\3\63\3\63\3\64\3\64\3\64\7\64\u01d3\n\64\f\64\16\64\u01d6\13\64\3\65"+
		"\3\65\3\65\3\65\5\65\u01dc\n\65\3\66\3\66\3\67\3\67\38\38\58\u01e4\n8"+
		"\38\58\u01e7\n8\39\39\39\39\3:\3:\3:\3;\3;\3;\3;\2\3b<\2\4\6\b\n\f\16"+
		"\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd"+
		"fhjlnprt\2\t\3\2\b\n\4\2\3\3%&\3\2#$\3\2%&\4\2\r\r\"$\4\2\23\24\30\33"+
		"\3\2\34\35\2\u01f6\2v\3\2\2\2\4\u0082\3\2\2\2\6\u0084\3\2\2\2\b\u0089"+
		"\3\2\2\2\n\u0090\3\2\2\2\f\u0092\3\2\2\2\16\u009a\3\2\2\2\20\u009e\3\2"+
		"\2\2\22\u00a2\3\2\2\2\24\u00a4\3\2\2\2\26\u00a6\3\2\2\2\30\u00a8\3\2\2"+
		"\2\32\u00be\3\2\2\2\34\u00c5\3\2\2\2\36\u00cc\3\2\2\2 \u00cf\3\2\2\2\""+
		"\u00d3\3\2\2\2$\u00f4\3\2\2\2&\u00f6\3\2\2\2(\u00fa\3\2\2\2*\u00fe\3\2"+
		"\2\2,\u0102\3\2\2\2.\u0104\3\2\2\2\60\u0117\3\2\2\2\62\u0119\3\2\2\2\64"+
		"\u011b\3\2\2\2\66\u0122\3\2\2\28\u0124\3\2\2\2:\u012c\3\2\2\2<\u012e\3"+
		"\2\2\2>\u0130\3\2\2\2@\u0138\3\2\2\2B\u013a\3\2\2\2D\u0140\3\2\2\2F\u0142"+
		"\3\2\2\2H\u0144\3\2\2\2J\u0146\3\2\2\2L\u0148\3\2\2\2N\u014a\3\2\2\2P"+
		"\u0152\3\2\2\2R\u0160\3\2\2\2T\u0168\3\2\2\2V\u016e\3\2\2\2X\u0170\3\2"+
		"\2\2Z\u017d\3\2\2\2\\\u018c\3\2\2\2^\u0198\3\2\2\2`\u019a\3\2\2\2b\u01bd"+
		"\3\2\2\2d\u01cb\3\2\2\2f\u01d4\3\2\2\2h\u01d7\3\2\2\2j\u01dd\3\2\2\2l"+
		"\u01df\3\2\2\2n\u01e6\3\2\2\2p\u01e8\3\2\2\2r\u01ec\3\2\2\2t\u01ef\3\2"+
		"\2\2v{\5\f\7\2wz\5\4\3\2xz\5\6\4\2yw\3\2\2\2yx\3\2\2\2z}\3\2\2\2{y\3\2"+
		"\2\2{|\3\2\2\2|~\3\2\2\2}{\3\2\2\2~\177\7\2\2\3\177\3\3\2\2\2\u0080\u0083"+
		"\5\b\5\2\u0081\u0083\5\n\6\2\u0082\u0080\3\2\2\2\u0082\u0081\3\2\2\2\u0083"+
		"\5\3\2\2\2\u0084\u0085\5X-\2\u0085\u0086\7\3\2\2\u0086\u0087\5Z.\2\u0087"+
		"\u0088\7\4\2\2\u0088\7\3\2\2\2\u0089\u008a\5\22\n\2\u008a\u008b\7\5\2"+
		"\2\u008b\u008c\5f\64\2\u008c\t\3\2\2\2\u008d\u0091\5\f\7\2\u008e\u0091"+
		"\5\16\b\2\u008f\u0091\5\20\t\2\u0090\u008d\3\2\2\2\u0090\u008e\3\2\2\2"+
		"\u0090\u008f\3\2\2\2\u0091\13\3\2\2\2\u0092\u0093\7\6\2\2\u0093\u0096"+
		"\7\5\2\2\u0094\u0097\58\35\2\u0095\u0097\5> \2\u0096\u0094\3\2\2\2\u0096"+
		"\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2"+
		"\2\2\u0099\r\3\2\2\2\u009a\u009b\7\7\2\2\u009b\u009c\7\5\2\2\u009c\u009d"+
		"\5T+\2\u009d\17\3\2\2\2\u009e\u009f\7!\2\2\u009f\21\3\2\2\2\u00a0\u00a3"+
		"\5\24\13\2\u00a1\u00a3\5\26\f\2\u00a2\u00a0\3\2\2\2\u00a2\u00a1\3\2\2"+
		"\2\u00a3\23\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5\25\3\2\2\2\u00a6\u00a7\7"+
		" \2\2\u00a7\27\3\2\2\2\u00a8\u00a9\7\13\2\2\u00a9\u00aa\7\'\2\2\u00aa"+
		"\u00ab\5\32\16\2\u00ab\u00ac\7\f\2\2\u00ac\u00b5\5R*\2\u00ad\u00ae\7\f"+
		"\2\2\u00ae\u00af\5\34\17\2\u00af\u00b1\7\f\2\2\u00b0\u00b2\5D#\2\u00b1"+
		"\u00b0\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\3\2\2\2\u00b3\u00b4\5\36"+
		"\20\2\u00b4\u00b6\3\2\2\2\u00b5\u00ad\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6"+
		"\u00b9\3\2\2\2\u00b7\u00b8\7\f\2\2\u00b8\u00ba\5t;\2\u00b9\u00b7\3\2\2"+
		"\2\u00b9\u00ba\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\7(\2\2\u00bc\u00bd"+
		"\7\4\2\2\u00bd\31\3\2\2\2\u00be\u00bf\5b\62\2\u00bf\33\3\2\2\2\u00c0\u00c6"+
		"\7\r\2\2\u00c1\u00c2\7\16\2\2\u00c2\u00c3\5 \21\2\u00c3\u00c4\7\17\2\2"+
		"\u00c4\u00c6\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c6\35"+
		"\3\2\2\2\u00c7\u00cd\7\r\2\2\u00c8\u00c9\7\16\2\2\u00c9\u00ca\5 \21\2"+
		"\u00ca\u00cb\7\17\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00c7\3\2\2\2\u00cc\u00c8"+
		"\3\2\2\2\u00cd\37\3\2\2\2\u00ce\u00d0\5\"\22\2\u00cf\u00ce\3\2\2\2\u00d0"+
		"\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2!\3\2\2\2"+
		"\u00d3\u00d4\5(\25\2\u00d4\u00d5\7\5\2\2\u00d5\u00d7\5$\23\2\u00d6\u00d8"+
		"\7\f\2\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8#\3\2\2\2\u00d9"+
		"\u00db\5l\67\2\u00da\u00d9\3\2\2\2\u00da\u00db\3\2\2\2\u00db\u00dc\3\2"+
		"\2\2\u00dc\u00ec\7#\2\2\u00dd\u00ed\5n8\2\u00de\u00df\7\'\2\2\u00df\u00e4"+
		"\5h\65\2\u00e0\u00e1\7\f\2\2\u00e1\u00e3\5h\65\2\u00e2\u00e0\3\2\2\2\u00e3"+
		"\u00e6\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3\2"+
		"\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\7(\2\2\u00e8\u00ea\3\2\2\2\u00e9"+
		"\u00eb\5n8\2\u00ea\u00e9\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed\3\2\2"+
		"\2\u00ec\u00dd\3\2\2\2\u00ec\u00de\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00f5"+
		"\3\2\2\2\u00ee\u00ef\7\'\2\2\u00ef\u00f0\5$\23\2\u00f0\u00f1\t\3\2\2\u00f1"+
		"\u00f2\5$\23\2\u00f2\u00f3\7(\2\2\u00f3\u00f5\3\2\2\2\u00f4\u00da\3\2"+
		"\2\2\u00f4\u00ee\3\2\2\2\u00f5%\3\2\2\2\u00f6\u00f7\5*\26\2\u00f7\'\3"+
		"\2\2\2\u00f8\u00fb\5\24\13\2\u00f9\u00fb\5\26\f\2\u00fa\u00f8\3\2\2\2"+
		"\u00fa\u00f9\3\2\2\2\u00fb)\3\2\2\2\u00fc\u00ff\7\r\2\2\u00fd\u00ff\5"+
		"b\62\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff+\3\2\2\2\u0100\u0103"+
		"\7\r\2\2\u0101\u0103\5d\63\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103"+
		"-\3\2\2\2\u0104\u0105\7\20\2\2\u0105\u0106\7\'\2\2\u0106\u010f\5\64\33"+
		"\2\u0107\u0108\7\f\2\2\u0108\u0109\5\60\31\2\u0109\u010b\7\f\2\2\u010a"+
		"\u010c\5D#\2\u010b\u010a\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2"+
		"\2\u010d\u010e\5\62\32\2\u010e\u0110\3\2\2\2\u010f\u0107\3\2\2\2\u010f"+
		"\u0110\3\2\2\2\u0110\u0113\3\2\2\2\u0111\u0112\7\f\2\2\u0112\u0114\5t"+
		";\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0115\3\2\2\2\u0115"+
		"\u0116\7(\2\2\u0116/\3\2\2\2\u0117\u0118\5*\26\2\u0118\61\3\2\2\2\u0119"+
		"\u011a\5*\26\2\u011a\63\3\2\2\2\u011b\u011c\5\66\34\2\u011c\u011e\7\'"+
		"\2\2\u011d\u011f\5N(\2\u011e\u011d\3\2\2\2\u011e\u011f\3\2\2\2\u011f\u0120"+
		"\3\2\2\2\u0120\u0121\7(\2\2\u0121\65\3\2\2\2\u0122\u0123\7#\2\2\u0123"+
		"\67\3\2\2\2\u0124\u0125\7\21\2\2\u0125\u0126\7\'\2\2\u0126\u0127\5:\36"+
		"\2\u0127\u0128\7\f\2\2\u0128\u0129\5<\37\2\u0129\u012a\7(\2\2\u012a\u012b"+
		"\7\4\2\2\u012b9\3\2\2\2\u012c\u012d\7)\2\2\u012d;\3\2\2\2\u012e\u012f"+
		"\7)\2\2\u012f=\3\2\2\2\u0130\u0131\7\22\2\2\u0131\u0132\7\'\2\2\u0132"+
		"\u0133\5@!\2\u0133\u0134\7\f\2\2\u0134\u0135\5B\"\2\u0135\u0136\7(\2\2"+
		"\u0136\u0137\7\4\2\2\u0137?\3\2\2\2\u0138\u0139\7)\2\2\u0139A\3\2\2\2"+
		"\u013a\u013b\7)\2\2\u013bC\3\2\2\2\u013c\u0141\5F$\2\u013d\u0141\5H%\2"+
		"\u013e\u0141\5J&\2\u013f\u0141\5J&\2\u0140\u013c\3\2\2\2\u0140\u013d\3"+
		"\2\2\2\u0140\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141E\3\2\2\2\u0142\u0143"+
		"\7\23\2\2\u0143G\3\2\2\2\u0144\u0145\7\24\2\2\u0145I\3\2\2\2\u0146\u0147"+
		"\7\25\2\2\u0147K\3\2\2\2\u0148\u0149\7\26\2\2\u0149M\3\2\2\2\u014a\u014f"+
		"\5P)\2\u014b\u014c\7\f\2\2\u014c\u014e\5P)\2\u014d\u014b\3\2\2\2\u014e"+
		"\u0151\3\2\2\2\u014f\u014d\3\2\2\2\u014f\u0150\3\2\2\2\u0150O\3\2\2\2"+
		"\u0151\u014f\3\2\2\2\u0152\u0153\t\4\2\2\u0153Q\3\2\2\2\u0154\u0155\7"+
		"\16\2\2\u0155\u015a\5.\30\2\u0156\u0157\7\f\2\2\u0157\u0159\5.\30\2\u0158"+
		"\u0156\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2"+
		"\2\2\u015b\u015d\3\2\2\2\u015c\u015a\3\2\2\2\u015d\u015e\7\17\2\2\u015e"+
		"\u0161\3\2\2\2\u015f\u0161\7\r\2\2\u0160\u0154\3\2\2\2\u0160\u015f\3\2"+
		"\2\2\u0161S\3\2\2\2\u0162\u0165\5\30\r\2\u0163\u0165\5.\30\2\u0164\u0162"+
		"\3\2\2\2\u0164\u0163\3\2\2\2\u0165\u0167\3\2\2\2\u0166\u0164\3\2\2\2\u0167"+
		"\u016a\3\2\2\2\u0168\u0166\3\2\2\2\u0168\u0169\3\2\2\2\u0169U\3\2\2\2"+
		"\u016a\u0168\3\2\2\2\u016b\u016f\5\22\n\2\u016c\u016f\7\7\2\2\u016d\u016f"+
		"\7\6\2\2\u016e\u016b\3\2\2\2\u016e\u016c\3\2\2\2\u016e\u016d\3\2\2\2\u016f"+
		"W\3\2\2\2\u0170\u0172\7\27\2\2\u0171\u0173\5l\67\2\u0172\u0171\3\2\2\2"+
		"\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u017a\5V,\2\u0175\u017b"+
		"\5b\62\2\u0176\u0178\5l\67\2\u0177\u0176\3\2\2\2\u0177\u0178\3\2\2\2\u0178"+
		"\u0179\3\2\2\2\u0179\u017b\7$\2\2\u017a\u0175\3\2\2\2\u017a\u0177\3\2"+
		"\2\2\u017bY\3\2\2\2\u017c\u017e\5l\67\2\u017d\u017c\3\2\2\2\u017d\u017e"+
		"\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0180\5V,\2\u0180\u0181\5^\60\2\u0181"+
		"\u0183\3\2\2\2\u0182\u0184\5\\/\2\u0183\u0182\3\2\2\2\u0183\u0184\3\2"+
		"\2\2\u0184[\3\2\2\2\u0185\u0187\5`\61\2\u0186\u0188\5l\67\2\u0187\u0186"+
		"\3\2\2\2\u0187\u0188\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\5V,\2\u018a"+
		"\u018b\5^\60\2\u018b\u018d\3\2\2\2\u018c\u0185\3\2\2\2\u018d\u018e\3\2"+
		"\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f]\3\2\2\2\u0190\u0196"+
		"\5b\62\2\u0191\u0193\5l\67\2\u0192\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193"+
		"\u0194\3\2\2\2\u0194\u0196\7$\2\2\u0195\u0190\3\2\2\2\u0195\u0192\3\2"+
		"\2\2\u0196\u0199\3\2\2\2\u0197\u0199\5\30\r\2\u0198\u0195\3\2\2\2\u0198"+
		"\u0197\3\2\2\2\u0199_\3\2\2\2\u019a\u019b\t\5\2\2\u019ba\3\2\2\2\u019c"+
		"\u019e\b\62\1\2\u019d\u019f\5l\67\2\u019e\u019d\3\2\2\2\u019e\u019f\3"+
		"\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01b0\7#\2\2\u01a1\u01b1\5n8\2\u01a2"+
		"\u01a3\7\'\2\2\u01a3\u01a8\5h\65\2\u01a4\u01a5\7\f\2\2\u01a5\u01a7\5h"+
		"\65\2\u01a6\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8"+
		"\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ac\7("+
		"\2\2\u01ac\u01ae\3\2\2\2\u01ad\u01af\5n8\2\u01ae\u01ad\3\2\2\2\u01ae\u01af"+
		"\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01a1\3\2\2\2\u01b0\u01a2\3\2\2\2\u01b0"+
		"\u01b1\3\2\2\2\u01b1\u01be\3\2\2\2\u01b2\u01b3\7\16\2\2\u01b3\u01b8\5"+
		"b\62\2\u01b4\u01b5\7\f\2\2\u01b5\u01b7\5b\62\2\u01b6\u01b4\3\2\2\2\u01b7"+
		"\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2"+
		"\2\2\u01ba\u01b8\3\2\2\2\u01bb\u01bc\7\17\2\2\u01bc\u01be\3\2\2\2\u01bd"+
		"\u019c\3\2\2\2\u01bd\u01b2\3\2\2\2\u01be\u01c7\3\2\2\2\u01bf\u01c0\f\5"+
		"\2\2\u01c0\u01c1\t\5\2\2\u01c1\u01c6\5b\62\6\u01c2\u01c3\f\3\2\2\u01c3"+
		"\u01c4\7\3\2\2\u01c4\u01c6\5b\62\4\u01c5\u01bf\3\2\2\2\u01c5\u01c2\3\2"+
		"\2\2\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8"+
		"c\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01cc\5l\67\2\u01cb\u01ca\3\2\2\2"+
		"\u01cb\u01cc\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\7#\2\2\u01cee\3\2"+
		"\2\2\u01cf\u01d0\5b\62\2\u01d0\u01d1\7\4\2\2\u01d1\u01d3\3\2\2\2\u01d2"+
		"\u01cf\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2"+
		"\2\2\u01d5g\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01db\t\6\2\2\u01d8\u01d9"+
		"\5j\66\2\u01d9\u01da\t\6\2\2\u01da\u01dc\3\2\2\2\u01db\u01d8\3\2\2\2\u01db"+
		"\u01dc\3\2\2\2\u01dci\3\2\2\2\u01dd\u01de\t\7\2\2\u01dek\3\2\2\2\u01df"+
		"\u01e0\t\b\2\2\u01e0m\3\2\2\2\u01e1\u01e3\5p9\2\u01e2\u01e4\5r:\2\u01e3"+
		"\u01e2\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e7\5r"+
		":\2\u01e6\u01e1\3\2\2\2\u01e6\u01e5\3\2\2\2\u01e7o\3\2\2\2\u01e8\u01e9"+
		"\7\16\2\2\u01e9\u01ea\7#\2\2\u01ea\u01eb\7\17\2\2\u01ebq\3\2\2\2\u01ec"+
		"\u01ed\7\36\2\2\u01ed\u01ee\7\"\2\2\u01ees\3\2\2\2\u01ef\u01f0\7\37\2"+
		"\2\u01f0\u01f1\7\"\2\2\u01f1u\3\2\2\2:y{\u0082\u0090\u0096\u0098\u00a2"+
		"\u00b1\u00b5\u00b9\u00c5\u00cc\u00d1\u00d7\u00da\u00e4\u00ea\u00ec\u00f4"+
		"\u00fa\u00fe\u0102\u010b\u010f\u0113\u011e\u0140\u014f\u015a\u0160\u0164"+
		"\u0168\u016e\u0172\u0177\u017a\u017d\u0183\u0187\u018e\u0192\u0195\u0198"+
		"\u019e\u01a8\u01ae\u01b0\u01b8\u01bd\u01c5\u01c7\u01cb\u01d4\u01db\u01e3"+
		"\u01e6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}