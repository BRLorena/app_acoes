from fastapi import APIRouter

from controllers import papeis_controller as papeis

router = APIRouter()

# recebe como parametro um APIRouter() e o prefix que deve contrer na URL 
router.include_router(papeis.router, prefix='/papeis')
