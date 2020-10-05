import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('lucianogvda02@gmail.com', 'K@x7iktv')
    