from sanic import Sanic
from sanic.response import redirect 
from sanic_jinja2 import SanicJinja2
from model.post import Post
from config import APP_NAME

app = Sanic(APP_NAME)
app.static("/static", "./static")
jinja = SanicJinja2(app)

"""
TODO: I dictionaryen "globals" skal i tilføje en dictionary-værdi "About" til nøglen "menu"
som peger på et "/about"-endpoint
Test hvad der sker hvis i kører programmet kommer menupunktet frem? 
Hvad sker der hvis man trykker på det? 

TODO: Tilføj en handler som reagerer på "/about"-endpointet og giv det et jinja-template "about.html"
OBS1: I skal oprette et template med filnavnet "about.html"
OBS2: I skal også lave en asynkron funktion der returnere dictionariet globals

TODO: Sørg for man kan sende en POST-request med både title på bloggen og text 
til "/newpost"-endpointet med den form der ligger i write_blog.html
OBS: Pt. indtaster man kun titlen på en post under denne form, man skal altså tilføje et yderligere input-tag

TODO: Sørg for at man kan gemme titel og text i et post-objekt. Pt. kan post-objekter kun 
indeholde titler.
Når newpost() bliver kaldt, skal i tilføje formens indhold til en instans af objektet og 
gemme objektet i jeres dict

TODO: Sørg for at man kan se jeres posts på "/posts"-endpointet
"""

#Menu logik (key = "navn", value = endpoints)
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