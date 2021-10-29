import datetime
from flask import Flask, render_template, request, redirect, session
from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/post_checkout', methods=['POST'])
def post_checkout():
    print(request.form)
    session['strawberry_num'] = request.form['strawberry']                          # Retrieve variables from the form
    session['raspberry_num'] = request.form['raspberry']                            #     and store the vars as in a session
    session['apple_num'] = request.form['apple']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['student_id'] = request.form['student_id']
    return redirect ("/checkout")
    

@app.route('/checkout')         
def checkout():
    current_date_time = datetime.datetime.now()
    total_num_ordered = int(session['strawberry_num']) + int(session['raspberry_num']) + int(session['apple_num'])
    return render_template("checkout.html", total_num_ordered= total_num_ordered, current_date_time= current_date_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    