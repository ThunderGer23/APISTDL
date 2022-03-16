from fastapi import APIRouter

dni = APIRouter()

@dni.get('/dates')
def get_dates():
    return "Lista la ruta :v"