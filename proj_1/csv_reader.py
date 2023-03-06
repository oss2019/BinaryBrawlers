import csv

spam_list = [] # will append a dict containing name and email

with open(r"email_list.csv") as csv_file:
    email_list = csv.reader(csv_file)
    for ind, row in enumerate(email_list):
        if ind == 0:
            pass
        else:
            spam_list.append({
                "name": row[0],
                "email": row[1]
            })
