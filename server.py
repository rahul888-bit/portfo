from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route("/")
def greetings():
    return render_template("index.html")


@app.route("/<string:pagename>")
def go_to_a_page(pagename):
    return render_template(pagename)


def read_csv(datum):
    with open("data.csv", mode="a") as my_file:
        email = datum["email"]
        subject = datum["subject"]
        message = datum["message"]
        csv_writer = csv.writer(my_file, delimiter=",",
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        read_csv(data)
        return redirect("index.html")
    else:
        return "Something is wrong"
    return "Heyyyyyy"
