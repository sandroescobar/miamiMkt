from flask import Flask, render_template, request, session, flash, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors, re



app = Flask(__name__)
app.secret_key = "super secret key"

app.config['MYSL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "Ae9542790079"
app.config['MYSQL_DB'] = 'miamiPayroll2'

mysql =MySQL(app)


@app.route('/', methods = ['GET', 'POST'])
def login():
    msg = ''
    if request.method == "POST" and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password =  request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('''SELECT * FROM accounts WHERE email = %s AND password = %s''', (email, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True #Marks “this user is authenticated. and can be used later in session
            '''
             Saves the user’s primary key (from your accounts table) in the session, and 
             later you can grab session['id'] to fetch that user’s data without re-querying 
             for their credentials each time. for session['id']
            '''
            session['id'] = account['id']
            '''
            stores their email address in the session too, so you can display it in your 
            templates (e.g. “Welcome back, {{ session.email }}!”) or use it for audit/logging.
            '''
            session['email'] = account['email']
            msg = 'Logged in successfully!'
            print(msg)
            return  render_template('idek.html', msg =msg)
        else:
            msg = "email or password not found"
            flash(msg)
    return render_template('login.html')





@app.route('/sign_up', methods = ['POST', 'GET'])
def sign_up():
    msg = ''
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        print(f"received the email: {email} and password: {password}")
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE email = (%s)', (email,))
        account = cursor.fetchone()
        if account:
            msg = "account already exists attempt to login"

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "improper email format"
            flash(msg)


        else:
            cursor.execute(
                ''' 
                INSERT INTO accounts(email, password)
                VALUES(%s, %s)
                ''',(email, password))
            mysql.connection.commit()
            msg = "you successfully created an account"
            flash(msg)
            # use redirect after handling a post as render_template won't redirect the user
            return redirect(url_for('login'))


    return render_template('sign_up.html')


@app.route('/idek', methods = ['POST','GET'])
def idek():
    return render_template('idek.html')

if __name__ == "__main__":
    app.run(debug=True)





