from app import app, spec
from flask import request, jsonify
from flask_pydantic_spec import (Response, Request)

from app.models.post import Post
from app.schemas.post_schema import Post_DTO, Post_list_DTO
from app.schemas.utils import translate_to_postsDTO


@app.post('/add-post')
@spec.validate(body=Request(Post_DTO), resp=Response(HTTP_201=Post_DTO), tags=["Post"])
def add_post():
    """
    - ADD post to bd.
    """
    title = request.json.get('title')
    self_text = request.json.get('self_text')
    comment = request.json.get('comment')
    score = request.json.get('score')

    post = Post.objects(comment=comment)

    if post:
        return jsonify({'message': 'Comment already exists.'}), 400    
    
    post = Post(title=title, self_text=self_text, comment=comment, score=score)
    
    post.save()
    
    resp = post.to_mongo().to_dict()
    resp.pop('_id')
    
    return jsonify(resp), 201


@app.get('/get-post/<string:comment>')
@spec.validate(resp=Response(HTTP_200=Post_DTO), tags=["Post"])
def get_post(comment):
    """
    - GET post by comment.
    """
    try:
        post = Post.objects.get(comment=comment)
        resp = post.to_mongo().to_dict()
        resp.pop('_id')

        return jsonify(resp), 200
    
    except:
        return jsonify({'message': 'post not found'}), 404
    

@app.get('/get-posts')
@spec.validate(resp=Response(HTTP_200=Post_list_DTO), tags=["Post"])
def get_all_posts():
    """
    - GET all posts.
    """
    posts = Post.objects().all()
    
    postsDTO = translate_to_postsDTO(posts)
    
    return jsonify(postsDTO.dict()), 200


@app.delete('/delete-posts/<string:comment>')
@spec.validate(tags=["Post"])
def delete_post(comment):
    """
    - DELETE post by comment.
    """
    try:
        post = Post.objects(comment=comment).first()
        print(post)
        post.delete()

        return jsonify({'message': 'post was deleted.'}), 204
    
    except:
        return jsonify({'message': 'post not found'}), 404

@app.delete('/delete-posts')
@spec.validate(resp=Response(HTTP_200=Post_list_DTO), tags=["Post"])
def delete_all_posts():
    """
    - DELETE alls posts.
    """
    posts = Post.objects().all()
    posts.delete()

    return jsonify({'message': 'all posts was deleted.'}), 204