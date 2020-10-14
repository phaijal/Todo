from mongoengine import *

connect('project1', host='mongodb+srv://akash:akash@cluster0.zqitl.mongodb.net/<dbname>?retryWrites=true&w=majority')


class Task(Document):
    task = StringField(required=True)
    done = BooleanField(default=False)


def add_task(task):
    Task(task=task, done=False).save()



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
