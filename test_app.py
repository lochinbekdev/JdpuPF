import pytest

def test_basic_route_adding(app):
    @app.route("/home")
    def home(req,resp):
        resp.text = "Hello from home Page" 
        
        
def test_dublicate_routes_throws_exception(app):
    @app.route("/home")
    def home(req,resp):
        resp.text = "Hello from home Page" 
    
    with pytest.raises(AssertionError):
        @app.route("/home")
        def home2(req,resp):
            resp.text = "Hello from home2 Page" 
            
def test_requests_can_be_sent_by_test_client(app,test_client):
    @app.route("/home")
    def home(req,resp):
        resp.text = "Hello from home Page"
        
    response = test_client.get('http://testserver/home')
    
    assert response.text == "Hello from home Page"
    
    
def test_parameterized_routing(app,test_client):
    @app.route("/hello/{name}")
    def greeting(request, response ,name):
        response.text = f"Hello {name} :)"
        
    assert test_client.get("http://testserver/hello/Lochinbek").text == "Hello Lochinbek :)"
    assert test_client.get('http://testserver/hello/Matthew').text == "Hello Matthew :)"
    

def test_default_response(test_client):
    response = test_client.get("http://testserver/nonexistent")
    
    assert response.text == "Sorry page not Found."
    assert response.status_code == 404
    
def test_class_based_get(app,test_client):
    @app.route("/books")
    class Books:
        def get(self,req,resp):
            resp.text = "Books page"
            
    assert test_client.get("http://testserver/books").text == "Books page"
    
def test_class_based_post(app,test_client):
    @app.route("/books")
    class Books:
        def post(self,req,resp):
            resp.text = "Endpoint to create a book"
            
    assert test_client.post("http://testserver/books").text == "Endpoint to create a book"
    
    
def test_class_based_method_not_allowed(app,test_client):
    @app.route("/books")
    class Books:
        def post(self,req,resp):
            resp.text = "Endpoint to create a book"
            
    response = test_client.get("http://testserver/books")
    
    assert response.text == "Method Not Allowed"
    assert response.status_code == 405
    