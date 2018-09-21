import numpy as np
import DES
import socket
HOST = '127.0.0.1'
PORT = 8123

def encrypt_string(input_str):
	to_encrypt = np.unpackbits(bytearray(input_str,'utf_8')).reshape(-1,8)
	encrypted = np.apply_along_axis(DES.apply, 1, to_encrypt, DES.key_test,True).astype(np.uint8)
	return "".join(encrypted.flatten().astype(str).tolist())


print("Enter string to encrypt and send:")
data = input()
encrypted = encrypt_string(data)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(encrypted.encode("utf-8"))