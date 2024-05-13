from sanic import Sanic
from sanic_jinja2 import SanicJinja2
from sanic.response import redirect
import uuid

app = Sanic("Try")
app.static("/static", "./static")
jinja = SanicJinja2(app)

<<<<<<< Updated upstream
baner = ["Tennis","Badminton","Volleyball"]

globals ={ 
<<<<<<< Updated upstream
           "menu": {"Book":"/book","Bliv Medlem":"/logind",}
=======
           "menu": {"Book":"/book", "Bliv Medlem":"/logind"},
>>>>>>> Stashed changes
=======
Bliv_Medlem = []

globals ={ 
           "menu": {"Book":"/book","Bliv Medlem":"/logind"}
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

@app.get("/logpå")
@jinja.template("logpå.html")
async def logpå(request):
    return globals

@app.post("/logind")
async def logind(request):
    Bliv_Medlem_brugernavn = request.form.get("Brugernavn")
    Bliv_Medlem_gmail = request.form.get("Gmail")
    Bliv_Medlem_adgangskode = request.form.get("Adgangskode")
    id = str(uuid.uuid4())

    Bliv_Medlem_entry = {"id": id, "Bliv_Medlem_brugernavn": Bliv_Medlem_brugernavn, "Bliv_Medlem_gmail": Bliv_Medlem_gmail, "Bliv_Medlem_adgangskode": Bliv_Medlem_adgangskode}
    Bliv_Medlem.append(Bliv_Medlem_entry)
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="localhost", port=8080)