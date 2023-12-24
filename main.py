from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/jaikumar")
async def jaiku():
    return {"message": "Hello it's jai"}
