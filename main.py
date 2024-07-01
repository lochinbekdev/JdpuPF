from app import JdpuPF
from middleware import Middleware

app = JdpuPF()

@app.route('/home',allowed_methods=["get"])
def home(request,response):
    if request.method == "GET":
        response.text = "Hello from the Home Page"
    else:
        response.status.code = 405
        response.text = "Method not allowed"


@app.route("/hello/{name}")
def greeting(request, response ,name):
    response.text = f"Hello , {name} :)"
    
@app.route("/books")
class Books:
    def get(self,request, response):
        response.text = "Books page"

    def post(self,request, response):
        response.text = "Endpoint to create a book"
        

def new_handler(req,resp):
    resp.text = "From new handler"
        
    app.add_route("/new-handler",new_handler)
    
def on_exception(req,resp,exc):
    resp.text = str(exc)
    
    
app.add_exception_handler(on_exception)

@app.route("/exception")
def exception_throwing_handler(req,resp):
    raise AttributeError("Some exception")

class LoggingMiddleware(Middleware):
    
    def __init__(self, app):
        super().__init__(app)
        
    def process_request(self, req):
        print("request is beign called")
        
    def process_response(self, req, resp):
        print("response has been generate")
        
app.add_middleware(LoggingMiddleware)