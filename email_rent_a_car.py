from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class Email:
    def __init__(self,client_email,name,id_client,price):
        self.client_email=client_email
        self.name=name
        self.client_id=id_client
        self.price = price
        
    def email_open_rent(self):
    
        email ='rentacarpython@gmail.com'
        password  ='rentacar2021'

        #configure html email template to send
        with open ('email_template.html','r') as html:
            template = Template(html.read())
            body_msg = template.substitute(client_name=self.name,id_rent=self.client_id,price=100)



        # email configuration
        msg = MIMEMultipart()
        msg['from'] = 'Rent A Car Administration'
        msg['to'] = self.client_email
        msg['subject'] = 'Rent Information'

        #config template
        body = MIMEText(body_msg,'html')
        msg.attach(body)

        #send email
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            #msg hello to server
            smtp.ehlo()
            #start
            smtp.starttls()
            #login
            smtp.login(email,password)
            #send
            smtp.send_message(msg)
            #smtp.sendmail(email,client_email,msg)
    
    def email_close_rent(self):
    
        email ='rentacarpython@gmail.com'
        password  ='rentacar2021'

        #configure html email template to send
        with open ('email_template_close.html','r') as html:
            template = Template(html.read())
            body_msg = template.substitute(client_name='nome do client',id_rent=3)



        # email configuration
        msg = MIMEMultipart()
        msg['from'] = 'Rent A Car Administration'
        msg['to'] = self.client_email
        msg['subject'] = 'Rent Information'

        #config template
        body = MIMEText(body_msg,'html')
        msg.attach(body)

        #send email
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            #msg hello to server
            smtp.ehlo()
            #start
            smtp.starttls()
            #login
            smtp.login(email,password)
            #send
            smtp.send_message(msg)
            #smtp.sendmail(email,client_email,msg)

