from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}


@app.get('/hello/{name}')
async def read_hello(name: str):
    return {"message": f"Hello {name}"}
