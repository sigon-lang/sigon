grammar Agent;

agent
	:
	communicationContext (context | bridgeRule)*
	EOF
	;

context
	:
	logicalContext | functionalContext
	;

bridgeRule
	:
	head ':-' body '.'
	;

logicalContext
	:
	logicalContextName ':' formulas
	;

functionalContext
	:
	communicationContext |
	plannerContext |
	customFunctionalContext
	;

communicationContext:
	'communication' ':' (sensor | actuator)+
	;

plannerContext
	:
	'planner'  ':' plansFormulas
	;
customFunctionalContext
	:
	CUSTOMFUNCTIONALNAME
	;
	

logicalContextName
	: primitiveContextName
	| customLogicalContextName
	;

primitiveContextName
	: 'beliefs' | 'desires' | 'intentions'
	;

customLogicalContextName
	:
	CUSTOMLOGICALNAME
	;

CUSTOMLOGICALNAME :
	'_'  ALPHA CHARACTER*
;

CUSTOMFUNCTIONALNAME :
	'*'  ALPHA CHARACTER*
;
plan
	: 'plan' LeftParen somethingToBeTrue ',' compoundAction (',' preConditions ',' internalOperator? postConditions)? (',' cost)? RightParen '.'
	;



somethingToBeTrue
	: term
	;

/*planPreconditions
	: preConditions
	;*/
preConditions
	: '_' | '[' planConditions ']' //aqui nao sei se posso por apenas _ ou o [_], talvez fosse melhor por o [ ] so quando tivesse algo
	;

postConditions
	: '_' | '[' planConditions ']' //aqui nao sei se posso por apenas _ ou o [_], talvez fosse melhor por o [ ] so quando tivesse algo
	;

planConditions
	: condition+
;
condition
	: ( contextReference ':' conditionTerm ','?)
	;

conditionTerm
	:
	 negation? CONSTANT ( annotation | (LeftParen atom (',' atom )* RightParen) annotation?)?
	| LeftParen conditionTerm (AND | OR | ':-') conditionTerm RightParen	
	; //faz sentido eu poder usar SÓ OR e AND quando referenciar apenas um mesmo contexto?

planPostconditions
	:  conditions
	;

contextReference
	:
	(primitiveContextName | customLogicalContextName)
	;

conditions
	: ('_' | term)
	;



conditions1
	: ('_' | term2)
	;

action
	: 'action' LeftParen functionInvocation (',' actionPreconditions ',' internalOperator? actionPostconditions)? (',' cost)? RightParen
	;

actionPreconditions
	: conditions
	;

actionPostconditions
	: conditions
	;

functionInvocation
	: functionName LeftParen argumentList? RightParen
	;

functionName
	: CONSTANT
	;





sensor
    : 'sensor' LeftParen  sensorIdentifier  ',' sensorImplementation RightParen '.'
    ;


sensorIdentifier
    : STRING
    ;

sensorImplementation
    : STRING
    ;

actuator
    : 'actuator' LeftParen actuatorIdentifier ',' actuatorImplementation RightParen '.'
    ;


actuatorIdentifier
    : STRING
    ;

actuatorImplementation
    : STRING
    ;

internalOperator
	: beliefAdition | beliefRemotion | desireAdition | desireAdition
	;

beliefAdition
	: '+'
	;
beliefRemotion
	: '-'
	;

desireAdition
	: '+!'
	;
desireRemotion
	: '-!'
	;
argumentList
	:	expression (',' expression)*
;

expression
	: CONSTANT | VARIABLE
	;

compoundAction
	: ('[' action (',' action)* ']') |'_' ;





plansFormulas
	: ((plan  | action )) *
	;


contextName:
	logicalContextName | 'planner' | 'communication'
	;


head
	:
	'!' negation?  contextName (term | negation? VARIABLE)
	;

// body
// 	: negation? contextName ((term | negation? VARIABLE) | plan)
// ((AND | OR) negation?  contextName   ((term | negation? VARIABLE) | plan))*
// 	;


body
	:  (negation? contextName bodyTerm) (otherBodyRules)?
	;

otherBodyRules
	: ((logicalOperator) negation?  contextName   bodyTerm)+
	;
bodyTerm
	: ((term | negation? VARIABLE) | plan)
	;
logicalOperator
	:
	(AND | OR)
	;

term
	:  negation? CONSTANT ( annotation | (LeftParen atom (',' atom )* RightParen) annotation?)? 
	| term (AND | OR) term
	| ('[' term (',' term)* ']')
	| term ':-' term
	;

term2
	:  negation? CONSTANT
	;


formulas
	: (term '.' )*
	;




atom
    : (NUMERAL | CONSTANT | VARIABLE | '_') (operator (NUMERAL | CONSTANT | VARIABLE | '_') )?
    ;

operator
    : '<' | '=<' | '>' | '>=' | '-' | '+'
    ;

negation
	: 'not ' | '~';

annotation
     : (preAction gradedValue ? ) | gradedValue
     ;

preAction
    : '['CONSTANT']'
    ;

gradedValue
    : '->0.' NUMERAL
    ;
cost
    : '0.' NUMERAL
    ;
NUMERAL
	: DIGIT+
	;

CONSTANT
	: LCLETTER CHARACTER*
	;

VARIABLE
	: UCLETTER CHARACTER*
	;



/*
* TODO: user been able to add a semantic for a context.
*semanticRules
*	: (LCLETTER | UCLETTER) CHARACTER* '.semantic'
*	;
*/

AND
   : '&'
   ;

OR
   : '|'
   ;

LeftParen : '(';
RightParen : ')';

STRING
	:
    '"' (~["\\\r\n])* '"';





fragment ALPHA:
	LCLETTER | UCLETTER
	;




fragment CHARACTER
    : LCLETTER | UCLETTER | DIGIT
    ;

fragment LCLETTER
    : [a-z_];

fragment UCLETTER
    : [A-Z];

fragment DIGIT
    : [0-9];

WS
   : [ \t\r\n] -> skip
;


BlockComment
    : '/*' .*? '*/' -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
;
    