from fastapi import FastAPI
from starlette.responses import RedirectResponse
from routes import book_routes

app = FastAPI()

app.include_router(book_routes.route)

@app.get('/')
def home():
    res = RedirectResponse(url='/docs')
    return res