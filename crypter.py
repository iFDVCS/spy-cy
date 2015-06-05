# write the cell into a named python file rather than ipynb, may be used with flaskr

# import the required modules from flask
from flask import Flask, request, render_template, url_for, flash, session, redirect
from werkzeug import secure_filename
import os

#import the form module created
from crypter_forms import EncryptionForm, DecryptionForm
from crypter_config import init_db

#use the flask module to create an application
app = Flask(__name__)
app.config.from_object(__name__)

#UPLOAD_FOLDER = '/C:/flaskr/uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# set the route for each page.
# show the template rendered with the specific page.
@app.route('/')
def run_homepage():
    return render_template('homepage.html', title="Home")

#@app.route('/encrypt_result', methods=('GET', 'POST'))
#def run_encrypt_result():
#    return render_template('encrypt_result.html', title="Encryption Result")

message_input = ""

@app.route('/encrypt', methods=('GET', 'POST'))
def run_encrypt():
    form = EncryptionForm(request.form)
    global message_input
    message_input = ""
    #if form.validate_on_submit():
    if request.method == 'POST' and form.validate():
        #dict = {}
        #dict['key_input'] = 'form.key.data'
        #key_input.save('/C:/flaskr/uploads/key_save.txt')
        message_input = "form.message.data"
        #level_input = 'form.level.data'
        #test = ''
        #global test 
        #test = 'testing'
        #filename = secure_filename(form.upload_genome.file.filename)
        #fieldname = field.file.filename.lower()
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #form.upload_genome.data.save('home/student/flaskr/uploads/' + filename)
        return render_template('encrypt_result.html', title="Encrypt", form=form)
        #return url_for('run_encrypt_result')
    else:
        return render_template('encrypt.html', title="Encrypt", form=form)


@app.route('/decrypt', methods=('GET', 'POST'))
def run_decrypt():
    form = DecryptionForm(request.form)
    if request.method == 'POST' and form.validate():
        enter_key = 'form.enter_key.data'
        encrypted_DNA = 'form.encrypted_DNA.data'
        return render_template('decrypt_result.html', title="Decrypt", form=form)
    else:
        return render_template('decrypt.html', title="Decrypt", form=form)

#@app.route('/decrypt_result', methods=('GET', 'POST'))
#def run_decrypt_result():
#    return render_template('decrypt_result.html', title="Decryption Result")

@app.route('/help')
def run_help():
    return render_template('help.html', title="Help")

@app.route('/about')
def run_about():
    return render_template('about.html', title="About")

#set the secret key for the app
app.secret_key = '\x90,\xd7\n\xf5\xe0\r,\x1a\x18\xda\xd40\x11\xe9Q\xe3\xbc\xc6\xf7'

#run the local server with the application
#de-bug enabled
if __name__ == '__main__':
    app.run(debug=True)