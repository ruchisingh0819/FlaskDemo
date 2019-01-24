from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    abc="ruchi"
    list2=[1,2,3]
    
    return render_template('temp.html',name=abc,list1=list2[1])
    
if __name__=="__main__":
  app.run(debug=True)
