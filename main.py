from sanic import Sanic
from sanic_jinja2 import SanicJinja2
import uuid
from sanic.response import redirect 

app = Sanic("Try")
app.static("/static", "./static")
jinja = SanicJinja2(app)

baner = ["Tennis","Badminton","Volleyball"]

Bliv_medlem = []

globals ={ 
           "menu": {"Book":"/book", "login":"/logind"},
           "Bliv_medlem" : {},
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

@app.get("/Bliv_medlem", name = "medlem-page")
@jinja.template("signup.html")
async def Bliv_medlem(request):
    return globals

@app.post("/Bliv_medlem")
async def Bliv_medlem(request):
    Bliv_medlem_brugernavn = request.form.get("Brugernavn")
    Bliv_medlem_gmail = request.form.get("Gmail")
    Bliv_medlem_adgangskode = request.form.get("Adgangskode")
    id = str(uuid.uuid4())

    Bliv_medlem_entry = {"id": id, "Bliv_medlem_brugernavn": Bliv_medlem_brugernavn, "Bliv_medlem_gmail": Bliv_medlem_gmail, "Bliv_medlem_adgangskode": Bliv_medlem_adgangskode}
    Bliv_medlem.append(Bliv_medlem_entry)
    return redirect("/logind")



if __name__ == "__main__":
    app.run(host="localhost", port=8080)