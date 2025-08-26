from fastapi import APIRouter

routerpeoples =  APIRouter(prefix="/peoples", tags=["peoples"])


@routerpeoples.get("/calculate_success_rate/")
async def read_peoples():
    #criar rota para calcular a taxa de sucesso
    return {"message": "Peoples route"}