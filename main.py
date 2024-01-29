from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


# basic endpoint to get root
@app.get('/')
def index():
    return {'message': 'Hello World'}


# Adding query parameters.(Things not in path=== query parameters)
# Also adding default values by using '='
# Adding optional parameters byu using Optional [datatype]

# @app.get('/blog/all')
# def get_all_blogs(page=1,page_size=10):
#  return f'all {page_size} pages on page {page}'

@app.get('/blog/all')
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'page{page} page size={page_size}'}


# Add a enum Class to restrict user inputs
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_from_type(type: BlogType):
    return {'message': f'BlogType: {BlogType[type].value}'}


@app.get('/blog/{id}')
def get_blog(id: int):
    return {'blog': f"Blog no {id}"}
