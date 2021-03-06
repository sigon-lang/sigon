from pyswip.prolog import PrologError
from pyswip import *


class PrologService():
    # __instance = BeliefsContextService how can i do this?
    prolog = Prolog()

    def verify_terms(facts):
        try:
            query_result = PrologService.prolog.query(facts, catcherrors=True)
            return list(query_result)
        except PrologError as e:
            print('Error while querying base', facts)
            print(e)
            return []

    def verify_body_terms(facts):
        try:
            query_result = PrologService.prolog.query(facts, catcherrors=True)
            return bool(list(query_result))
        except PrologError as e:
            print('Error while querying base', facts)
            print(e)
            return False

    def verify(fact, module):
        try:
            query_result = PrologService.prolog.query(
                PrologService.set_context(fact, module), catcherrors=True)
            return bool(list(query_result))

        except PrologError as e:
            print('Error while querying base', fact, module)
            print(e)
            return False

    def verify_custom(fact, module):
        try:
            query_result = PrologService.prolog.query(
                PrologService.set_context(fact, module), catcherrors=True)
            return list(query_result)

        except PrologError as e:
            # print('Error while querying base', fact, module)
            # print(e)
            return False

    def retract(fact, module):
        currentFact = fact
        if fact.startswith('-'):
            currentFact = fact.replace('-', '')
            PrologService.prolog.retract(PrologService.set_context(
                currentFact, module), catcherrors=True)
        return

    def append_fact(fact, module):
        try:
            PrologService.prolog.assertz(
                PrologService.set_context(fact, module), catcherrors=True)
            # TODO: check how it is done in java
        except:
            print("An error occurred while adding the following fact: " + fact)
            #raise Exception("Incorrect format while adding fact: "+ fact)

    def append_facts(facts, module):
        for f in facts:
            print('Adding fact', f)  # adding context on ...
            PrologService.prolog.appendFact(f, module)
        # TODO: verificar exception

    def set_context(fact, ctx):
        terms = fact.split(':-')
        if len(terms) > 1:
            head = terms[0].join([ctx+'(', ')'])
            body = terms[1].join([ctx+'(', ')'])
            return (head + ":-" + body)
        return fact.join([ctx+'(', ')'])

    # def addInitialFact(fact, module):
    #     PrologService.prolog.assertz(fact)
