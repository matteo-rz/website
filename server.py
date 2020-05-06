from flask import Flask, render_template, request, redirect,flash
import csv
#render template allows us to send HTML file

app = Flask(__name__) #use flask class to instantiate an app


@app.route('/')     #this is a decorator
def my_home():
    return render_template('index.html') #note that Flask automatically tries to look in template directory

@app.route('/components.html')     #this is a decorator
def components():
    return render_template('components.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=='POST':
        try:
            info_received = request.form.to_dict()   #turn the data into a dictionary
            write_to_csv(info_received)
            return render_template('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'

def write_to_file(data):
    with open('database.txt','a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file=database.write(f'\n{email}, sbj:{subject}, msg:{message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message]) #the data is passed as list

#sent as a string, flask automatically converts to HTML to be readable by browser!


app.run()