from fastapi import FastAPI
from fastapi.responses import Response

from api.api_router import router as api_router

app = FastAPI()


@app.get("/healthcheck")
def health_check():
    return Response()


app.include_router(api_router)

for route in app.routes:
    print(route.methods.pop() + " " + route.path)
