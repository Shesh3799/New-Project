from utilities import *
@app.route('/psignup',methods=['GET','POST'])
def psignup():

    if (request.method == 'POST'):
        f = request.form
        value_list = []

        for key in f.keys():
            for value in f.getlist(key):
                # value_list.append(value)
                print(key,value)
        flash("Success")
        return render_template('patient_register.html')

    return render_template('patient_register.html')

