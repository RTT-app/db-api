from app.models.post import Post
from app.schemas.post_schema import Post_list_DTO

def translate_to_postsDTO(post_list):
    postsDTO = Post_list_DTO(posts=[],quantity=0)

    for post in post_list:
        post_dict = post.to_mongo().to_dict()
        post_dict.pop('_id')
        postsDTO.posts.append(post_dict)

    postsDTO.quantity = len(postsDTO.posts)

    return postsDTO
