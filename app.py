from flask import Flask,render_template,redirect
import mysql.connector
from forms import RegisterForm,LoginForm

app = Flask(__name__)
app.secret_key = "Naafiri" 
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="gabbie",
        password="Kr!llM3R1ghtN@w",
        database="shrine"
    )
"""
def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="DIN_DB_BRUKER",
        password="DITT_PASSORD",
        database="DIN_DATABASE" 
    )


# Alle Ruter til sider for programmet ligger listet her #

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        brukernavn = form.username.data
        passord = form.password.data
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn FROM kunder WHERE brukernavn=%s AND passord=%s",
            (brukernavn, passord)
        )
        return redirect("/login")  #fortsatt i if-blokken

    return render_template("register.html", form=form) #utenfor if-blokken)
    user = cur.fetchone() #Husker å lagre svar fra databasen i variabel user!
    cur.close()
    conn.close()

"""



@app.route('/')
def base():


    return render_template("base.html")




@app.route('/welcome')
def welcome():
    return render_template("welcome.html")




@app.route('/register')
def register():
    


    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        'SELECT tag FROM shrine;'
    )
    tags = cur.fetchall()
    cur.close()
    conn.close()


    return render_template("register.html", tags = tags)

@app.route('/register/<tag>')
def vision(tag):
    
    conn = get_conn()
    cur = conn.cursor(dictionary=True)
    cur.execute(
        'SELECT * FROM shrine WHERE tag=%s;',(tag,)
    )
    book = cur.fetchone()
    cur.close()
    conn.close()


    return render_template("library.html", book = book)



    """

    ### IMPORTANT: Register Code ###
    

    evry = ["aim", "movement", "communication", "defense","looting","constructionFO","constructionIC","lootingFO","lootingIC"]
    combat = ["aim", "movement", "communication", "defense"]
    survival = ["movement", "communication", "lootingFO","lootingIC","constructionFO","constructionIC"]
    development = ["lootingFO","lootingIC","constructionFO","constructionIC","defense"]

    FO = ["aim", "movement", "communication", "defense","lootingFO","constructionFO"]
    IC = ["aim", "movement", "communication", "defense","lootingIC","constructionIC"]


    # The Sets for different purposes! #
    selected = {FO,IC}



    results = evry.intersection(selected)


    pages = {
        "aim": "/aim",
        "movement": "/movement",
        "communication": "/communication",
        "defense": "/defense",
        "lootingFO": "/looting_ICARUS",
        "lootingIC": "/looting_FALLOUT",
        "constructionFO": "/construction_ICARUS",
        "constructionIC": "/construction_FALLOUT"
    }
    , results=results, pages=pages
    """
    


@app.route('/index')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()
