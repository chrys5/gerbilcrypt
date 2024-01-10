#use global system information (stuff that won't change), username, and name of site to generate a unique password using sha-256

import sys
import json
from hashlib import sha256

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*_-.?!@#$%&*_-.?"
header = "python main.py <identifier>"

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-e" and len(sys.argv) > 2:
        filler = ' '.join(sys.argv[2:])
        #save filler in config.json
        json.dump({"filler": filler}, open("config.json", "w"))
        print("Identifier message changed to: {filler}".format(filler=filler))

    try:
            filler = json.loads(open("config.json", "r").read())["filler"]
    except:
        json.dump({"filler": "<anything>"}, open("config.json", "w"))
        filler = "<identifier>"
        
    if not sys.argv[-1].isdigit():
        print("Usage: \n\
            \t {header} {filler} <length> \n\
            \t {header} -e <new filler message> \n\
            \t {header} -h".format(header=header, filler=filler))
        sys.exit(0)

    length = int(sys.argv[-1])
    hash = sha256(filler.join(sys.argv[1:]).encode()).hexdigest()
    while len(hash) < length*2:
        hash += sha256(hash.encode()).hexdigest()

    #generate length array of random numbers from 0 to len(ALPHABET) using hash
    idx = [int(hash[i:i+2], 16) % len(ALPHABET) for i in range(0, length*2, 2)]
    #use array to generate password
    password = ''.join([ALPHABET[i] for i in idx])
    print(password)
    
    sys.exit(0)