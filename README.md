# CryptoHW1


Testing:

Firstly, run server.py(Python3) to initialize the server. Then, in another terminal on the same machine, run client.py. This can also be used on different machines by changing the IP and port which exists in both programs. When client.py is run, it will prompt you for a string, which will be encrypted using the DES. This will then be sent to the server, where it is decrypted and printed in the terminal.

Implementation Details:
All of the DES implementation is written in DES.py. This code currently uses a static key, and will encrypt numpy arrays of 8 bits. Both the server and the client convert their strings back and forth from this 8-bit format to implement the DES.

Compared to a standard DES, this encryption is very weak. The first detail making it weak is the fact that it only encrypts blocks of 8 bits each. Without any other permutation used, this means that when encrypting string input, every character is encrypted independently, making it incredibly vulnerable to frequency analysis. This would essentially destroy this DES implementation given a long enough input, provided no additional changes were made. 
