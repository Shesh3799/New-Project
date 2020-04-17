from login import *
from signup import *


@app.route('/')
def home():
    return render_template('patient_register.html')


if __name__=="__main__":
     app.run(port=5000, debug=True)