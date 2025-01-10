import os
import csv
from flask import Flask, render_template, request, redirect


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database_csv:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(
            database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        if database_csv.tell() == 0:
            csv_writer.writerow(['email', 'subject', 'message'])

        csv_writer.writerow([email, subject, message])


app = Flask(__name__)


@app.route('/')
def root_page():
    return render_template('index.html')


@app.route('/<string:pagename>')
def regular_page(pagename='index'):
    return render_template(f'{pagename}.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'
