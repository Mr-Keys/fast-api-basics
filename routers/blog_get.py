from fastapi import APIRouter,status,Response
from typing import Optional
from enum import Enum

router=APIRouter(
    prefix='/blog',
    tags=['blog']
)

@router.get('/all')
def get_all_blogs(page=1, page_size: Optional[int] = None):
    return {'message': f'page{page} page size={page_size}'}


# combining path parameters with query parameters
@router.get('/{id}/comments/{comment_id)',tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    return {'message': f'blog_id{id},comment_id {comment_id}'}


# Add a enum Class to restrict user inputs
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get('/type/{type}')
def get_blog_from_type(type: BlogType):
    return {'message': f'BlogType: {BlogType[type].value}'}


# adding status code
@router.get(
    '/{id}', status_code=status.HTTP_404_NOT_FOUND,
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
# @router.get('/blogz/{id}',tags=['blog'])
# def get_blog(id: int, response: Response):
#     if id > 5:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'error': f'Blog {id} not found'}
#     else:
#         return {'blog': f"Blog no {id}"}

