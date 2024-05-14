from sanic import Sanic
from sanic_jinja2 import SanicJinja2
import uuid
from sanic.response import redirect 

app = Sanic("Try")
app.static("/static", "./static")
jinja = SanicJinja2(app)

Bliv_medlem = []


booke = []

globals = { 
           "menu": {"Book":"/book", "Bliv Medlem":"/logind"},
           "Sport": ["Tennis","Badminton","Volleyball"],
           "valgt_sport": None,
           "current_user": None,
           "ugedage": ["ma","ti","on","to","fr","lø","sø"],
           "dage": [],
           "booked": booke
           
}

for i in range(1,32):
    globals["dage"].append(i)

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

@app.get("/logind")
@jinja.template("logind.html")
async def logind(request):
    if globals["current_user"]:
        return globals
    else:
        globals_copy = globals.copy()
        if "Bliv Medlem" in globals_copy["menu"]:
            globals_copy["menu"].pop("Bliv Medlem")
        globals_copy["menu"]["Bliv Medlem"] = "/Bliv_medlem"
        return globals_copy

@app.get("/book")
@jinja.template("book.html")
async def book(request):
    return globals

@app.get("/Bliv_medlem", name = "medlem-page")
@jinja.template("Bliv_medlem.html")
async def bliv_medlem(request):
    return globals

@app.get("/logaf/<brugernavn>")
async def log_af(request, brugernavn: str):
    if globals["current_user"] == brugernavn:
        globals["current_user"] = None
        if f"log af: {brugernavn}" in globals["menu"]:
            globals["menu"].pop(f"log af: {brugernavn}")
        return redirect("/logind")

@app.post("/valgt")
async def valgt_dato(request):
    booking = request.form.get("vlgt")
    Andreas = {"booking": booking, "sport": globals["valgt_sport"]}
    booke.append(Andreas)
    print(globals["booked"])
    return redirect("/")

@app.post("/logind")
async def login(request):
    brugernavn = request.form.get("Brugernavn")
    adgangskode = request.form.get("Adgangskode")
    
    match = next((user for user in Bliv_medlem if user ["Bliv_medlem_brugernavn"] == brugernavn), None)
    
    if match and match["Bliv_medlem_adgangskode"] == adgangskode:
        globals["current_user"] = brugernavn
        if "Bliv Medlem" in globals["menu"]:
            globals["menu"].pop("Bliv Medlem")
        redirect_obj = redirect("/")
        return redirect_obj
    else:
        globals["current_user"] = False
        return redirect("/logind")

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