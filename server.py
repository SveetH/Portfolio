from flask import Flask ,render_template , request, redirect
import csv

app = Flask(__name__)


 
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

def write_to_file(data):
	with open('database.txt', mode='a') as database:
		email = data["email"]
		name = data["name"]
		phone = data["phone"]
		message = data["message"]
		file = database.write(f'\n {name}, {email}, {phone}\n message: {message}\n')

def write_to_csv(data):
    with open('database2.csv', mode='a') as database2:
        email = data["email"]
        name = data["name"]
        phone = data["phone"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, name, phone, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	data = request.form.to_dict()
    	write_to_csv(data)
    	return redirect('/submit')
    else:
    	pass