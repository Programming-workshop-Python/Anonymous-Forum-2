from flask import request
from main import app
from src.app_bundle.controllers.api.v1.post_controller import PostController as PostApiControllerV1
from src.app_bundle.controllers.api.v1.thread_controller import ThreadController as ThreadControllerV1
from src.app_bundle.entities.post import Post
from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.adapters.request_entity.post.collection.posts_adapter import PostsAdapter
from src.app_bundle.helpers.adapters.request_entity.post.post_adapter import PostAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.collection.threads_adapter import ThreadsAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.thread_adapter import ThreadAdapter
from src.app_bundle.helpers.builders.post.post_builder import PostBuilder
from src.app_bundle.helpers.builders.thread.thread_builder import ThreadBuilder
from src.app_bundle.repositories.post_repository import PostRepository
from src.app_bundle.repositories.thread_repository import ThreadRepository
from src.app_bundle.services.crud.post_service import PostService
from src.app_bundle.services.crud.thread_service import ThreadService
from src.app_bundle.services.validators.entity.post_validator import PostValidator
from src.app_bundle.services.validators.entity.thread_validator import ThreadValidator

# API VERSION #1
# POSTS
thread_adapter = ThreadAdapter()
thread_service = ThreadService(
    ThreadRepository(Thread()),
    ThreadBuilder(),
    ThreadValidator()
)
post_adapter = PostAdapter(thread_adapter)
post_api_controller_v1 = PostApiControllerV1(
    PostService(
        PostRepository(Post()),
        PostBuilder(thread_service),
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


@app.route("/api/v1/posts/get_by_tread", methods=['GET'])
def get_posts_from_thread_v1():
    x = post_api_controller_v1.get_posts_from_thread(request)
    return x


@app.route("/api/v1/posts/create", methods=['POST'])
def post_create_v1():
    return post_api_controller_v1.create(request)


@app.route("/api/v1/posts/delete", methods=['DELETE'])
def post_delete_v1():
    return post_api_controller_v1.delete(request)


@app.route("/api/v1/posts/update", methods=['PUT'])
def post_update_v1():
    return post_api_controller_v1.update(request)


# THREADS
thread_controller_v1 = ThreadControllerV1(
    thread_service,
    thread_adapter,
    ThreadsAdapter(thread_adapter)
)


@app.route("/api/v1/threads/all", methods=['GET'])
def threads_all_v1():
    return thread_controller_v1.get_all()


@app.route("/api/v1/threads/get", methods=['GET'])
def threads_get_v1():
    return thread_controller_v1.get(request)


@app.route("/api/v1/threads/create", methods=['POST'])
def threads_create_v1():
    return thread_controller_v1.create(request)


@app.route("/api/v1/threads/delete", methods=['DELETE'])
def threads_delete_v1():
    return thread_controller_v1.delete(request)


@app.route("/api/v1/threads/update", methods=['PUT'])
def threads_update_v1():
    return thread_controller_v1.update(request)
