from fastapi import APIRouter, Query, Body
from pydantic import BaseModel
from typing import Optional, List

router = APIRouter(
    prefix='/blog',
    tags=['blog']
)


class BlogModel(BaseModel):
    title: int
    content: str
    no_of_comments: int
    published: Optional[bool] = False


# combining parameters
@router.post('/new/{id}')
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version

    }


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
                   comment_id: int = Query(None,
                                           title='comment id of the post',
                                           description='comment id is the id associated with each post',
                                           deprecated=True

                                           ), content: str = Body('Hii how are you', min_length=10, regex='^[a-z\s]*$'),
                   some_other_key: str = Body(...),
                   v: Optional[List[str]]= Query(None)
                   ):
    return {'data': f'id {id}'}
