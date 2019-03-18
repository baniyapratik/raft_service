from raft_service.exceptions.handlers import http_exc_handler
def init_exc_handlers(app):
    # http exceptions
    app.errorhandler(400)(http_exc_handler)
    app.errorhandler(401)(http_exc_handler)
    app.errorhandler(404)(http_exc_handler)
    app.errorhandler(405)(http_exc_handler)
    app.errorhandler(500)(http_exc_handler)