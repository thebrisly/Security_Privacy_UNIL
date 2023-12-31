#in this exercise we downloaded a file (transmission-4.0.4-x64.msi) and we need to verify the integrity of the file
#if we need to calculate the hash for this file and the compare it with the one on the website
#if they are the same, it means that the data have NOT been compromised and that the download is ok

# the hash of the file shoud be : 9120ab6e93b946841a7249e763ad54a851103e8bcc5121dac49c0b3676493ba5 (SHA 256)
#let's try to calculte the hash with a little program :

import hashlib as h

downloaded_file = "transmission-4.0.4-x64.msi"
original_hash = "9120ab6e93b946841a7249e763ad54a851103e8bcc5121dac49c0b3676493ba5"

sha256_hash = h.sha256()

with open(downloaded_file, "rb") as f:
    # decompose the file in little pieces to economize memory
    while chunk := f.read(8192):
        sha256_hash.update(chunk)

df_hash = sha256_hash.hexdigest()

#testing if the two hash are the same
print("The hash of '", downloaded_file,  "' is : ", df_hash)
if df_hash == original_hash :
    print("SUCCESSFUL - it's the same hash !")
else :
    print("not the same hash... you are fucked")