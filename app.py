from flask import Flask, render_template, request, session, redirect, flash, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from models.user import Product, Member, db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = "SuperSecretKey"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

# flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# create the db structure
with app.app_context():
    db.create_all()

@app.route('/')
@login_required
def index():
    products = Product.query.all()
    print(current_user)
    #registered_member = registered_member
    return render_template('index.html', products=products,user=current_user)


@app.route("/login", methods=["GET", "POST"])
def login():

    # clear the initial flash message
    session.clear()

    if request.method == 'GET':
        return render_template('login.html')

    # get the form data
    memberID = request.form['memberID']

    # query the member
    registered_member = Member.query.filter_by(memberID=memberID).first()

    # check the passwords
    if registered_member is None :
        flash('Invalid Member ID')
        return render_template('login.html')

    # login the user
    login_user(registered_member)
    return redirect(request.args.get('next') or url_for('index'))


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        session.clear()
        return render_template('register.html')

    # get the data from our form
    #password = request.form['password']
    #conf_password = request.form['confirm-password']
    username = request.form['memberID']
    #email = request.form['email']

    # make sure the password match
    if conf_password != password:
        flash("Passwords do not match")
        return render_template('register.html')

    # create a user, and check if its unique
    user = User(username, password, email)
    u_unique = user.unique()

    # add the user
    if u_unique == 0:
        db.session.add(user)
        db.session.commit()
        flash("Account Created")
        return redirect(url_for('login'))

    # else error check what the problem is
    elif u_unique == -1:
        flash("Email address already in use.")
        return render_template('register.html')

    elif u_unique == -2:
        flash("Username already in use.")
        return render_template('register.html')

    else:
        flash("Username and Email already in use.")
        return render_template('register.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


# required function for loading the right user
@login_manager.user_loader
def load_user(id):
    return Member.query.get(int(id))

# load nickname
#@login_manager.user_loader
#def load_nick(id):
#    return Member.query.get(int(id))


if __name__ == '__main__':
    app.run()
