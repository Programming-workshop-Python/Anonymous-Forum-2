from flask import request
from main import app
from src.app_bundle.controllers.api.v1.post_controller import PostController as PostApiControllerV1
from src.app_bundle.entities.post import Post
from src.app_bundle.helpers.adapters.request_entity.post.collection.posts_adapter import PostsAdapter
from src.app_bundle.helpers.adapters.request_entity.post.post_adapter import PostAdapter
from src.app_bundle.helpers.builders.post.post_builder import PostBuilder
from src.app_bundle.repositories.post_repository import PostRepository
from src.app_bundle.services.crud.post_service import PostService
from src.app_bundle.services.validators.entity.post_validator import PostValidator

# API VERSION #1
# POSTS
post_adapter = PostAdapter()
post_api_controller_v1 = PostApiControllerV1(
    PostService(
        PostRepository(Post()),
        PostBuilder(),
        PostValidator()
    ),
    post_adapter
    ,
    PostsAdapter(post_adapter)
)


@app.route("/api/v1/posts/all", methods=['GET'])
def posts_all_v1():
    return post_api_controller_v1.get_all()


@app.route("/api/v1/posts/get", methods=['GET'])
def post_get_v1():
    return post_api_controller_v1.get(request)


@app.route("/api/v1/posts/create", methods=['POST'])
def post_create_v1():
    return post_api_controller_v1.create(request)


@app.route("/api/v1/posts/delete", methods=['DELETE'])
def post_delete_v1():
    return post_api_controller_v1.delete(request)


@app.route("/api/v1/posts/update", methods=['PUT'])
def post_update_v1():
    return post_api_controller_v1.update(request)
