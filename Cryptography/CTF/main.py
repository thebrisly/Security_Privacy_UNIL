import hashlib

prof_emails = ["benoit.garbinato@unil.ch", "mauro.cherubini@unil.ch"]
with open("/home/lfabbian/Security/Cryptography/CTFleaked_hashed_emails.txt", 'r') as file:
    lhe = file.read().splitlines()

print(lhe[0])
print(prof_emails[0])


#hashed_tm = hashlib.sha256(test_email.encode()).hexdigest()

#print(hashed_tm)