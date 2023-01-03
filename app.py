from flask import Flask, render_template,redirect,flash,request
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,Pet
from forms import AddPetForm


app = Flask(__name__)
app.app_context().push()

app.config["SECRET_KEY"] = "oh-so-secret"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///wtforms"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:secret@localhost:5432/wtforms'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    pets = Pet.query.all()
    return render_template('home.html',pets = pets)


@app.route('/add', methods=['GET','POST'])
def Add_pet():
    
    form =  AddPetForm()
    
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        age = form.age.data
        photo_url =form.photo_url.data
        is_available = form.is_available.data
        pet = Pet(name=name,species=species,age=age,photo_url=photo_url, is_available = is_available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Created new {species}: name is {name}  and age is {age}")
        return redirect('/')
    else:
        return render_template('add_pet.html', form = form)

##################################################################
@app.route('/<int:id>/edit', methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)
    # options = db.session.query(Pet.species)
    # form.species.choices = options

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.is_available = form.is_available.data
        db.session.commit()
        flash(f"{pet.name} updated")
        db.session.commit()
        return redirect("/")
    else:
        return render_template("edit_pet_form.html", form=form, pet = pet)
