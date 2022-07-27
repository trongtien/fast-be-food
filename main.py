from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from app.configs.postgresql import SessionLocalPostgre
from app.api import router as api_router_admin


app = FastAPI()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    print("response", response)
    try:
        request.state.db = SessionLocalPostgre()
        response = await call_next(request)

        print("response", response)
    finally:
        request.state.db.close()
    return response
    
app.include_router(router=api_router_admin.router, prefix="/api")

@app.get("/", tags=["test"])
def index():
    return {"name": "First Data"}
