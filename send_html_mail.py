##Author : Sarani Bhattacharya
##Date:    9th-Dec-2019

##This Python script sends the content of a CSV file as an HTML table to your mail.

import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
me = "example@yourdomain.com"
you = "sarani.bhattacharya@yourdomain.com"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

html = """
 
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>html title</title>
  <style type="text/css" media="screen">
    table{
        border-collapse: collapse;
        empty-cells:hide;
    }
    td, th {
		border: 1px solid black;
		text-align: center;
	}
	thead{
		background-color: #3498eb;
		color: black;
		margin-left: 1%;
		margin-right: 1%;
		text-align: center;
	}
	p {
		font-weight: bold;
		font-family: "Times New Roman", Times, serif;
		font-size: large;
	}
  </style>
"""

filename="/home/sbhattacharya/py_in_file.csv"
df_marks=pd.read_csv(filename)
html_tab = df_marks.to_html(index=0)

html +="<p>Here goes you heading </p>"
html += html_tab

mailbody = MIMEText(html, 'html')
msg.attach(mailbody)
s = smtplib.SMTP('localhost')
s.sendmail(me, you, msg.as_string())
s.quit()
