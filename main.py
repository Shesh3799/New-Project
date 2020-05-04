from login import *
from signup import *
from dashboard import *


@app.route('/')
def home():
    return render_template('index.html')


if __name__=="__main__":
     app.run(port=5000, debug=True)