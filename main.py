from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

posts = [
    {
        "id": 1, 
        "title": "First Post", 
        "content": "This is the content of the first post."
    },
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."}
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def read_root(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts": posts, "title": "Home Page"})

@app.get("/api/posts")
def get_posts():
    return posts
