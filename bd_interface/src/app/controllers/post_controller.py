from flask import request, jsonify

from app import app, spec

from flask_pydantic_spec import (Response, Request)
from app.schemas.post_schema import Post_DTO, Post_list_DTO
from app.models.post import Post


@app.post('/add-post')
@spec.validate(body=Request(Post_DTO), resp=Response(HTTP_201=Post_DTO), tags=["Post"])
def add_post():
    """
    - Add post to bd.
    """
    title = request.json.get('title')
    self_text = request.json.get('self_text')
    comment = request.json.get('comment')
    score = request.json.get('score')

    post = Post.objects(comment=comment)
    print(post)
    if post:
        return jsonify({'message': 'Comment already exists.'}), 400    
    
    post = Post(title=title, self_text=self_text, comment=comment, score=score)
    
    post.save()
    
    resp = post.to_mongo().to_dict()
    resp.pop('_id')
    
    return jsonify(resp), 201


@app.get('/post/<string:comment>')
@spec.validate(resp=Response(HTTP_200=Post_DTO), tags=["Post"])
def get_post(comment):
    """
    Get post by comment.
    """
    post = Post.objects.get(comment=comment)

    if post:
        return jsonify(post.to_mongo()), 200
    else:
        return jsonify({'message': 'post not found'}), 404
    

@app.get('/posts')
@spec.validate(resp=Response(HTTP_200=Post_list_DTO), tags=["Post"])
def get_all_posts():
    """
    List all posts.
    """
    posts = Post.objects()
    print(posts)
    return jsonify(posts.to_json()), 200