import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # I personally don't like mixing post logic with rendering, but these are the constraints of the app
    total_fruits = int(request.form['strawberry']) + int(request.form['raspberry']) + int(request.form['apple'])
    print(f"Charging {request.form['first_name']} {request.form['last_name']} for {total_fruits} fruits")
    return render_template(
        "checkout.html",
        strawberry=request.form['strawberry'],
        raspberry=request.form['raspberry'],
        apple=request.form['apple'],
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        student_id=request.form['student_id'],
    )

@app.route('/fruits')         
def fruits():
    # I went a bit overboard here
    image_folder = os.path.join(app.static_folder, 'img')
    image_names = os.listdir(image_folder)
    image_urls = []
    for image in image_names:
        current_url = url_for('static', filename=f"img/{image}")
        image_urls.append(current_url)
    return render_template("fruits.html", images=image_urls)

if __name__=="__main__":   
    app.run(debug=True)    