import smtplib
import optparse


def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-s","--sender",dest="sender_mail",help="Enter the sender mail address")
    parse_object.add_option("-p","--password",dest="sender_password",help="Enter the sender password")
    parse_object.add_option("-t","--target",dest="target_mail",help="Enter the target mail address")
    parse_object.add_option("-m","--message",dest="message",help="Enter the message")
    (user_inputs,arguments) = parse_object.parse_args()
    return user_inputs

def send_email(my_email, target_email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com",587)
    email_server.starttls()
    email_server.login(my_email, password)
    email_server.sendmail(my_email, target_email, message)
    email_server.quit()

sender_mail = user_input().sender_mail
sender_password = user_input().sender_password
target_mail = user_input().target_mail
message = user_input().message

number = 0
while True:
    number +=1
    send_email(sender_mail,target_mail,sender_password,message)
    print("Sent mail: " + str(number))

#by G0khannn
