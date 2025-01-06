class student:
    #name = ''
    def __init__(self,name,age,literature,math,english):
        self.name = name
        self.age = age
        self.literature = literature
        self.math = math
        self.english = english

    def get_name(self):
        return(self.name)
    def get_age(self):
        return(int(self.age))
    def get_course(self):
        return(max(self.literature,self.math,self.english))
    def get_average(self):
        return((self.literature+self.math+self.english)/3)

p = student('Mike',18,90,80,100)
print(p.get_name())
print(p.get_age())
print(p.get_course())
print(p.get_average())
    