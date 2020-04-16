from utilities import *
@app.route('/plogin',methods=['GET','POST'])
def plogin():
    if (session.get('pid') is None):
        if (request.method == 'POST'):
            pid=request.form.get('patient_id')
            name=request.form.get('patient_name')
            name=name.lower()
            password=request.form.get('patient_pass')
            query = login.query.filter_by(uid=pid).first()
            if (query is None):
                flash('No such Patient ID exist')
                return redirect(url_for('plogin'))
            else:
                qname=query.username
                qname=qname.lower()
                if(query.password==password and qname==name):
                    session['pid'] = pid
                    flash("Sucess")
                else:
                    flash("User name or password error")
            return render_template('patient_login.html')
        return render_template('patient_login.html')

    else:
        flash("Already Signed IN as "+str(session.get('pid')))
        return render_template('patient_login.html')

@app.route('/llogin',methods=['GET','POST'])
def llogin():
    if (session.get('lid') is None):
        if (request.method == 'POST'):
            lid=request.form.get('lab_id')
            name=request.form.get('lab_name')
            name=name.lower()
            password=request.form.get('lab_pass')
            query = lab_login.query.filter_by(lid=lid).first()
            if (query is None):
                flash('No such Lab ID exist')
                return redirect(url_for('llogin'))
            else:
                qname=query.username
                qname=qname.lower()
                if(query.password==password and qname==name):
                    session['lid'] = lid
                    flash("Sucess")
                else:
                    flash("User name or password error")
            return render_template('sample_login.html')
        return render_template('sample_login.html')

    else:
        flash("Already Signed IN as "+str(session.get('lid')))
        return render_template('sample_login.html')

@app.route('/tlogin',methods=['GET','POST'])
def tlogin():
    if (session.get('tid') is None):
        if (request.method == 'POST'):
            tid=request.form.get('test_id')
            name=request.form.get('test_name')
            name=name.lower()
            password=request.form.get('test_pass')
            query = testlab_login.query.filter_by(tid=tid).first()
            if (query is None):
                flash('No such Lab ID exist')
                return redirect(url_for('tlogin'))
            else:
                qname=query.username
                qname=qname.lower()
                if(query.password==password and qname==name):
                    session['tid'] = tid
                    flash("Sucess")
                else:
                    flash("User name or password error")
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





