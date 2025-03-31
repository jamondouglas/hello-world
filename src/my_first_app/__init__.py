from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def homepage(request):
    return JSONResponse({"message": "Hello, Starlette with Poetry!"})

routes = [
    Route("/", endpoint=homepage)
]

app = Starlette(debug=True, routes=routes)

print(dir(app))
print(app.routes)