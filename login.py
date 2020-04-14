from utilities import *
@app.route('/plogin',methods=['GET','POST'])
def plogin():
    if (request.method == 'POST'):
        f = request.form
        print("Sucess")
        for i in f.keys():
            for j in f.getlist(i):
                print(j)

    return render_template('patient_portal.html')


