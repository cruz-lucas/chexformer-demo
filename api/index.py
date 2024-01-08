from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


app = FastAPI()
app.mount("/", StaticFiles(directory=".", html=True), name="static")


@app.get("/")
async def main():
    return {"message": "Hello asd"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
