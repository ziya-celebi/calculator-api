from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculate")
async def calculate(request: Request):
    data = await request.json()
    try:
        result = eval(data["expression"].replace('×', '*').replace('÷', '/'))
        return {"result": str(result)}
    except:
        return {"result": "Error"}