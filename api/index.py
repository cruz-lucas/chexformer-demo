from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/", StaticFiles(directory=".", html=True), name="static")


@app.get("/")
async def main():
    return {"message": "Hello asd"}


@app.get("/api/python")
async def main():
    return {"message": "Hello World"}
