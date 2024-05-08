from app import JdpuPF

app = JdpuPF()

@app.route('/home')
def home(request,response):
    response.text= "Hello from the Home Page"


@app.route("/about")
def about(request,response):
    response.text= "Hello from the About Page"

@app.route("/lochin")
def about(request,response):
    response.text= "Hello from the Lochin Page"


