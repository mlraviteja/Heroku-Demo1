# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 16:22:24 2020

@author: admin
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'speed':33, 'ram':2, 'screen':14,'yes':0})

print(r.json())