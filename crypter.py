#write all the code from this cell into a python file, of a set name and directory.
#running this file in the command line will launch the application.

#import the required modules from flask
from flask import Flask, request, render_template, url_for, flash, session, redirect
import jinja2

#import the form module created in the crypter_forms.py file.
from crypter_forms import EncryptionForm, DecryptionForm

#import the modules with encrypt and decrypt functions in the encrypt.py and decrypt.py file.
import encrypt as en
from decrypt import decrypt

#use the flask module to create an application
app = Flask(__name__)
app.config.from_object(__name__)

#app route sets the route for each page of the website.
#each page renders the corresponding html file, all extend from template.html to give a uniform website.
#give each page a unique title to display on the website.

#home page of DNA-Crypter 
@app.route('/')
def run_homepage():
    return render_template('homepage.html', title="Home")

#encrypt page, uses the EncryptionForm imported from the other module.
#returns the encrypt_result render if the HTTP method is POST (form is being submitted), and the form is valid with no errors.
#encrypt_result extends from encrypt template, remaining on the same page.
#takes the data from the form, adds to variables for message, key, level and DNA_sequence.
#this data is used in the encrypt function to give a result, the encrypted DNA sequence, which is passed onto the encrypt_result template.
#else returns the encrypt template render, keeping the same page if the HTTP method is GET or thr form is invalid.
@app.route('/encrypt', methods=('GET', 'POST'))
def run_encrypt():
    form = EncryptionForm(request.form)
    if request.method == 'POST' and form.validate():
        message_input = form.message.data
        key_input = form.key
        level_input = form.level
        DNA_sequence_input = form.DNA_sequence.data
        DNA_sequence_input = DNA_sequence_input.strip()
        return render_template('encrypt_result.html', title="Encrypt", form=form, result = en.encrypt(message_input, key_input, level_input, DNA_sequence_input))  
    else:
        return render_template('encrypt.html', title="Encrypt", form=form)

#decrypt page, same theory as the encrypt page above.
#data gives a result, the decrypted message, which is passed to the decrypt_result template.
@app.route('/decrypt', methods=('GET', 'POST'))
def run_decrypt():
    form = DecryptionForm(request.form)
    if request.method == 'POST' and form.validate():
        enter_key_input = form.enter_key
        encrypted_DNA_input = form.encrypted_DNA
        return render_template('decrypt_result.html', title="Decrypt", form=form, result = decrypt(enter_key_input, encrypted_DNA_input))
    else:
        return render_template('decrypt.html', title="Decrypt", form=form)

#help page
@app.route('/help')
def run_help():
    return render_template('help.html', title="Help")

#about page
@app.route('/about')
def run_about():
    return render_template('about.html', title="About")

#set the secret key for the application
app.secret_key = '\x90,\xd7\n\xf5\xe0\r,\x1a\x18\xda\xd40\x11\xe9Q\xe3\xbc\xc6\xf7'

#runs the local server (http://127.0.0.1:5000) with the application
#de-bug enabled
if __name__ == '__main__':
    app.run(debug=True)