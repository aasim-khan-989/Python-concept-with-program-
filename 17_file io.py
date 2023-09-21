'''     file handling in a python    '''
# In python, we use open function to open a file
# a = open("filehandling.txt", 'r')# note if not specify mode it will take read mode as default
# print(a.read())
# it is used to read the file in console
# it will read only five characters
# note if we used read()so it  will not read again untill the file is closed
# print(a.read())
# a.close()
# it will read 5 characters
# print(a.read(5))
# a.close()
# use of readline method
# a = open("filehandling.txt", 'r')
# print(a.readline())
# print(a.readline())
#use of readlines in python : it will show file as a list and every line as a list element
# a = open("filehandling.txt", 'r')
# print(a.readlines())
# a.close()


# x=open('filehandling.txt','r')
# y=x.read()
# print(type(y))



def game():
    return 5
score=game()

with(open('HighScore.txt','r')) as f:
    highscore = int(f.read())
if highscore==0 or highscore<=score:
    with(open('HighScore.txt', 'w')) as f:
        f.write(str(score))












































