import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from .api.main_router import router as router_main
from .core.config.setting import settings
from .core.config.exception_handler import CustomException, http_exception_handler
from .core.models.modal_base import Base
from .core.database.postgres import engine as engine_postgres, databaseBase as database_postgres
# from .core.config.event_app import event_start_app, event_close_app

Base.metadata.create_all(bind=engine_postgres)

app = FastAPI(
    title=settings.PROJECT_NAME
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
app.include_router(router_main, prefix=settings.API_PREFIX)
app.add_exception_handler(CustomException, http_exception_handler)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port='3337')