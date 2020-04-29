



with open("emails.txt") as file: 
    content = file.read()

emails = content.split(',') 

duplicate_free_emails = []

for individual_email in emails:
    # if email is not in duplicate free array then add that email to the duplicate free array 
    if individual_email not in duplicate_free_emails:
        duplicate_free_emails.append(individual_email)

print(duplicate_free_emails)