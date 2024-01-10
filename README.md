### a simple file encryptor

to use:
1. run scripts/compile.sh to create executable
2. add executable path to user environment variables
3. run `gerbil -h` in terminal for help

ex. 
  `gerbil encrypt message.txt pwpw1234 -d`
will encrypt message.txt using key pwpw1234 to create encrypted file message.gerbil, while deleting message.txt
