
#import module to make forms
from flask import Flask
from werkzeug import secure_filename
from wtforms import Form, PasswordField, StringField, BooleanField, SelectField, TextAreaField, validators
from wtforms.validators import ValidationError, InputRequired, EqualTo, Length
#from flask_wtf import Form
#from flask_wtf.file import FileField, FileAllowed, FileRequired

def key_check(form,field):
    if len(field.data) < 6:
        raise ValidationError('Key must be at least 6 characters.')      

#def file_check(form,field):
    #filename = secure_filename(field.data.filename.lower())
    #ALLOWED_EXTENSIONS = set(['txt','fna'])
    #if field.data:
        #if not ('.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS): 
            #raise ValidationError('Wrong file-type, must be fna or txt.')
    #else:
       # raise ValidationError('Please open the DNA sequence.')
        
#form for encryption
class EncryptionForm(Form):
    message = TextAreaField('Message to be encrypted:', [InputRequired()])
    key = PasswordField('Choose your secret key:', [EqualTo('confirm_key', message='The keys must match.')])
    confirm_key = PasswordField('Re-enter key:', [InputRequired(), key_check])
            #Length(min=6, message='Key must be at least 6 characters.')])
    level = SelectField('Choose the level of encryption:', choices=[('1','Level 1'), ('2','Level 2'), ('3','Level 3'), ('4', 'Level 4')], validators=[InputRequired()])
    DNA_sequence = TextAreaField('Paste your DNA sequence:', [InputRequired()])
    
    # other options of input unable to successfully implement.
    #default_genome = BooleanField('Use the default genome sequence:') 
    #upload_genome = FileField('Open DNA sequence to be encrypted:', [validators.InputRequired(), file_check])
    
    
                                                  
#form for decryption
class DecryptionForm(Form):
    enter_key = PasswordField('Enter your secret key:', [InputRequired(), key_check])
    encrypted_DNA = TextAreaField('Paste the encrypted DNA sequence:', [InputRequired()])
    