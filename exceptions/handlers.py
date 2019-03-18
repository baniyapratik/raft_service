from raft_service.ext.api import APIResponse, APIErrorMsg

HTTP_CODE_MAP = {
    400: 'bad_request',
    401: 'unauthorized',
    403: 'forbidden',
    404: 'not_found',
    405: 'method_not_allowed',
    500: 'internal_server_error'
}


def http_exc_handler(exc):
    error_type = HTTP_CODE_MAP[exc.code]
    error = APIErrorMsg(error_type=error_type)
    return APIResponse(status=exc.code, error=error)