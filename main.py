from app import JdpuPF

app = JdpuPF()

@app.route('/home')
def home(request,response):
    response.text= "Hello from the Home Page"


@app.route("/hello/{name}")
def greeting(request, response ,name):
    response.text = f"Hello , {name} :)"
    