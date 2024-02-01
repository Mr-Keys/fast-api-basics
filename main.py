from fastapi import FastAPI
from routers import blog_get,blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


# basic endpoint to get root
@app.get('/')
def index():
    return {'message': 'Hello World'}

