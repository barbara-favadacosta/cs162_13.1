from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///things.db'

db = SQLAlchemy(app)



####################################################################3

class Thing(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))

############################################################################


@app.route('/add', methods=['POST'])
def add():
    thing =Thing(text=request.form['thing'])
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for('index'))



def index():
    things = Thing.query.all()
    return render_template('index.html', things=things)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
