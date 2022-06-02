from mcs.contexts.ctx_service import ContextService
import torch
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


class AATCtx(ContextService):

    _instance = None
    avg_salary = 0.0
    # Load model
    model = torch.jit.load('sigon/regressorv1-f.pt')

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

    def __new__(cls):
        cls.model.eval()
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def verify(self, fact):  # Checks the detected avg_salary

        return [{fact: self.avg_salary}]

    @classmethod
    def append_fact(self, fact) -> bool:
        self.check_keys(fact)
        self.data.update(fact)
        # get dummy data
        df_dum = pd.get_dummies(self.data)
        X = df_dum.drop('avg_salary', axis=1)
        X_torch = torch.tensor(np.array(X), dtype=torch.float)
        avg_salary_result = self.model.forward(X_torch)
        print(self.model.forward(X_torch))
        self.avg_salary = avg_salary_result[0]
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

