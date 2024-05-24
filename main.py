from app import JdpuPF

app = JdpuPF()

@app.route('/home')
def home(request,response):
    response.text= "Hello from the Home Page"


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