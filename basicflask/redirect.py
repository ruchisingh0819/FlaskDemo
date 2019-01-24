from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/admin")
def index_admin():
    return "Administrator area,guest not allowed"
@app.route("/guest/<guest>")
def index_guest(guest):
    return "Guest user %s not having admin rights"%guest
@app.route("/user/<name>")
def index_user(name):
    if name=="admin":
        return redirect(url_for('index_admin'))
    else:
        return redirect(url_for('index_guest',guest=name))
if __name__=="__main__":
  app.run(debug=True)
