from fastapi import FastAPI

import api.ejemplo.endpoints
import api.ejemplo2.endpoints


app = FastAPI()

prefix_base = "/api/v1"
app.include_router(api.ejemplo.endpoints.router, prefix=f"{prefix_base}/ejemplo")
app.include_router(api.ejemplo2.endpoints.router, prefix=f"{prefix_base}/ejemplo2")
