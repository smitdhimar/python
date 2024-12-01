class myClass:
    def __init__(self):
        print("init called");
    def __str__(self):
        return "this is myclass's string method"

obj= myClass();
print(obj)