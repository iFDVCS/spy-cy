#write all the code from this cell into a python file, of a set name and directory.

#import the flask module, and wtforms to make forms.
#import the various Fields and validators from wtforms, required for the form.
from flask import Flask
from wtforms import Form, PasswordField, StringField, BooleanField, SelectField, TextAreaField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length

#did not get FileField working to upload a DNA sequence file, instead just used TextAreaField - kept code if you wanted to see
#from flask_wtf import Form
#from flask_wtf.file import FileField, FileAllowed, FileRequired 
#from werkzeug import secure_filename

#checks if the file uploaded with TextAreaField is the correct format, did not use.
#the wtform and flask-wtf were interfering with each other preventing the form from being validated.
#def file_check(form,field):
    #filename = secure_filename(field.data.filename.lower())
    #ALLOWED_EXTENSIONS = set(['txt','fna'])
    #if field.data:
        #if not ('.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS): 
            #raise ValidationError('Wrong file-type, must be fna or txt.')
    #else:
       # raise ValidationError('Please open the DNA sequence.')
    
#function to check that the key inputted from the form is less than 6 characters, if so gives validation error.
#no error given if the key is greater than 5 characters - sufficiently long to maintain security of the decryption.
def key_check(form,field):
    if len(field.data) < 6:
        raise ValidationError('Key must be at least 6 characters.')    
    
#check if DNA sequence input is only composed of A, T, G, C.
#if the DNA sequence they put in contains any other character, gives error.
#note: is also able to encrypt an empty genome (so just the message into DNA).
def dna_check(form,field):
    characters = []
    dna = field.data
    dna = dna.strip()
    characters = list(dna)
    for i in characters:
        if (i != "A") and (i != "T") and (i != "G") and (i != "C") and (i != "a") and (i != "t") and (i != "g") and (i != "c") and (i != "\r"):
            raise ValidationError('DNA sequence must be composed of A, T, G, or C only.')
    
#form for encryption using wtform functions.
#takes the information of the message and DNA sequence with a Text area box.
#takes the information of the key with a password box, does not show characters while typing to keep security of key.
#key is input twice and checks that they are the same with EqualTo, if not gives error.
#takes the information of level of encryption with a Select field, giving 4 choices of level.
#InputRequired ensures that section of the form is filled, if not will give error.
class EncryptionForm(Form):
    message = TextAreaField('Message to be encrypted:', [InputRequired()])
    key = PasswordField('Choose your secret key:', [EqualTo('confirm_key', message='The keys must match.')])
    confirm_key = PasswordField('Re-enter key:', [InputRequired(), key_check])
    level = SelectField('Choose the level of encryption:', choices=[('1','Level 1'), ('2','Level 2'), ('3','Level 3'), ('4', 'Level 4')], validators=[InputRequired()])
    DNA_sequence = TextAreaField('Paste your DNA sequence:', [dna_check])
    
#other options of form input unable to successfully implement.
    #default_genome = BooleanField('Use the default genome sequence:') 
    #upload_genome = FileField('Open DNA sequence to be encrypted:', [validators.InputRequired(), file_check])
    
                                                  
#form for decryption using wtform functions.
#same theory as in the encryption form above.
class DecryptionForm(Form):
    enter_key = PasswordField('Enter your secret key:', [InputRequired(), key_check])
    encrypted_DNA = TextAreaField('Paste the encrypted DNA sequence:', [InputRequired(), dna_check])