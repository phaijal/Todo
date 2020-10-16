from mongoengine import *

connect(host='mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/dbname?retryWrites=true&w=majority')


class taskname(EmbeddedDocument):
    task = StringField()
    done = BooleanField()


class Tasks(Document):
    heading = StringField(required=True)
    tasks = ListField(EmbeddedDocumentField(taskname))
    t = StringField()


def add_heading(heading):
    Tasks(heading=heading).save()


def get_all_task_object():
    return Tasks.objects()


def get_task_object(heading):
    return Tasks.objects.get(heading=heading)


def save_task_object(t):
    t.save()
