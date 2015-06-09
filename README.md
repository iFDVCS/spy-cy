# spy-cy

The aim of the spy-cy project was to develop a web application able to encrypt a message into a DNA sequence, then encrypt this message using a specified key. 
The point of this is to enable anyone to send a message through DNA alone in or within cells, and also possible applications in spy/secret communication or DNA digital data storage. The advantages of DNA cryptography is that DNA has a long lifespan to hold a message, and it can contain an extremley high density of data (compared to other storage e.g. hard drives).

We achieved this with our web application: **DNA-Crypter**. 
The app encrypt page takes user input of a message, key, level of encryption, and DNA sequence, and encrypts the message in the DNA. The app decrypt page takes user input of an encrypted DNA sequence and the specific key, and decrypts the message.
Four levels of encryption and decryption exist of varying levels of complexity: level 1 - level 4. 
These utilise the algorithms: Caesar, Vigenere, Hill, and AES.

How to set up:
* Install in the command line: Python, Flask, and WTForms (e.g. pip install Flask).
* Download all the files in this iFDVCS/spy-cy repository, place in a folder.
* In the command line, change the directory the the folder containing all the files.

How to run DNA-Crypter:
* In the command line type 'python crypter.py'.
* Click on the link to the DNA-Crypter webpage (e.g. http://127.0.0.1:5000/)
* Have a go at encrypting and decrypting a message into a DNA sequence, use the Help and About pages available.
* Stop the web application with Ctrl + C.

Good-luck encrypting and decrypting your DNA message! 
Try sending the encrypted DNA sequence to a friend for them to decrypt (as well as the secret key) :)


From the Spy-cy team: Joanna, Anna and Andjelika.
