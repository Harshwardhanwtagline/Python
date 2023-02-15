import re

def valid_email(emails):
    pattern = r'\b[A-Za-z0-9._-]+@[A-Za-z0-9]+\.[A-Za-z]{2,3}\b'
    for i in emails[:]:
        if not bool(re.match(pattern, i)):
            emails.remove(i)
    return emails



if __name__ == "__main__":
    emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]
    print(valid_email(emails))