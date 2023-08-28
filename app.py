from flask import Flask, render_template
import model
model.start()
app = Flask(__name__)

@app.route("/", methods = ['POST'])
def get_predictions():
    query = request.form['query']
    return model.predict(query)
