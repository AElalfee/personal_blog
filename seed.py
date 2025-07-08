import os

from dotenv import load_dotenv

from app import create_app, db
from app.models import User

load_dotenv()

app = create_app()

with app.app_context():
    db.create_all()

    existing_user = User.query.filter_by(email=os.getenv("ADMIN_EMAIL")).first()

    if not existing_user:
        user = User(
            username=os.getenv("ADMIN_USERNAME"), email=os.getenv("ADMIN_EMAIL")
        )
        user.set_password(os.getenv("ADMIN_PASSWORD"))

        db.session.add(user)
        db.session.commit()
        print("User created successfully with username: ", user.username)
