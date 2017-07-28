from .core import Logging as log_api
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # handle logging middleware before request processed
        # get current path url
        current_path = request.get_full_path()

        # get method of request
        method = request.method

        # Get value sent in parameter post
        # when we only need 1 param
        # data_received = request.POST['message']
        # when we need all param
        data_received = str(request.POST.dict())

        # save log from middleware
        param_request = [current_path, method, data_received]
        log_api.save_log_middleware_before(param_request)

        response = get_response(request)

        # handle logging middleware after request processed and response will be done
        data_sent = str(response.data)
        param_response = [current_path, method, data_sent]
        log_api.save_log_middleware_after(param_response)


        # Code to be executed for each request/response after
        # the view is called.

        return response


    return middleware