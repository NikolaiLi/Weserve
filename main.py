from sanic import Sanic
from sanic_jinja2 import SanicJinja2
import uuid
from sanic.response import redirect 

app = Sanic("Try")
app.static("/static", "./static")
jinja = SanicJinja2(app)

Bliv_medlem = []

globals ={ 
           "menu": {"Book":"/book", "Bliv Medlem":"/logind"},
           "Sport": ["Tennis","Badminton","Volleyball"],
           "valgt_sport": None
}
@app.get("/")
@jinja.template("index.html")
async def home(request):
    return globals


@app.get("/Sport/<sport_valg>")
@jinja.template("Sport.html")
async def sport(request, sport_valg: str):
    for sport in globals["Sport"]:
        if sport_valg == sport:
            globals["valgt_sport"] = sport_valg
        else:
            print("ikke en rigtig sport")
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
@jinja.template("Bliv_medlem.html")
async def bliv_medlem(request):
    return globals

@app.post("/logind")
async def login(request):
    brugernavn = request.form.get("Brugernavn")
    adgangskode = request.form.get("Adgangskode")
    
    match = next((user for user in Bliv_medlem if user ["Bliv_medlem_brugernavn"] == brugernavn), None)
    
    if match and match["Bliv_medlem_adgangskode"] == adgangskode:
        redirect_obj = redirect("/")
        return redirect_obj
    else:
        return redirect("/Bliv_medlem")

@app.post("/Bliv_medlem")
async def bliv_medlem(request):
    Bliv_medlem_brugernavn = request.form.get("Brugernavn")
    Bliv_medlem_adgangskode = request.form.get("Adgangskode")
    id = str(uuid.uuid4())

    Bliv_medlem_entry = {"id": id, "Bliv_medlem_brugernavn": Bliv_medlem_brugernavn, "Bliv_medlem_adgangskode": Bliv_medlem_adgangskode}
    Bliv_medlem.append(Bliv_medlem_entry)
    return redirect("/logind")

if __name__ == "__main__":
    app.run(host="localhost", port=8080)