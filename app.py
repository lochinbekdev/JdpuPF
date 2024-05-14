from webob import Request, Response
from parse import parse
import inspect

class JdpuPF:

    def __init__(self):
        self.routes=dict()

    def __call__(self,environ,start_response):
        request = Request(environ)
        response=self.handle_request(request)
        return response(environ, start_response)

    def handle_request(self,request):
        response = Response()
        handler, kwargs = self.find_handler(request)

        if handler is not None:
            if inspect.isclass(handler):
                handler = getattr(handler(),request.method.lower(),None)

                if handler is None:
                    response.status_code = 405
                    response.text = "Method Not Allowed"
                    return response
                
            handler(request,response,**kwargs)
        else:
            self.deafult_response(response)
        return response

    def deafult_response(self,response):
        response.status_code = 404
        response.text = 'Sorry page not Found.'

    def find_handler(self,request):
        for path, handler in self.routes.items():
           paresed_result= parse(path,request.path)
           if paresed_result is not None:
               return handler, paresed_result.named
        return None, None
           
    def route(self,path):
        
        assert path not in self.routes, "Dublicate route. Pleace change the URL."
        
        def wrapper(handler):
            self.routes[path] = handler
            return handler
        return wrapper