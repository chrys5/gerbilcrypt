## CMD Line Interface for encryption/decryption

import os
import argparse
import getpass

from gerbil.encryption import *

def init_parser():
    parser = argparse.ArgumentParser(
        description="a simple file encryptor",)
    parser.add_argument("function", 
                        help="the function to be executed", 
                        choices=["encrypt", "decrypt", "delete"])
    parser.add_argument("file",
                        help="the file to be encrypted/decrypted",
                        type=str)
    parser.add_argument("password",
                        nargs="?",
                        help="the input password",
                        type=str)
    parser.add_argument("-d", "--delete",
                        help="delete the original file",
                        action="store_true")
    parser.add_argument("-r", "--rename",
                        help="rename file upon decryption",
                        type=str)
    parser.add_argument("-rn", "--randomizename",
                        help="randomize the name of the encrypted file (only works in encrypt mode)",
                        action="store_true")
    return parser
    
if __name__ == "__main__":
    parser = init_parser()
    args = parser.parse_args()

    file = os.path.abspath(args.file)
    assert os.path.exists(file), "File or directory does not exist"
    password = args.password
    delete = args.delete
    rename = args.rename
    randomizename = args.randomizename

    if args.function == "encrypt":
        if password == None:
            password = getpass.getpass("Enter password: ")
        encrypted_file = encrypt_file(file, password, delete, rename)
        if randomizename:
            new_name = os.path.join(os.path.dirname(encrypted_file), os.urandom(12).hex().upper())
            os.rename(encrypted_file, new_name)
            encrypted_file = new_name
        print("Encrypted file: " + encrypted_file)
    
    if args.function == "decrypt":
        if password == None:
            password = getpass.getpass("Enter password: ")
        decrypted_file = decrypt_file(file, password, delete, rename)
        if decrypted_file == None:
            print("Decryption failed. Wrong password or file has been corrupted.")
        else:
            print("Decrypted file: " + decrypted_file)

    if args.function == "delete":
        secure_delete(file)
        print("File deleted.")