from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

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
