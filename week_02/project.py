import time

class TODO:
    # todos = [
    #     {
    #     'id': '', ids in floating point make sure dont use ./decimal so typecast into in int
    #     'desc':'',
    #     'is_completed':False
    # },
    # {},{},{}]
    ## format needs as
    todo =[

    ]
    
    def add_todo(self, desc):
        
    ##1. Take the description from the user
    ##2. We have to create a dictionary in which we will add the todo desc.
    ##3. We have to append that dictionary inside tools
        # self.desc=input()
        # self.desc=desc
        
        dict_1={}
        dict_1['id']=int(time.time())
        dict_1['desc']=desc
        dict_1['is_completed']=False
        self.todo.append(dict_1)
        return print(self.todo)

    
    def remove_todo(self, id):
        for i in self.todo:
            if i['id'] == id:
                self.todo.remove(i)
                return 1
        else:
            return -1
          
    
    def display_todos(self):
        return print(self.todo)
    
    def update_todo(self, id, new_desc):
        for i in self.todo:
            if i['id']== id:
                i['desc']=new_desc
    
    def toggle_mark_as_completed(self, id):
        for i in self.todo:
            if i['id'] == id:
                i['is_completed'] = True
    
    def completed_todos(self):
        for i in self.todo:
            if i['is_completed'] == True:
                print(i)
    
    def incompleted_todos(self):
         for i in self.todo:
            if i['is_completed'] == False:
                print(i)
    

# obj1=TODO()
# obj1.add_todo('1234')
# (obj1.display_todos())
   

