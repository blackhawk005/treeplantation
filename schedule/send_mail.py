import MySQLdb
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def mail_seder(receiver_email, user, event, date, place, flag):
    sender_email = "treeasurenss@gmail.com"
    password = 'treeasure1234'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Nature is calling you........"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    if flag == 1:
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
        mydb = MySQLdb.connect(
        "localhost",
        "root",
        "",
        "plantation"
        )
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
    mydb = MySQLdb.connect(
        "localhost",
        "root",
        "",
        "plantation"
    )
    mycursor = mydb.cursor()
    print(username)
    if flag == 0:
        query = 'select email, username from auth_user where username="'+username+'"'
    else:
        query = 'select email, username from auth_user where not username="'+username+'"'
    mycursor.execute(query)
    result = mycursor.fetchall()
    for i in result:
        print(i[0], i[1])
        mail_seder(i[0], i[1], event, date, place, flag)