## encode() is used to convert the text into a sequence of bytes (binary representation)
## hexdigest() is used to convert the hash into a hexa decimal notation othwerwise it will output an md5 object

import hashlib as h

text_to_hash = input("Give me a text that I need to hash: ")
md5_hash = h.md5(text_to_hash.encode()).hexdigest()
print("Le hash de '", text_to_hash, "' équivaut à ", md5_hash)

#you can run this program as much as you want, the hash will be ALWAYS the same for a text
#proof :
fixed_text = "hello"
fixed_md5_hash = h.md5(fixed_text.encode()).hexdigest()
print("Le hash de '", fixed_text, "' équivaut à ", fixed_md5_hash)