from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2
from model.post import Post
from config import APP_NAME

app = Sanic(APP_NAME)
app.static("/static", "./static")
jinja = SanicJinja2(app)

globals ={ 
           "menu": {"Frontpage":"/", "Write blog":"/write_blog"}
         }

@app.get("/")
@jinja.template("index.html")
async def home(request):
    return globals

@app.get("/write_blog")
@jinja.template("write_blog.html")
async def write_blog(request):
    return globals

@app.post("/newpost")
async def new_post(request):
    title = request.form.get('blogname')
    
    return redirect(f"/write_blog")

if __name__ == "__main__":
    app.run(host="localhost", port=8080)