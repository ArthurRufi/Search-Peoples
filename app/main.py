from fastapi import FastAPI
from Peoples.application.controllers.peoplescontrollers import *

app = FastAPI()
app.include_router(routerpeoples)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

#criar rota master para peoples e dentro de peoples criar rota para as funcionalidades
@app.get("/peoples")
async def read_peoples():
    return {"message": "Peoples route"} 