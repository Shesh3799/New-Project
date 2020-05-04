from utilities import *
@app.route('/plogin',methods=['GET','POST'])
def plogin():
    if (session.get('pid') is None):
        if (request.method == 'POST'):
            name=request.form.get('patient_email')
            name=name.lower()
            password=request.form.get('patient_pass')
            query = patient.query.filter_by(email=name).first()
            if (query is None):
                flash('No such Patient ID exist')
                return redirect(url_for('plogin'))
            else:
                if(query.password==password):
                    session['pid'] = name
                    return redirect(url_for('patient_dashboard'))
                else:
                    flash("Password error")
            return render_template('patient_login.html')
        return render_template('patient_login.html')

    else:
        return redirect(url_for('patient_dashboard'))

@app.route('/llogin',methods=['GET','POST'])
def llogin():
    if (session.get('lid') is None):
        if (request.method == 'POST'):
            name=request.form.get('lab_name')
            name=name.lower()
            password=request.form.get('lab_pass')
            query = sample_collection.query.filter_by(regno=name).first()
            if (query is None):
                flash('No such Lab ID exist')
                return redirect(url_for('llogin'))
            else:
                if(query.password==password):
                    session['lid'] = name
                    return redirect(url_for('staff_dashboard'))
                else:
                    flash("Password error")
            return render_template('sample_login.html')
        return render_template('sample_login.html')

    else:
        return redirect(url_for('staff_dashboard'))

@app.route('/tlogin',methods=['GET','POST'])
def tlogin():
    if (session.get('tid') is None):
        if (request.method == 'POST'):
            name=request.form.get('test_name')
            name=name.lower()
            password=request.form.get('test_pass')
            query = testing_facility.query.filter_by(regno=name).first()
            if (query is None):
                flash('No such Lab ID exist')
                return redirect(url_for('tlogin'))
            else:
                if(query.password==password):
                    session['tid'] = name
                    flash("Sucess")
                else:
                    flash("Password error")
            return render_template('testing_login.html')
        return render_template('testing_login.html')

    else:
        flash("Already Signed IN as "+str(session.get('tid')))
        return render_template('testing_login.html')

@app.route('/plogout',methods=['GET','POST'])
def plogout():
    session.pop('pid',None)
    flash("Sucessfully logged out")
    return render_template('patient_login.html')

@app.route('/llogout',methods=['GET','POST'])
def llogout():
    session.pop('lid',None)
    flash("Sucessfully logged out")
    return render_template('sample_login.html')

@app.route('/tlogout',methods=['GET','POST'])
def tlogout():
    session.pop('tid',None)
    flash("Sucessfully logged out")
    return render_template('testing_login.html')





