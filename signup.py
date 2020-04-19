from utilities import *
@app.route('/psignup',methods=['GET','POST'])
def psignup():
    if (request.method == 'POST'):
        name=request.form.get('name')
        pas=request.form.get('pass')
        adhar=request.form.get('adhar_num')
        fname=request.form.get('Fname')
        mname=request.form.get('Mname')
        gen=request.form.get('gender')
        dob=request.form.get('DOB')
        email=request.form.get('Email')
        phone=request.form.get('ph_num')
        state=request.form.get('state')
        city=request.form.get('city')
        addr=request.form.get('caddress')
        entry = patient(adharname=name,password=pas,adharno=adhar,father=fname,mother=mname,gender=gen,dob=dob, email=email, contact=phone, state=state,district=city,address=addr)
        db.session.add(entry)
        db.session.commit()
        flash(name+" "+pas+" "+adhar+" "+fname+" "+mname+" "+gen+" "+dob+" "+email+" "+phone+" "+state+" "+city+" "+addr+" ")
        return render_template('patient_register.html')

    return render_template('patient_register.html')

@app.route('/lsignup',methods=['GET','POST'])
def lsignup():
    if (request.method == 'POST'):
        name=request.form.get('reg_name')
        reg_no=request.form.get('reg_num')
        pas=request.form.get('pass')
        state = request.form.get('state')
        city = request.form.get('city')
        addr = request.form.get('adr')
        web = request.form.get('web')
        email=request.form.get('email')
        phone=request.form.get('ph_num')
        start=request.form.get('stime')
        end = request.form.get('etime')
        entry = sample_collection(regno=reg_no,regname=name,password=pas,state=state,district=city,address=addr,email=email,contact=phone,worktstart=start,worktend=end)
        db.session.add(entry)
        db.session.commit()
        flash(name+" "+reg_no+" "+pas+" "+state+" "+city+" "+addr+" "+web+" "+email+" "+phone+" "+start+" "+end)
        return render_template('sample_register.html')

    return render_template('sample_register.html')

@app.route('/tsignup',methods=['GET','POST'])
def tsignup():
    if (request.method == 'POST'):
        name=request.form.get('reg_name')
        reg_no=request.form.get('reg_num')
        pas=request.form.get('pass')
        state = request.form.get('state')
        city = request.form.get('city')
        addr = request.form.get('adr')
        email=request.form.get('email')
        phone=request.form.get('ph_num')
        notest=request.form.get('ntest')
        entry = testing_facility(regno=reg_no,regname=name,password=pas,state=state,district=city,address=addr,email=email,contact=phone,notest=notest)
        db.session.add(entry)
        db.session.commit()
        flash(name+" "+reg_no+" "+pas+" "+state+" "+city+" "+addr+" "+" "+email+" "+phone+" "+notest)
        return render_template('testing_register.html')

    return render_template('testing_register.html')