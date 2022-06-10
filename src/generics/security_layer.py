from Crypto.Cipher import AES
from src.generics.utils_functions import get_config_file_data

config,config_file = get_config_file_data()
config.read(config_file)

#secret_key:bytes = str.encode(config._defaults['secret_key'])
secret_key:bytes = str.encode('14qrM8312Qht2jA8')

def get_decoded_data(nonce,ciphertext:str, tag:str):
    cipher = AES.new(secret_key, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)
    return data.decode("utf-8")

def cipher_data(data:str):
    cipher = AES.new(secret_key,AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    return (cipher.nonce,ciphertext, tag)