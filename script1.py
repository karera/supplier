from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import psycopg2
from form import RegistrationForm,LoginForm

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://postgres:33200161@127.0.0.1:5432/suppliers'
app.config['SECRET_KEY'] = '92f2c670322a0af6d7a3fc337d71b01a'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email  = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200))
    first_name = db.Column(db.String(50), nullable=False, unique=True)
    last_name = db.Column(db.String(50), nullable=False, unique=True)
    u_gender = db.Column(db.String(50))
    u_mobile = db.Column(db.Integer,nullable=False, unique=True)
    u_datetime = db.Column(db.DateTime, default=datetime.utcnow)
    u_address = db.Column(db.Text, nullable=False)

conn = psycopg2.connect("dbname = 'suppliers' user ='postgres' host ='127.0.0.1' port ='5432' password =33200161")

cursor = conn.cursor()

cursor.execute('SELECT version();')
record = cursor.fetchall()
print('you are connected to -', record, '\n')



cursor.close()
conn.close()
print('postgreSQL connection is closed')

@app.before_first_request
def create_all():
    db.create_all()


log_in = [
    {
        'email':'admin@gmail.com',
        'password': '123',
        'first_name':'sam',
        'last_name':'eliot',
        'mobile':'0705146265'
    },
    {
        'email':'admin@gmail.com',
        'password': '123',
        'first_name':'sam',
        'last_name':'eliot',
        'mobile': '0705'


    }
]

@app.route('/')
def home():
    return 'Homepage here'


@app.route('/about')
def about():
    return render_template("form.html")

@app.route('/signup')
def signup():
    return render_template("sign.html")


@app.route('/suppliers', methods=['GET','POST'])
def suppliers():
    if request.method == 'POST':
        email_u = request.form['email']
        password_U = request.form['password']
        first = request.form['first_name']
        last = request.form['last_name']
        gender = request.form['u_gender']
        mobile = request.form['u_mobile']
        address = request.form['u_address']

        print(request.form.get('email'))
        print(request.form['password'])

        Record = Users(email=email_u, password=password_U, first_name=first, last_name=last, u_gender=gender, u_mobile=mobile, u_address=address)
        db.session.add(Record)
        db.session.commit()
        return redirect('/suppliers')
    else:
    #     log_in = Users.query.all()
        return render_template("supplier.html")
        #if i wanted to return content to the form
        # return render_template("supplier.html", suppliers=log_in)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for(suppliers))
    return render_template('register.html', title='Register', form=form)
    
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('you have been logged in', 'success')
            return redirect(url_for('suppliers'))
        else:
            flash('login unsuccessful. please check username and password', 'danger')

    return render_template('Login.html', title='Login', form=form)



if __name__=="__main__":
    app.run(debug=True)