from fastapi import FastAPI
from apis.login import router as login_router
from apis.users import router as user_router
from apis.organisation import router as org_router
from apis.userorganization import router as userorg_router
from apis.website import router as web_router
from apis.project import router as project_router
from apis.projectwebsite import router as proweb_router
from apis.cronjob import router as cronjob_router
from apis.webstats import router as webstats_router
from apis.statsrequests import router as stats_router
from models.users import Base
from base import engine
from apis.cronjob import start_job, scheduler
from contextlib import asynccontextmanager

app = FastAPI()

@asynccontextmanager
async def lifespan(_:FastAPI):
    start_job()
    yield
    scheduler.shutdown(wait = False)


Base.metadata.create_all(bind=engine)

app.include_router(login_router, prefix="/login", tags=["Login"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(org_router, prefix="/organisation", tags=["Organisation"])
app.include_router(userorg_router, prefix="/userorganisation", tags=["UserOrganisation"])
app.include_router(web_router, prefix="/website", tags=["Website"])
app.include_router(project_router, prefix="/project", tags=["Project"])
app.include_router(proweb_router, prefix="/projectwebsite", tags=["ProjectWebsite"])
app.include_router(cronjob_router, prefix="/cronjob", tags=["CronJob"])
app.include_router(webstats_router, prefix="/webstats", tags=["WebStats"])
app.include_router(stats_router, prefix="/statsrequests", tags=["LoadTesting"])

@app.middleware("http")
async def add_custom_header(request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "CustomValue"
    return response
