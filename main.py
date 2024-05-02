from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2
from model.post import Post
from config import APP_NAME

app = Sanic(APP_NAME)
app.static("/static", "./static")
jinja = SanicJinja2(app)

globals ={ 
           "menu": {"Book":"/book", "Bliv Medlem":"/logind"}
         }

@app.get("/")
@jinja.template("index.html")
async def home(request):
    return globals

@app.get("/book")
@jinja.template("book.html")
async def book(request):
    return globals

@app.get("/logind")
@jinja.template("logind.html")
async def logind(request):
    return globals


if __name__ == "__main__":
    app.run(host="localhost", port=8080)