from fastapi import FastAPI
from service.planner import plan_transport
app = FastAPI()
@app.get("/health")
def root(): return {"status": "ok"}
@app.post("/decision")
def solve(data: dict): return plan_transport(data.get("prediction", 0))
