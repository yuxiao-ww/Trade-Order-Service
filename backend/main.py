from fastapi import FastAPI, WebSocket
from .routes import router as order_router
from .websocket import router as websocket_router


app = FastAPI(title="Trade Order Service", description="FastAPI Trading API with WebSocket")

app.include_router(order_router)
app.include_router(websocket_router)


# 直接注册 WebSocket 端点
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Received: {data}")
    except:
        await websocket.close()
