from mcs.contexts.ctx_service import ContextService
import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
import json
import math
import decimal


class NNCtx(ContextService):

    _instance = None    
    avg_salary = 0.0
    # Load model
    model = torch.jit.load('sigon/regressorv4-f.pt')
    with open('sigon/encoder', 'rb') as f:
            enc = pickle.load(f)
    
    data = {
        'Rating': 3.4,
        'Size': '10000+ employees',
        'Type of ownership': 'Other Organization',
        'Industry': 'Health Care Services & Hospitals',
        'Sector': 'Health Care',
        'Revenue': '$2 to $5 billion (USD)',
        'num_comp': 0,
        'hourly': 0,
        'employer_provided': 0,
        'job_state': 'MD',
        'same_state': 0,
        'age': 36,
        'python_yn': 1,
        'spark': 0,
        'aws': 0,
        'excel': 0,
        'job_simp': 'data scientist',
        'seniority': 'na'
    }
    @classmethod
    def __new__(cls):
        cls.model.eval()
        with open('sigon/encoder', 'rb') as f:
            cls.enc = pickle.load(f)
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact):  # Checks the detected avg_salary
        print(fact)
        if 'greater' in fact:
            value = fact[fact.find('(')+1:fact.rfind(')')]    
            result = float(self.avg_salary) - float(value)   
            if result > 0.0:       
                return [{fact: self.avg_salary}]            
        elif 'avgSalary' in fact:
            value = fact[fact.find('(')+1:fact.rfind(')')]    
            return [{fact: self.avg_salary}]   
        return []



    @classmethod
    def append_fact(self, fact) -> bool:
        fact = json.loads(fact)
        self.check_keys(fact)
        self.data.update(fact)  
        entry = pd.DataFrame([self.data])
        encoded_entry = self.enc.transform(entry).toarray()

        entry_torch = torch.tensor(np.array(encoded_entry), dtype=torch.float)
        formated_entry = torch.tensor(np.array(entry_torch), dtype = torch.float)
        self.avg_salary = self.model.forward(formated_entry).item()*1000
        
        return True

    @classmethod
    def add_initial_fact(self, fact) -> bool:
        return True

    @classmethod
    def check_keys(self, fact):
        keys_to_remove = []
        for key in fact.keys():
            if key not in self.data:
                keys_to_remove.append(key)
                
        for key in keys_to_remove:
            del fact[key]                

