from app import db


class Member(db.Model):
    __tablename__ = 'members'

    member_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String(), nullable=False)
    registration_date = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'member_id': self.member_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password': self.password,
            'registration_date': self.registration_date.isoformat() if self.registration_date else None
        }

    @classmethod
    def create_from_request(cls, request):
        data = request.json
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if not all([first_name, last_name, email, password]):
            raise ValueError("Missing fields in the request data")

        new_user = cls(first_name=first_name, last_name=last_name, email=email, password=password)

        db.session.add(new_user)
        db.session.commit()

        return new_user

