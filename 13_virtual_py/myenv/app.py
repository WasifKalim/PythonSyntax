from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {'data': 'welcome to home page'}

@app.get('/contact')
def contact():
    return {'data': 'welcome to contact page'}

import uvicorn
uvicorn.run(app)
