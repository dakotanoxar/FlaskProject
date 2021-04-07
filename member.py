from flask import Blueprint,render_template,url_for,request
import pymysql

mydb = pymysql.connect('localhost','root','','pythondb')

member = Blueprint('member',__name__)

@member.route('/showmember')
def Showdata():
    with mydb:
        cur = mydb.cursor()
        sql = "SELECT * FROM membertb"
        cur.execute(sql)
        rows = cur.fetchall()
        return render_template('showmember.html',datas="This is Member",members=rows)

@member.route('/editmember',methods=['POST'])
def Editmember():
    if request.method == "POST":
        id = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        sex = request.form['sex']
        bdate = request.form['bdate']
        email = request.form['email']
        with mydb:
            cur = mydb.cursor()
            sql = "UPDATE membertb SET mem_fname = %s,mem_lname = %s,mem_sex = %s,mem_bdate = %s,mem_email = %s,mem_id = %s"
            cur.execute(sql,(fname,lname,sex,bdate,email,id))
            mydb.commit()
            return "Update membertb"