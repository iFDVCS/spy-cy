
#import module to make forms
from flask import Flask
from wtforms import Form, StringField, BooleanField, SelectField, TextAreaField, validators
from flask_wtf import Form
from flask_wtf.file import FileField, FileAllowed, FileRequired

def key_check(Form,field):
    if len(field.data) < 6:
        raise validators.ValidationError('Key must be at least 6 characters.')
        
#form for encryption
class EncryptionForm(Form):
    message = TextAreaField('Message to be encrypted:    ', [validators.Required()])
    key = StringField('Choose your secret key:     ', [validators.Required(), key_check])
    level = SelectField('Choose the level of encryption:' , choices=[('type1','1'), ('type2','2'), ('type3','3'), ('type4', '4'), ('type5', '5')])
    upload_genome = FileField('Upload DNA sequence (txt/fna format):', validators=[FileAllowed(['txt','fna'], 'Please upload a txt or fna file')])
    default_genome = BooleanField('OR- Use default DNA sequence:')
    
#form for decryption
class DecryptionForm(Form):
    enter_key = StringField('Your secret key:', [validators.Required(), key_check])
    encrypted_genome = FileField('Upload the encrypted DNA sequence (txt/fna format):', validators=[FileRequired, FileAllowed(['txt','fna'], 'Please upload a txt or fna file')])
    