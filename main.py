from fastapi import FastAPI

app = FastAPI()

db = []

@app.post("/api/{number_1}/{number_2}")
async def get_ibnfo(name: str,
                    l_name: str):
    n = name.lower()
    l = l_name.lower()
    db = {'name': n,
          "l_name": l}
    print(db)
    return {'name':n,
          "l_name":l}