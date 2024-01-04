from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, git!"


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
