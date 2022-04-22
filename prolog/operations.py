from agent.context.ctx_service import ContextService
from pyswip import *


class Operations():

    
        
    def verify(functor_def, module):
        q = Query(functor_def, module=module)        
        if q.nextSolution():
            q.closeQuery()
            return True
        q.closeQuery()
        return False
        
        

    def retract(retract, functor_def, module):
        try:
            call(retract(functor_def), module=module)
        
        except:
            print("An error occurred while removing the following functor: ", functor_def)     
        

    def appendFact(assertz, functor_def, module):
        try:
            call(assertz(functor_def), module=module)
        except:            
            print("An error occurred while adding the following functor: ", functor_def)            
            #raise Exception("Incorrect format while adding fact: "+ fact)


    def appendFacts(assertz, functor_definitions, module):
        for f in functor_definitions:
            print('Adding functor', f) #adding context on ...
            Operations.appendFact(assertz, f, module)
        #TODO: verificar exception

   
    
   





