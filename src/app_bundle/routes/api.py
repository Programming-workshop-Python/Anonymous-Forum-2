from flask import request
from main import app
from src.app_bundle.controllers.api.v1.post_controller import PostController as PostApiControllerV1
from src.app_bundle.controllers.api.v1.thread_controller import ThreadController as ThreadControllerV1
from src.app_bundle.controllers.api.v1.board_controller import BoardController as BoardControllerV1
from src.app_bundle.entities.board import Board
from src.app_bundle.entities.post import Post
from src.app_bundle.entities.thread import Thread
from src.app_bundle.helpers.adapters.request_entity.board.board_adapter import BoardAdapter
from src.app_bundle.helpers.adapters.request_entity.board.collection.boards_adapter import BoardsAdapter
from src.app_bundle.helpers.adapters.request_entity.post.collection.posts_adapter import PostsAdapter
from src.app_bundle.helpers.adapters.request_entity.post.post_adapter import PostAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.collection.threads_adapter import ThreadsAdapter
from src.app_bundle.helpers.adapters.request_entity.thread.thread_adapter import ThreadAdapter
from src.app_bundle.helpers.builders.board.board_builder import BoardBuilder
from src.app_bundle.helpers.builders.post.post_builder import PostBuilder
from src.app_bundle.helpers.builders.thread.thread_builder import ThreadBuilder
from src.app_bundle.repositories.board_repository import BoardRepository
from src.app_bundle.repositories.post_repository import PostRepository
from src.app_bundle.repositories.thread_repository import ThreadRepository
from src.app_bundle.services.crud.board_service import BoardService
from src.app_bundle.services.crud.post_service import PostService
from src.app_bundle.services.crud.thread_service import ThreadService
from src.app_bundle.services.validators.entity.board_validator import BoardValidator
from src.app_bundle.services.validators.entity.post_validator import PostValidator
from src.app_bundle.services.validators.entity.thread_validator import ThreadValidator

# API VERSION #1
# POSTS
board_adapter = BoardAdapter()
board_service = BoardService(BoardRepository(Board()), BoardBuilder(), BoardValidator())
thread_adapter = ThreadAdapter(board_adapter)
thread_service = ThreadService(
    ThreadRepository(Thread()),
    ThreadBuilder(board_service),
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
    return post_api_controller_v1.get_posts_from_thread(request)


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


@app.route("/api/v1/threads/get_by_board", methods=['GET'])
def get_threads_from_board_v1():
    return thread_controller_v1.get_threads_from_board(request)


# BOARDS
board_controller_v1 = BoardControllerV1(
    board_service,
    board_adapter,
    BoardsAdapter(board_adapter)
)


@app.route("/api/v1/boards/all", methods=['GET'])
def boards_all_v1():
    return board_controller_v1.get_all()


@app.route("/api/v1/boards/get", methods=['GET'])
def boards_get_v1():
    return board_controller_v1.get(request)


@app.route("/api/v1/boards/create", methods=['POST'])
def boards_create_v1():
    return board_controller_v1.create(request)


@app.route("/api/v1/boards/delete", methods=['DELETE'])
def boards_delete_v1():
    return board_controller_v1.delete(request)


@app.route("/api/v1/boards/update", methods=['PUT'])
def boards_update_v1():
    return board_controller_v1.update(request)
