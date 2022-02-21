import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return 'Hello, world!'


uvicorn.run(app)
