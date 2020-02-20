class dictObj(object):
    def __init__(self):
        self.x="red"
        self.y="yellow"
        self.z="green"
        def do_nothing(self):
            pass
test=dictObj()
print(test.__dict__)

#split a string into a list
str="welcome to the python class"
a_list=str.split(' ')
print(a_list)

#creating a string using a list of string
b_list="".join(str)
print(b_list)