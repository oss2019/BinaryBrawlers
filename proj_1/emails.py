from smtplib import SMTP
from email.message import EmailMessage

from news import collected_data
from csv_reader import spam_list

email_id = "erlbman564@gmail.com"

with open(r"final\pass", mode="r") as fi: # Never upload this pass file on any medium online
    password = fi.readline()

content = ""

for ind, data_point in enumerate(collected_data):
    content += f"{ind+1}) {data_point['title']}\n{data_point['link']}\n\n"

content += "Regards,\nErlic Bachman"

with SMTP(host="smtp.gmail.com", port=587) as smpt:
    smpt.ehlo()
    smpt.starttls()
    smpt.login(user=email_id, password=password)
    for target in spam_list:
        intro = f"Hello {target['name']},\n\n"
        email = EmailMessage()
        email["From"] = "Erlic Bachman"
        email["Subject"] = "Your Daily News Letter is here"
        email["To"] = target["email"]
        email.set_content(intro + content)
        smpt.send_message(email)
    print("Done")
