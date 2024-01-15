# gerbilcrypt

A simple file encryptor with cmd line interface. Three features are included: encryption, decryption, and secure deletion (although file data may still be present in swap space, caches, etc). The [cryptography](https://github.com/pyca/cryptography) libary was for much of the encryption/decryption mechanisms.

## Usage:

1. Run scripts/compile.sh to create *gerbil.exe* executable
2. Optional: add path to *gerbil.exe* to user path variable for easy terminal access
3. Run `gerbil --help` in terminal for help

```
usage: gerbil.exe [-h] [-d] [-r RENAME] [-rn] {encrypt,decrypt,delete} file [password]

a simple file encryptor

positional arguments:
  {encrypt,decrypt,delete}
                        the function to be executed
  file                  the file to be encrypted/decrypted
  password              the input password

options:
  -h, --help            show this help message and exit
  -d, --delete          delete the original file
  -r RENAME, --rename RENAME
                        rename file upon decryption
  -rn, --randomizename  randomize the name of the encrypted file (only works in encrypt mode)
```

## Examples:

```
gerbil encrypt message.txt pwpw1234 -d
```
will encrypt message.txt using key pwpw1234 to create encrypted file message.gerbil, while securely deleting message.txt. If no password is given as an argument, a password will be prompted.