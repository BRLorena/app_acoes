from fastapi.testclient import TestClient


# test obtem o clien do conftest e return None
def test_get_root(client: TestClient) -> None:
  response = client.get("/") # return 200
  body = response.json() # return um json
  assert response.status_code == 400
  assert body['mensagem'] == 'api de papeis'
