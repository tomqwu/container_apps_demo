from fastapi import FastAPI, HTTPException
import httpx
import os
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

DAPR_HTTP_PORT = os.getenv("DAPR_HTTP_PORT", "3500")
BACKEND_APP_ID = os.getenv("BACKEND_APP_ID", "backend")

@app.get("/create-order")
async def create_order():
    payload = {"order_id": 123, "item": "Widget", "quantity": 2}
    dapr_url = f"http://localhost:{DAPR_HTTP_PORT}/v1.0/invoke/{BACKEND_APP_ID}/method/orders"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(dapr_url, json=payload)
            response.raise_for_status()
            backend_response = response.json()
            logging.info(f"Backend response via Dapr: {backend_response}")
            return {
                "message": backend_response.get("message", "Order processed successfully"),
                "data": backend_response.get("data", payload)
            }
    except httpx.HTTPStatusError as e:
        logging.error(f"Backend returned an error via Dapr: {e.response.text}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Backend returned an error via Dapr: {e.response.text}"
        )
    except httpx.RequestError as e:
        logging.error(f"Error calling backend via Dapr: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error calling backend via Dapr: {str(e)}"
        )

@app.get("/")
async def check_backend():
    dapr_url = f"http://localhost:{DAPR_HTTP_PORT}/v1.0/invoke/{BACKEND_APP_ID}/method/api/v1/example"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(dapr_url)
            response.raise_for_status()
            backend_response = response.json()
            return {"message": backend_response.get("message", "Backend check successful")}
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Backend returned an error via Dapr: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calling backend via Dapr: {str(e)}"
        )
