import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


@app.get('/')
def hello_world():
    return { 'message': 'hello' }

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("index.html", {"request": request, "id": thisdict})

if __name__ == '__main__':
    uvicorn.run(app)