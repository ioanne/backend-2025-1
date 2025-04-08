from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Página de home 2!"}


@app.post("/")
def process_home():
    return {"message": "Procesando pagina de home!"}


@app.patch("/")
def patch_home():
    return {"message": "Modificación parcial de pagina de home!"}


@app.put("/")
def put_home():
    return {"message": "Modificación total de pagina de home!"}


@app.delete("/")
def delete_home():
    return {"message": "Eliminando de la pagina de home!"}
