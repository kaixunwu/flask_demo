from app import app
from app import db
from app.model.models import User


@app.route('/')
def hello_word():
    return 'hello world!'


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
