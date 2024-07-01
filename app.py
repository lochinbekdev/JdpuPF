from webob import Request, Response
from parse import parse
import  wsgiadapter
import requests
import inspect
from jinja2 import Environment,FileSystemLoader
import os

class JdpuPF:

    def __init__(self,template_dir="templates"):
        self.routes=dict()
        
        self.template_env = Environment(
            loader=FileSystemLoader(os.path.abspath(template_dir))
        )

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
           
    def add_route(self,path,handler):
        assert path not in self.routes, "Duplicate route. Pleace change the URL."     
        self.routes[path] = handler
    
    def route(self,path):
        def wrapper(handler):
            self.add_route(path,handler)
            return handler
        return wrapper
    
    def test_session(self):
        session=requests.Session()
        session.mount('http://testserver', wsgiadapter.WSGIAdapter(self))
        return session
    
    def template(self,template_name,context=None):
        if context is None:
            context = {}
            
        return self.template_env.get_template(template_name).render(**context).encode()