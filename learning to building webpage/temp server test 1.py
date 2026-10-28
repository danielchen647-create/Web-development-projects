from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 1. Configure CORS to protect your server

# app.add_middleware(
#     CORSMiddleware,
#     # In production, replace "*" with your actual frontend URL (e.g., ["https://myfrontend.com"])
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# 2. Create the endpoint
@app.get("/api/test-connection")
async def test_connection():
    return {"message": "Success! The backend hears you loud and clear."}
