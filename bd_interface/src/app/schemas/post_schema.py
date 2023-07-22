from pydantic import BaseModel

class Post_DTO(BaseModel):
    title: str
    self_text: str
    comment: str
    score: int

class Post_list_DTO(BaseModel):
    posts: list[Post_DTO]
    quantity: int