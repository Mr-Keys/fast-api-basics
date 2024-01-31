from fastapi import FastAPI, status, Response
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

@app.get('/blog/all',tags=['blog'])
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'page{page} page size={page_size}'}


# combining path parameters with query parameters
@app.get('/blog/{id}/comments/{comment_id)',tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id{id},comment_id {comment_id}'}


# Add a enum Class to restrict user inputs
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}',tags=['blog'])
def get_blog_from_type(type: BlogType):
    return {'message': f'BlogType: {BlogType[type].value}'}


# adding status code
@app.get(
    '/blog/{id}', status_code=status.HTTP_404_NOT_FOUND,
    tags=['blog'],
    summary='Get a particular blog based on the blog id provided',
    description='From multiple blogs in a database get a particular blog based on the blog id',
    response_description='List of available vlogs'
)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'blog': f"Blog no {id}"}

#below is a more optimised way for the above method.
@app.get('/blogz/{id}',tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    else:
        return {'blog': f"Blog no {id}"}



#tags-used to define categories for different API calls
#summary-short description of what the API does and description-details about the API(long)
#can also use ''' some description here ''' inside a function declaration for description


#ROUTERS-separate operations into multiple files /share a prefix but perform multiple operations
