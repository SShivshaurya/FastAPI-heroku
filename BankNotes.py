# -*- coding: utf-8 -*-
"""
Created on Wed July 7 2021
@author: Saurabh Singh
"""

from pydantic import BaseModel
#2. Class which describes Bank Notes measurements
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float