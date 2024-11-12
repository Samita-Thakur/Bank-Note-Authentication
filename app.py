import uvicorn
from fastapi import FastAPI
from Banknotes import Banknotes
import pickle
import numpy as np
import pandas as pd

app = FastAPI()
pickle_in=open("classifier.pkl", "rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name:str):
    return{'Welcome to False note detector':f'{name}'}

@app.post('/predcit')
def predict_banknote(data:Banknotes):
    data=data.dic()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']

    prediction=classifier.predict([[variance, skewness, curtosis, entropy]])

    if (prediction[0]>0.5):
        prediction="Fake Note"
    else:
        prediction="Authentic note"
    return {
        'prediction':prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

