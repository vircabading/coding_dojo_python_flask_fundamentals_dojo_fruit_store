from flask import Flask, render_template, request, redirect
from werkzeug.datastructures import RequestCacheControl
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

# @app.route('/checkout')         
# def checkout():
#     # print(request.form)
#     return render_template("checkout.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_num = request.form['strawberry']                         # Retrieve variables from the form
    raspberry_num = request.form['raspberry']
    apple_num = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    print(f"straberry num: {strawberry_num} :: raspberry num: {raspberry_num} :: apple num: {apple_num}")
    print(f"first name: {first_name} :: last name: {last_name} :: student id: {student_id}")
    return render_template("checkout.html", strawberry_num = strawberry_num , raspberry_num = raspberry_num, apple_num = apple_num, first_name= first_name, last_name = last_name, student_id = student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    