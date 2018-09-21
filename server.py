import DES
import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 8123



def decrypt_string(input_bits):
	to_decrypt = np.array(list(input_bits)).reshape(-1,8).astype(np.uint8)
	decrypted = np.apply_along_axis(DES.apply, 1, to_decrypt, DES.key_test,False).astype(np.uint8)
	packed = np.packbits(decrypted);
	return "".join([chr(item) for item in packed])


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn,addr = s.accept()
	with conn:
		print("Connection received from {}".format(addr))
		data = conn.recv(1024).decode('utf_8')
		print(decrypt_string(data))
