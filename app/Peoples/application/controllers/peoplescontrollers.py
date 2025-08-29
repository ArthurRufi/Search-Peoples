from fastapi import APIRouter

routerpeoples =  APIRouter(prefix="/peoples", tags=["peoples"])


@routerpeoples.get("/calculate_success_rate/")
async def get_tax(id: int):
#criar rota para calcular a taxa de sucesso
    # passar o id para as funcoes necessarias
    
    return {"message": "Peoples route"}

@routerpeoples.get("/vizualizer/")
#adicoonar o recebimento para a rota
async def view_all_information_for_context(id: int):
    return {"message": "Confirm person route"}


