from fastapi import FastAPI, HTTPException
import httpx
import os
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:4000")

@app.get("/create-order")
async def create_order():
    payload = {"order_id": 123, "item": "Widget", "quantity": 2}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BACKEND_URL}/orders", json=payload)
            response.raise_for_status()
            backend_response = response.json()
            logging.info(f"Backend response: {backend_response}")
            return {
                "message": backend_response.get("message", "Order processed successfully"),
                "data": backend_response.get("data", payload)
            }
    except httpx.HTTPStatusError as e:
        logging.error(f"Backend returned an error: {e.response.text}")
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Backend returned an error: {e.response.text}"
        )
    except httpx.RequestError as e:
        logging.error(f"Error calling backend: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error calling backend: {str(e)}"
        )

@app.get("/")
async def check_backend():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{BACKEND_URL}/api/v1/example")
            response.raise_for_status()
            backend_response = response.json()
            return {"message": backend_response.get("message", "Backend check successful")}
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Backend returned an error: {e.response.text}"
        )
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calling backend: {str(e)}"
        )
