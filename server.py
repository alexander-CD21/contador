
from flask import Flask,render_template,redirect,session

app=Flask(__name__)
app.secret_key = "contandolosnumeros" 

@app.route('/')
def contador():
    if "contador" in session:
        session["contador"]+=1
    else :
        session["contador"]=1
    return render_template("index.html")

@app.route('/contador2', methods=["POST"] )
def contarDos():
    
    if "contador" in session:
        session["contador"]+=1
    return redirect( '/' )

@app.route( '/destruir', methods=["GET"] )
def reset():
    session.clear()
    return redirect( '/' )
    

if __name__=="__main__":
    app.run(debug=True)