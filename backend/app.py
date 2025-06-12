from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/orders")
async def create_order(request: Request):
    body = await request.json()
    return {"message": "Order created successfully", "data": body}

@app.get("/api/v1/example")
def example_endpoint():
    return {"message": "success"}
