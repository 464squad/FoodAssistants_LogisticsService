from flask import Flask  # import objects from flask model

app = Flask(__name__)  # define app using flask


if __name__ == "__main__":
    app.run(port=3000)  # run app on port 3000
