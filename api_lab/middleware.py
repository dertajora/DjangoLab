from .core import Logging as log_api
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # get current path url
        current_path = request.get_full_path()

        # get method of request
        method = request.method

        # get value sent in parameter post
        message = request.POST['message']

        # save log from middleware
        log_middleware = [current_path, method, message]
        log_api.save_log_middleware(log_middleware)

        response = get_response(request)



        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware