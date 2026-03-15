from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_socialmedia", methods=["GET","POST"])
def add_one_socialmedia():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into socialmedia (name) values (:name)",request.form)
        user = query_db('select * from socialmedia')
        return render_template("socialmediaform.html", socialmedias=user, one_user=one_user, the_title="add new socialmedia")
    user = query_db('select * from socialmedia')
    one_user = query_db("select * from socialmedia limit 1", one=True)
    return render_template("socialmediaform.html", socialmedias=user, one_user=one_user, the_title="add new socialmedia")

@app.route("/add_one_programminglanguage", methods=["GET","POST"])
def add_one_programminglanguage():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into programminglanguage (name) values (:name)",request.form)
        user = query_db('select * from programminglanguage')
        return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")
    user = query_db('select * from programminglanguage')
    one_user = query_db("select * from programminglanguage limit 1", one=True)
    return render_template("programminglanguageform.html", programminglanguages=user, one_user=one_user, the_title="add new programminglanguage")

@app.route("/add_one_script", methods=["GET","POST"])
def add_one_script():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into script (title,description,myscript,programminglanguage_id,socialmedia_id) values (:title,:description,:myscript,:programminglanguage_id,:socialmedia_id)",request.form)
        user = query_db('select * from script')
        return render_template("scriptform.html", scripts=user, one_user=one_user, the_title="add new script")
    user = query_db('select * from script')
    one_user = query_db("select * from script limit 1", one=True)
    return render_template("scriptform.html", scripts=user, one_user=one_user, the_title="add new script")

