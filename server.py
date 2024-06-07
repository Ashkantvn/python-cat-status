from flask import Flask,render_template,request
from status import get_status
from waitress import serve
import os


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template(
            "index.html")

@app.route("/status")
def create_status():
    status_code = request.args.get("status")
    url = f"https://http.cat/{status_code}"
    
    if not bool(status_code):
        status_code = "404"

    status_data = get_status(status_code)
    

    if not status_data.status_code == 200:
        return "THERE IS NO DATA!"


    if not os.path.exists('static/image/'):
        os.makedirs('static/image/')
    
    with open(f"static/image/status.jpg", 'wb+') as f:
        f.write(status_data.content)
    

    return render_template(
            "status.html",
            title=status_code,
            link = url)


if __name__ == "__main__":
 
    serve(app,host="0.0.0.0",port="8000")



