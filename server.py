from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, message])


@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('thankyou.html')

from pymongo import MongoClient

def get_database():
   CONNECTION_STRING = "mongodb+srv://polohi:0yKy6gvhcz0ac9dR@cluster0.or0xa7y.mongodb.net/test"
   client = MongoClient(CONNECTION_STRING)
   return client['user_messages']