
from mongoengine import *

class info(EmbeddedDocument):
	Age = StringField()
	Born = StringField()


class User(Document):

	Username = StringField(max_length= 20, required= True)
	Password  = LongField()
	information = (EmbeddedDocumentField(info))