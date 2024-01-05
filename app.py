from flask import Flask, render_template, request, url_for, redirect
import os

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0


@app.route("/")  # this decorator create the home route
def home():
    techs = ["HTML", "CSS", "Flask", "Python"]
    name = "30 Days Of Python Programming"
    return render_template("home.html", techs=techs, name=name, title="Home")


@app.route("/about")
def about():
    name = "30 Days Of Python Programming"
    return render_template("about.html", name=name, title="About Us")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/post", methods=["GET", "POST"])
def post():
    name = "Text Analyzer"
    if request.method == "GET":
        return render_template("post.html", name=name, title=name)
    if request.method == "POST":
        content = request.form["content"]
        return redirect(url_for("result"))


def start_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)


def start_server():
    from wsgiref import simple_server

    # for deployment
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    # app.run(debug=True, host='0.0.0.0', port=port)

    httpd = simple_server.make_server("", port, app)
    print(f"Serving 0.0.0.0 on port {port}, control-C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Shutting down.")
        httpd.server_close()


if __name__ == "__main__":
    # start_server()
    start_flask()
