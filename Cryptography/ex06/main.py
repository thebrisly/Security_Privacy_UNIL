import hashlib

hashed_phone_numbers = {
    "participants": [
        {
            "work phone": "4c48cb6ac1fca984ff41bcd1888d01e5",
            "mobile phone": "aa40f062b5b7e40e139faf7f9ef8f5e6",
            "contacts": ["044768b20fc6cce49d9ab13a8ebc6ae9", "364600351ad65479697bd06b714a649c", "1f5c308421c857a7fe32a878ddb20967"]
        },
        {
            "work phone": "785f7d94d4bfceb1e954b724cf01d4c0",
            "mobile phone": "64939f75ab752856a75fcfd731baf8ea",
            "contacts": ["3bc47f97d5b7805af2f75bf28b4334e4", "25e1577a6534156615bbe17a37798316"]
        }
    ]
}

# I found the work phone of Noé on the internet. It's this one :
num_str = "0216923314"

# from this one i will try to find the salt
# Iteration on all the possible combination of 6 numbers :
for salt in range(1000000):  # 000000 - 999999
    salt_str = str(salt).zfill(6) 

    combined_string = num_str + salt_str

    hashed = hashlib.md5(combined_string.encode()).hexdigest()

    for participant in hashed_phone_numbers["participants"]:
        if hashed in [participant["work phone"], participant["mobile phone"]] or hashed in participant["contacts"]:
            print(f"SALT : {salt_str}")
            print(f"PHONE NUMBER : {num_str}")
            break

###############################################33¨

# Now we want to find his mobile phone !
# Time to do the reverse test :

salt_str = "737737"
prefix_str = "07"

for number in range(100000000):
    mobile_phone_str = str(number).zfill(8)

    new_combined_string = prefix_str + mobile_phone_str + salt_str

    new_hashed = hashlib.md5(new_combined_string.encode()).hexdigest()
    for participant in hashed_phone_numbers["participants"]:
        if new_hashed in participant["mobile phone"]:
            print(f"SALT : {salt_str}")
            print(f"PHONE NUMBER : {mobile_phone_str}")

########################################################

# Let's visually try to know which of these two numbers are the one of Noé

phone_number1 = "0778889900" + "737737"
phone_number2 = "0791337633" + "737737"
work_number = "0216923314" + "737737"

hash_ph1 = hashlib.md5(phone_number1.encode()).hexdigest()
hash_ph2 = hashlib.md5(phone_number2.encode()).hexdigest()
hash_work = hashlib.md5(work_number.encode()).hexdigest()

print("HASH for 0778889900 : ", hash_ph1)
print("HASH for 0791337633 : ", hash_ph2)
print("HASH for work phone : ", hash_work)