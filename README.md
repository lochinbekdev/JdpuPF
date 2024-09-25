# JdpuPF Python Freamwork ✨

[![License: MIT](https://img.shields.io/badge/license-MIT-C06524)](https://github.com/hynek/hatch-fancy-pypi-readme/blob/main/LICENSE.txt)
[![PyPI - Version](https://img.shields.io/pypi/v/hatch-fancy-pypi-readme.svg)](https://pypi-camo.freetls.fastly.net/bfea3a66d4f133c7c1319b08540fbd35125bec0a/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f70796672616d65757a)



### Installation

```toml
pip install JdpuPF
```


### How to use it


### Basic usage:


```toml
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
```



### Unit Tests

The recommended way of writing unit tests is with `pytest`. There are two built in fixtures that you may want to use when writing unit tests with JdpuPF. The first one is app which is an instance of the main API class:


```toml
def test_dublicate_routes_throws_exception(app):
    @app.route("/home")
    def home(req,resp):
        resp.text = "Hello from home Page" 
        assert resp.text == "Hello from home Page"    
    with pytest.raises(AssertionError):
        @app.route("/home")
        def home2(req,resp):
            resp.text = "Hello from home2 Page" 
```

The other one is `client` that you can use to send HTTP requests to your handlers. It is based on the famous `requests` and it should feel very familiar:

```toml
def test_parameterized_routing(app,test_client):
    @app.route("/hello/{name}")
    def greeting(request, response ,name):
        response.text = f"Hello {name} :)"
        
    assert test_client.get("http://testserver/hello/Lochinbek").text == "Hello Lochinbek :)"
    assert test_client.get('http://testserver/hello/Matthew').text == "Hello Matthew :)"
```

Thank you for Usage