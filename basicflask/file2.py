from flask import Flask
app=Flask(__name__)
@app.route("/hi/<float:no>")
def index(no):
    return'Number is %f'%no
if __name__=="__main__":
  app.run(debug=True)
