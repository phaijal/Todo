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


def add_task(heading, task):
    task_name = taskname(task=task, done=False)
    t = Tasks.objects.get(heading=heading)
    t.tasks.append(task_name)
    t.save()


def mark_complete(heading, task):
   # Task.objects(task=tas).update(done=True)
    t = Tasks.objects.get(heading=heading)
    for a in t.tasks:
        if a.task == task:
            a.done = True
    t.save()
"""



def add_task(task):
    Tasks(task=task, done=False).save()



def get_tasks():
    tasks = []
    for task in Task.objects:
        tasks.append(task.task)
    return tasks


def mark_complete(tas):
    Task.objects(task=tas).update(done=True)
    task = Task.objects(task=tas)
    print(task)
   # task[0].done= True
 #   task.done = True
   # Task.save(self)
"""
"""




class Todo(object):
    def add(self, task):
        collection.insert_one({"task": task, "done": False})
        ret_json = {
            "msg": "Added Task"
        }
        return ret_json

    def get(self):
        return collection.find({}, {"task": 1, "done": 1, "_id": 0})

    def markcomp(self,task):
        myquery = {"task": task}
        newvalues = {"$set":
            {
                "done": True
            }
        }
        collection.update_one(myquery, newvalues)
        ret_json = {
            "msg": f"{task}, status: Completed"
        }
        return ret_json
        
"""
