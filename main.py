from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1, 
        "author": "John Cena",
        "title": "First Post", 
        "content": "You can't see me."
    },
    {"id": 2, "author": "Randy Orton", "title": "Second Post", "content": "Watch out! RKO out of nowhere!"},
    {"id": 3, "author": "Dwayne Johnson", "title": "Third Post", "content": "The Rock."}
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False, name="posts")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home"})

@app.get("/api/posts")
def get_posts():
    return posts
