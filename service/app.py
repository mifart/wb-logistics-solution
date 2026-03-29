from fastapi import FastAPI
from service.planner import plan_transport
app = FastAPI()
@app.get("/")
def home(): return {"message": "WB Logistics API is Live", "links": {"health": "/health", "decision": "/decision"}}
  
@app.get("/health")
def root(): return {"status": "ok"}
@app.post("/decision")
def solve(data: dict): return plan_transport(data.get("prediction", 0))
