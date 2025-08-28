from fastapi import APIRouter

routerpeoples =  APIRouter(prefix="/peoples", tags=["peoples"])


@routerpeoples.get("/calculate_success_rate/")
async def get_tax(id: int):
#criar rota para calcular a taxa de sucesso
    # passar o id para as funcoes necessarias
    
    return {"message": "Peoples route"}