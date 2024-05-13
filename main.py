from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic("Try")
app.static("/static", "./static")
jinja = SanicJinja2(app)

baner = ["Tennis","Badminton","Volleyball"]

globals ={ 
<<<<<<< Updated upstream
           "menu": {"Book":"/book","Bliv Medlem":"/logind",}
=======
           "menu": {"Book":"/book", "Bliv Medlem":"/logind"},
>>>>>>> Stashed changes
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

@app.get("/Bliv_medlem", name = "Bliv_medlem-page")
@jinja.template("Bliv_medlem.html")
async def Bliv_medlem(request):
    return globals

if __name__ == "__main__":
    app.run(host="localhost", port=8080)