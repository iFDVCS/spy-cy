
#import module to make forms
from flask import Flask
from werkzeug import secure_filename
from wtforms import Form, StringField, BooleanField, SelectField, TextAreaField, validators
from wtforms.validators import ValidationError
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

def key_check(form,field):
    if len(field.data) < 6:
        raise ValidationError('Key must be at least 6 characters.')
    
def file_check(form,field):
    #filename = secure_filename(Form.upload_genome.data.filename)
    #filename = field.data.lower()
    #filename = secure_filename(form.upload_genome.data)
    filename = secure_filename(field.file.filename.lower())
    ALLOWED_EXTENSIONS = set(['txt','fna'])
    if field.file:
        if not ('.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS): 
            raise ValidationError('Wrong file-type, must be fna or txt.')
    #else:
       # raise ValidationError('Please open the DNA sequence.')
        
    
#form for encryption
class EncryptionForm(Form):
    message = TextAreaField('Message to be encrypted:', [validators.Required()])
    key = StringField('Choose your secret key:', [validators.Required(), key_check])
    level = SelectField('Choose the level of encryption:' , choices=[('type1','1'), ('type2','2'), ('type3','3'), ('type4', '4'), ('type5', '5')])
    upload_genome = FileField('Open DNA sequence to be encrypted:', [validators.Required(), file_check])
    #default_genome = BooleanField('Use default DNA sequence:')
    
#form for decryption
class DecryptionForm(Form):
    enter_key = StringField('Your secret key:', [validators.Required(), key_check])
    encrypted_genome = FileField('Open the encrypted DNA sequence:', validators=[file_check])
    