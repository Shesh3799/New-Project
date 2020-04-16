from login import *


@app.route('/')
def home():
    return render_template('dashboard.html')


if __name__=="__main__":
     app.run(port=5000, debug=True)