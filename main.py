
from fastapi import FastAPI

from routes import router

app = FastAPI()

app.include_router(router, prefix='')


# ---------------- examples ----------------------#

# @app.get("/") ## Maneira de buscar o header
# def read_root(user_agent: Optional[str] = Header(None)):
#     return {"user-agent": user_agent}

# @app.get("/cookie") ## Maneira de trabalhar com cookie /salvado no cliente
# def cookie(response:Response): ## key and value são parametros
#     response.set_cookie(key='mine', value='BRL')
#     return {'cookie':True}

# ## maneira de recuperar o cookie armaz. no nav P/ numa response
# @app.get("/get_cookie") 
# def get_cookie(mine:Optional[str] = Cookie(None)):
#   return {"Cookie":mine}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, p:bool, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q, "p": p} 

# @app.post("/item")
# def add_item(item:Item, item2:Item):
#   return [item, item2]

# #verificar valor no stock
# # @app.get("/items/valor_total")
# # def get_valor_total():
# #   #pythonica P/ resolver o problema
# #   v_total = sum([item.value * item.quantidade for item in banco_de_dados])

#   # for item in banco_de_dados:
#   #   v_total+= item.value * item.quantidade

#   return {"valor_total": v_total}
