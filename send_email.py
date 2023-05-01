import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "Dannybui5155@gmail.com"
    with open(".env", 'r') as file:
        unsorted = file.read().split("=")
        password = unsorted[1]
        # print(password)
    receiver = "Dannybui5155@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)



