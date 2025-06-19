
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/parse-sentiment")
async def parse_sentiment(req: Request):
    body = await req.json()
    return {
        "token": body.get("token", "UNKNOWN"),
        "sentiment": "Bullish",
        "confidence_score": 88,
        "urgency_score": 7,
        "spike_status": True
    }

@app.post("/trade-dummy")
async def trade_dummy(req: Request):
    body = await req.json()
    token = body.get("token", "UNKNOWN")
    action = "BUY" if body.get("sentiment") == "Bullish" else "HOLD"
    return {
        "trade_token": token,
        "trade_action": action,
        "executed_price": "mock-$0.0031",
        "timestamp": "simulated",
        "status": "executed"
    }
