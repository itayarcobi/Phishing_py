#! /usr/bin/python
#Itay_Arcobi_313260382
import os
import smtplib
import sys
import urllib.request 
import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
SERVER= "localhost"
FROM="billg@msn.com"
TO= [sys.argv[1]+"@"+sys.argv[2]]
mes_type = sys.argv[4]
# port = 465  
# smtp_server = "smtp.gmail.com"
# sender_email = "my@gmail.com"  
# receiver_email = "your@gmail.com" 
# password = input
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

if os.path.isfile(mes_type):
            text_file = open(mes_type, "r")
            data = text_file.read()
            text_file.close()
            TEXT= f"Hello {sys.argv[1]} the {sys.argv[3]}!\n"+data

else: 
        try:
                status_code = urllib.request.urlopen(mes_type).getcode()
                website_is_up = status_code == 200
                if website_is_up==True:
                        url = mes_type
                        html = urlopen(url).read()
                        soup = BeautifulSoup(html, features="html.parser")
                        for script in soup(["script", "style"]):
                                script.extract()    
                        text = soup.get_text()
                        lines = (line.strip() for line in text.splitlines())
                        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                        text = '\n'.join(chunk for chunk in chunks if chunk)
                        TEXT=text
        except:
                TEXT= f"Hello {sys.argv[1]} the {sys.argv[3]}!\n"+mes_type


    
	
SUBJECT= "Hello :)"


msg = MIMEMultipart()
msg['From'] = FROM
msg['To'] =COMMASPACE.join(TO)
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = SUBJECT
 
msg.attach( MIMEText(TEXT) )
part = MIMEBase('application', "octet-stream")
part.set_payload( open(os.path.join(sys.path[0],"attach_create.py"),"rb").read() )
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"'
                % os.path.basename(os.path.join(sys.path[0],"attach_create.py")))
msg.attach(part)
server=smtplib.SMTP(SERVER)
server.sendmail(FROM,TO, msg.as_string())
server.quit()
