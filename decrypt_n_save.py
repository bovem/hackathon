import os ,sys, time
import shutil
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


password_provided = sys.argv[1] # This is input in the form of a string
password = password_provided.encode() # Convert to type bytes
salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once


f_name = password_provided
source = './data/' + f_name
if not os.path.exists(source):
    os.makedirs(source)

for f in os.listdir(source): 
    destination = './data/temp/'
    if not os.path.exists(destination):
        os.makedirs(destination)
    dest = shutil.copy(source+'/'+f, destination) 
    
    
    
    print("After copying file:")  
    print(os.listdir(destination))
    print("Destination path:", dest)
    
    
    #time.sleep(5)
    input_file = './data/temp/'+f
    output_file = './data/temp/'+f
    with open(input_file, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(encrypted)
    
    print("File successfuly decrypted!!")
    sys.stdout.flush()

    

        
              