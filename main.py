import uvicorn
from fastapi import FastAPI

app=FastAPI()

@app.get('/')

def index():
    return {"message":"Hello, World!"}

@app.get('/welcome')

def get_name(name:str):
    return {'Welcome to False note detector':f'{name}'}
            

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
#uvicorn main:app --reload