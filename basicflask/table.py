from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    dict1={'Maths':80,'C':70,'java':60}
    print(dict1)
    return render_template('table.html',result=dict1)
    
if __name__=="__main__":
  app.run(debug=True)
