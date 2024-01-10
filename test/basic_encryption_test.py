import sys
import os
dirname = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(dirname, '..\\src')))
from gerbil import encryption

test = [("text/sample.txt", "sample_after_decryption"),
        ("video/video.mp4", "video_after_decryption"),
        ("dir/testdir", "testdir_after_decryption"),]
PASSWORD = "1234567890"

def test_encrypt_decrypt(file, password, rename=None):
    dir = os.path.dirname(file)
    #empty out everything in dir other than file
    for f in os.listdir(dir):
        if (f != os.path.basename(file)):
            os.remove(os.path.join(dir, f))

    encrypted_file = encryption.encrypt_file(file, password, False)
    print("Encrypted file: " + encrypted_file)
    decrypted_file = encryption.decrypt_file(encrypted_file, password, True, rename=rename)
    if (decrypted_file == None):
        print("Decryption failed")
    print("Decrypted file: " + decrypted_file)

if __name__ == "__main__":
    for file in test:
        test_encrypt_decrypt(os.path.join(dirname, file[0]), PASSWORD, rename=file[1])