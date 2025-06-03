from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://uwpbrzasi4dzqlld8ekl:B7ADHjpsKnVUWKu71i9aBDA7oOlyEY@bbqhgph7wb0iza3ajqzn-postgresql.services.clever-cloud.com:50013/bbqhgph7wb0iza3ajqzn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models.Author import Author
from models.Member import Member

@app.route('/authors', methods=['GET'])
def getAuthors():
    authors = Author.query.all()
    return render_template('authors.html', authors=authors)

@app.route('/members', methods=['GET'])
def getMembers():
    members = Member.query.all()
    members_list = [member.to_dict() for member in members]
    return jsonify(members_list)

@app.route('/members', methods=['POST'])
def registerUser():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')

    if not all([first_name, last_name, email, password]):
        raise ValueError("Missing fields in the request data")

    new_user = Member(first_name=first_name, last_name=last_name, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 200


if __name__ == '__main__':
    app.run()
