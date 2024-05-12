from app import JdpuPF

app = JdpuPF()

@app.route('/home')
def home(request,response):
    response.text= "Hello from the Home Page"


@app.route("/about")
def about(request,response):
    response.text= "Hello from the About Page"

@app.route("/ads")
def about(request,response):
    response.text= "Hello from the Ads Page"
    
@app.route("/news")
def news(request, response):
    response.text = "Hello from News Page"

@app.route("/hello/{name}")
def greeting(request, response ,name):
    response.text = f"Hello , {name} :)"
    