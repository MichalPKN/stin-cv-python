from flask import Flask
from controllers.payment_controller import payment_controller

app = Flask(__name__)
app.register_blueprint(payment_controller)

if __name__ == '__main__':
    app.run(debug=True)