# import sys
# #from finder_module import find_index as fi,test as t

# import finder_module as fm
# sys.path.append('/Users/Himanshu_1912/Lets_Code/CODE_A/C++_Py_JS_Algo_DS_ETC/PYthon/code_snippets/Python-Imports')


# anothernames=['']

# findindex = fm.find_index(names,'Dogg')


# print(findindex)

# # print(sys.path)

# import random
# import math
import os

# names = ['Meoww','Bokuu','Cat','Dogg','Rick','Thomas','Jackson','Jacobs','Wright','Tom']

# random_name= random.choice(names)
# print(random_name)

# sins= math.sin(65)
print("ok")

def cwdis():
    cwd = os.getcwd()
    print(cwd)

def ccwd(*dirnam):
    os.chdir(*dirnam)

def lsdir():
    lsdir=os.listdir()
    print('List- ',lsdir)
def mkdir(*dirnam):
    mkddir=os.mkdir(*dirnam)
    print('Dir_Maked- ',*dirnam)

def mkdirs(*dirnam):
    mkdirs=os.makedirs(*dirnam)

def rmdir(*dirnam):
    rmddir=os.rmdir(*dirnam)
    print('Dir_Removed- ',*dirnam)

cwdis()
lsdir()
ccwd('')
cwdis()
lsdir()

#mkdirs('ok/sub_ok')

# rmdir('Ok_It_Works/')

#lsdir()


