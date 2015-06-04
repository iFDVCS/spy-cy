#write the cell into a named python file rather than ipynb, may be used with flaskr

#import the required modules from flask
from flask import Flask, request, render_template, url_for, flash, session, redirect
from werkzeug import secure_filename

#import the form module created
from crypter_forms import EncryptionForm, DecryptionForm

#use the flask module to create an application
app = Flask(__name__)
app.config.from_object(__name__)

#UPLOAD_FOLDER = '/home/student/flaskr/uploads'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#set the route for each page.
#show the template rendered with the specific page.
@app.route('/')
def run_homepage():
    return render_template('homepage.html', title="Home")

@app.route('/encrypt', methods=('GET', 'POST'))
def run_encrypt():
    form = EncryptionForm(request.form)
    if request.method == 'POST' and form.validate():
        key = form.key.data
        message = form.message.data
        level = form.level.data
        #filename = secure_filename(form.upload_genome.file.filename)
        #fieldname = field.file.filename.lower()
        print(filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #form.upload_genome.data.save('home/student/flaskr/uploads/' + filename)
        #flash('Your message has been encrypted')
        return render_template('encrypt_result.html', title="Encrypt",form=form)
    else:
        return render_template('encrypt.html', title="Encrypt", form=form)

#@app.route('/encrypt_result', methods=('GET', 'POST'))
#def run_encrypt_result():
#    return render_template('encrypt_result.html', title="Encryption Result")

@app.route('/decrypt', methods=('GET', 'POST'))
def run_decrypt():
    form = DecryptionForm(request.form)
    if request.method == 'POST' and form.validate():
        enter_key = form.enter_key.data
        encrypted_genome = form.encrypted_genome.data
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