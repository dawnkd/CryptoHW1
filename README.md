# CryptoHW1

## Requirements

Python 3

NumPy

## Testing:

Firstly, run server.py(Python3) to initialize the server. Then, in another terminal on the same machine, run client.py. This can also be used on different machines by changing the IP and port which exists in both programs. When client.py is run, it will prompt you for a string, which will be encrypted using the DES. This will then be sent to the server, where it is decrypted by server.py. This is then printed out to the terminal, for the user to view. This could be used to send any encrypted string between two computers, provided both knew the 10-bit key beforehand.

## Implementation Details:
All of the DES implementation is written in DES.py. This code currently uses a static key, and will encrypt numpy arrays of 8 bits. Both the server and the client convert their strings back and forth from this 8-bit format to implement the DES. They then call the same DES.py functions to encrypt or decrypt the data they've received. This is currently implemented to use strings, but could easily be modified to accept any type of data, as strings are just a specific subset of binary data. 

Every element of this toy DES is written according to the specifications in the lecture slides. This implementation takes in 8 bit blocks, performs 2 rounds of DES, and has 2 non-linear elements in the two S-boxes. In addition, it uses xor operations, bit permutations, and shifts to further obscure the encryption. Most of the implementation is fairly simple, using standard numPy functions to accomplish most tasks. It was written in a manner to allow most of the implementation details to be tweaked, whether changing the S-boxes, the keys, permutations, or adding more rounds of DES. 

## Security:
Compared to a standard DES, this encryption is very weak. The first detail making it weak is the fact that it only encrypts blocks of 8 bits each. Without any other permutation used, this means that when encrypting string input, every character is encrypted independently, making it incredibly vulnerable to frequency analysis. This would essentially destroy this DES implementation given a long enough input, provided no additional changes were made. The best way to alleviate this is to permute the binary data before encryption, so at least strings wouldn't be that predictable. Additionally, compared to DES, this implementation doesn't do much substitution, given only 2 rounds with 2 s-boxes. This makes it more vulnerable to being predicted. To alleviate this problem, the simplest solution would just be to lengthen the input size, and include more non-linear elements to the DES. Lastly, the most important problem lies in the fact that the key is only 10 bits long. This means that there are only 1024 possible keys, creating a very small set to be brute-forced. This is the primary element making this DES implementation very weak, but coupled with the other weaknesses just compounds the problem. While a useful way to teach the principles of DES, this algorithm isn't going to be protecting any sensitive information any time soon.
