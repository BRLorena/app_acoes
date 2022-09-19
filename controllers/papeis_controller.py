from fastapi import APIRouter  # Cookie, FastAPI, Header, Response
from models.papel import Papel

router = APIRouter() # Criar rotas com a notation APIRouter


@router.post("/")
async def add_item(papel: Papel):
  await papel.save()
  return papel

@router.get("/")
async def list_item():
  return await Papel.objects.all()
