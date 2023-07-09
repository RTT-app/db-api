from flask import request, jsonify

from app import app, spec

from flask_pydantic_spec import (Response, Request)
from app.schemas.post_schema import Post_DTO, Post_list_DTO
from app.models.post import Post


@app.post('/add_post')
@spec.validate(body=Request(Post_DTO), resp=Response(HTTP_201=Post_DTO), tags=["post"])
def add_post():
    """
    Add post to bd.
    """
    title = request.json['title']
    self_text = request.json['self_text']
    comment = request.json['comment']
    score = request.json['score']
    
    post = Post.query.filter_by(email=email).first()

    if not contractor:
    
        new_contractor = Contractor(
            name = name,
            surname = surname,
            email = email,
            password = password,
        )

        db.session.add(new_contractor)
        db.session.commit()

        new_contractor_ = Contractor.query.filter_by(email=email).first()
        new_contractor_dto = translate_contractor_to_contractorDTO(new_contractor_).dict()
        
        return jsonify(new_contractor_dto), 201    
    
    else:

        return jsonify({'message': 'This email is already registered.'}), 409
    

@app.get('/contractors/<int:id>')
@spec.validate(resp=Response(HTTP_200=ContractorGetDTO), tags=["contractor"])
def get_contractor(comment):
    """
    Get contractor route.
    - get contractor by id.
    """

    post = Post.objects(comment=comment)

    if post: #check if contractor was found
        #contractor_dto = translate_contractor_to_contractorGetDTO(contractor).dict()
        return jsonify(post), 200
    
    else:
        return jsonify({'message': 'Contractor not found'}), 404
    

@app.get('/posts')
@spec.validate(resp=Response(HTTP_200=Post_list_DTO), tags=["contractor"])
def get_all_posts():
    """
    List all contractors.
    """
    posts = Post.objects()
    
    return jsonify(posts), 200