from fastapi import FastAPI, Request, Response
import httpx
import os

app = FastAPI()
DAPR_HTTP_PORT = int(os.getenv("DAPR_HTTP_PORT", 3500))
BACKEND_APP_ID = "backend"

@app.post("/orders")
async def create_order(request: Request):
    body = await request.json()
    dapr_url = f"http://localhost:{DAPR_HTTP_PORT}/v1.0/invoke/{BACKEND_APP_ID}/method/createOrder"
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(dapr_url, json=body)
            return Response(content=resp.content, status_code=resp.status_code, media_type=resp.headers.get("content-type"))
        except Exception as e:
            return {"error": str(e)}
