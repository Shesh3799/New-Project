from utilities import *
@app.route('/ldash',methods=['GET','POST'])
def staff_dashboard():
    if (session.get('lid')):
        query = bookings.query.filter_by(lid=session.get('lid')).all()
        if (request.method == 'POST'):

            if(request.form.get('1')):
                pid=request.form.get('pid')
                slot=request.form.get('slot')
                user = bookings.query.filter_by(pid=pid).first()
                user.status=1
                user.alloted_date=slot
                db.session.commit()
            else:
                pid=request.form.get('pid')
                res=request.form.get('res')
                print(res)
                if(res=="2"):
                    k = patient.query.filter_by(pid=pid).first()
                    k.book_stat = int(0)
                    user = bookings.query.filter_by(pid=pid).first()
                    user.sample_status=int(res)
                    db.session.commit()
                    print(k.book_stat)
                else:
                    user = bookings.query.filter_by(pid=pid).first()
                    user.sample_status = int(res)
                    db.session.commit()


        return render_template('staff_dashboard.html',query=query,name=session.get('lid'))
    return render_template('sample_login.html')


@app.route('/ldash2',methods=['GET','POST'])
def staff_dashboard2():
    if (session.get('lid')):
        query = bookings.query.filter_by(sample_status=1)
        if (request.method == 'POST'):
            pid = request.form.get('pid')
            res = request.form.get('res')
            user = bookings.query.filter_by(pid=pid).first()
            user.result= int(res)
            db.session.commit()


            return render_template('staff_dashboard2.html',query=query,name=session.get('lid'))
        return render_template('staff_dashboard2.html',query=query,name=session.get('lid'))
    return render_template('sample_login.html')

@app.route('/pdash',methods=['GET','POST'])
def patient_dashboard():
    if (session.get('pid')):
        query = patient.query.filter_by(email=session.get('pid')).first()
        return render_template('patient_dashboard.html', query=query)

    return render_template('patient_login.html')

@app.route('/pdash2',methods=['GET','POST'])
def patient_dashboard2():
    if (session.get('pid')):
        query = patient.query.filter_by(email=session.get('pid')).first()
        if (request.method == 'POST'):
            f=request.form
            res=0
            for i in f.keys():
                for j in f.getlist(i):
                    res+=float(j)
            res=res/10
            res*=100
            res=str(res)+"%"
            flash("Your Infection Percentage is : "+res[:5]+"%")
            user = patient.query.filter_by(email=session.get('pid')).first()
            user.infection = res[:5]
            db.session.commit()
            return render_template('patient_dashboard2.html',query=query)
        return render_template('patient_dashboard2.html', query=query)

    return render_template('patient_login.html')

@app.route('/pdash3',methods=['GET','POST'])
def patient_dashboard3():
    if (session.get('pid')):
        query = patient.query.filter_by(email=session.get('pid')).first()
        search = "{}%".format(query.pincode[:3])
        query1 = sample_collection.query.filter(sample_collection.pincode.like(search)).all()
        if(query.book_stat==1):
            query1 = bookings.query.filter_by(pid=query.pid).first()
            query2=sample_collection.query.filter_by(regno=query1.lid).first()
            return render_template('patient_dashboard3.html', query=query, query1=query1,query2=query2)

        if (request.method == 'POST'):
            f=request.form
            res=0
            lid=request.form.get('lid')
            pid =request.form.get('pid')
            print(lid,pid)
            i=patient.query.filter_by(pid=pid).first()
            j=sample_collection.query.filter_by(regno=lid).first()
            x=datetime.now()
            x=str(x)
            entry = bookings(lid=lid,pid=pid, name=i.adharname, contact=i.contact, risk=i.infection,request_date=x[:19],alloted_date="None",status=0,sample_status=0,result=0)
            i.book_stat = 1
            db.session.add(entry)
            db.session.commit()
            return render_template('patient_dashboard3.html',query=query,query1=query1)
        return render_template('patient_dashboard3.html', query=query,query1=query1)

    return render_template('patient_login.html')