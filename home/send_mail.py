import MySQLdb
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .mysql import mysqldb

def mail_seder(receiver_email, user, event, date, place, flag):
    sender_email = "treeasurenss@gmail.com"
    password = 'treeasure@nss123'
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    # Create the plain-text and HTML version of your message
    if flag == 1:
        message["Subject"] = "Nature is calling you........"
        text = """\
        Hello """ + user + """
        We have a new event organized on """ + date + """.
        The name of the event is """ + event + """ organized at location """ + place + """.
        Do visit our website to participate.
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                We have a new event organized on """ + date + """.
                The name of the event is """ + event + """ organized at location """ + place + """.
                Do visit our website to participate.
            </p>
            </body>
        </html>
        """
    elif flag==0:
        message["Subject"] = "Nature is calling you........"
        
        mydb = mysqldb()
        mycursor = mydb.cursor()
        query = 'select info from schedule_tt where event_name="'+event+'"'
        mycursor.execute(query)
        result = mycursor.fetchall()
        text = """\
        Hello """ + user + """
        You are sucessfully registered to the event """ + event + """
        Details
        Date: """ + date + """
        Place: """ + place + """
        Information: """ + result[0][0] +"""
        Do visit our website to participate.
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                You are sucessfully registered to the event """ + event + """<br>
                Details<br>
                Date: """ + date + """<br>
                Place: """ + place + """<br>
                Information: """ + result[0][0] +"""<br>
                Do visit our website to participate.
            </p>
            </body>
        </html>
        """

    elif flag==6:
        mydb = mysqldb()
        mycursor = mydb.cursor()
        query = 'select time from schedule_tt where event_name="'+event+'"'
        mycursor.execute(query)
        result = mycursor.fetchall()
        message["Subject"] = "Event date has changed"
        
        text = """\
        Hello """ + user + """
        Details of the event """ + event + """
        in which you have participated has been changed
        Date: """ + date + """
        Place: """ + place + """
        Time: """ + result[0][0] +"""
        If you are not avaiable on that date, you can go to profile and delete your participation.
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                Details of the event  """ + event + """ in which you have participated has been changed<br>
                Date: """ + date + """<br>
                Place: """ + place + """<br>
                Time: """ + result[0][0] +"""<br>
                If you are not avaiable on that date, you can go to profile and delete your participation
            </p>
            </body>
        </html>
        """
    elif flag == 3:
        message["Subject"] = "We are disappointed"
        text = """\
        Hello """ + user + """
        You have been reported.
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                You have been reported
            </p>
            </body>
        </html>
        """
    elif flag == 4:
        message["Subject"] = "We are disappointed"
        text = """\
        Hello """ + user + """
        Your event """ + event + """ have been reported.
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                Your event """ + event + """ have been reported.
            </p>
            </body>
        </html>
        """
    elif flag == 5:
        message["Subject"] = "Welcome to TreeAsure"
        text = """\
        Hello """ + user + """
        Welcome to treeasure. Make sure you authenticate your account within 2 days of making your account. 
        On failing to do so will result in dismissal of your account. 
        If already authenticated during the registration process, kindly ignore this message
        To authenticate, Click here
        """
        html = """\
        <html>
            <body>
            <p>Hello """ + user + """,<br>
                Welcome to treeasure. Make sure you authenticate your account within 2 days of making your account. 
                On failing to do so will result in dismissal of your account. 
                If already authenticated during the registration process, kindly ignore this message
                To authenticate, <a href="https://forms.gle/7LXQsSb9HvZCf7m27">Click here </a>
            </p>
            </body>
        </html>
        """
    
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )


def send_email(username, event, date, place, flag):
    mydb = mysqldb()
    mycursor = mydb.cursor()
    print("++++++++++++++++++++++++++",flag)
    if flag == 0:
        query = 'select email, username from auth_user where username="'+username+'"'
    elif flag == 6:
        query = 'select email, name from schedule_participants where event_name="'+event+'"'
    else:
        query = 'select email, username from auth_user where not username="'+username+'"'
    mycursor.execute(query)
    result = mycursor.fetchall()
    
    for i in result:
        print(i[0], i[1])
        mail_seder(i[0], i[1], event, date, place, flag)