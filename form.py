# from flask import Flask
# from flask_sqlalchemy import sqlalchemy
# import psycopg2
# from flask_login import LoginManager,UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='postgres://postgres:33200161@127.0.0.1:5432/suppliers'
# app.config['SECRET_KEY'] = 'can not touch this'

# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email  = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('Password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email  = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

   

# conn = psycopg2.connect("dbname = 'suppliers' user ='postgres' host ='127.0.0.1' port ='5432' password =33200161")

# cursor = conn.cursor()

# cursor.execute('SELECT version();')
# record = cursor.fetchall()
# print('you are connected to -', record, '\n')



# cursor.close()
# conn.close()
# print('postgreSQL connection is closed')

# @login_manager.user.loader
# def load_user(user_id):
#     return user.query.get(int(user_id))




# if __name__=="__main__":