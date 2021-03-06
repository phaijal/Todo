from mongoengine import *

connect(host='mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/dbname?retryWrites=true&w=majority')


class taskname(EmbeddedDocument):
    task = StringField()
    done = BooleanField()


class Tasks(EmbeddedDocument):
    heading = StringField(required=True)
    tasks = ListField(EmbeddedDocumentField(taskname))
    t = StringField()

class people(Document):
    name = StringField()
    section = ListField(EmbeddedDocumentField(Tasks))
    t= StringField()


def add_people(name):
    people(name=name).save()


def get_people(name):
    return people.objects.get(name=name)


def add_heading(person,heading):
    p = get_people(person)
    T=Tasks(heading=heading)
    p.section.append(T)
    p.save()


def get_heading(name):
    return people.objects.get(name=name)


def get_task_object(name):
    p = people.objects.get(name=name)
    return p


