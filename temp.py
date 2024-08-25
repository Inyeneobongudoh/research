def fc(n):
    prd = 1
    for i in range(n,1,-1):
        prd*=i
    return prd

print(fc(8))

def dic(n):
    my_dict = {}
    for i in range(1,n+1):
        my_dict[i] = i*i
    return my_dict

print(dic(6))

def toupper(senctence):
    return senctence.upper()

print(toupper('Hello world Practice makes perfect'))


def sort(senctence):
    sent_list = senctence.split()
    return " ".join(sorted(list(set(sent_list))))
print(sort('hello world and practice makes perfect and hello world again'))

'''Question: Write a program to compute the frequency of the words from the input. 
The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
 New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. Then, 
 the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1'''

# def count_words(sentence):
#     sent_list = sentence.split()
#     dic = {}
#     for i in sent_list:
#         count = 0
#         for j in range(len(sent_list)):
#             count+=1
#         dic[i] = count
#     return sorted(dic)

def count_words(sentence):
    words = sentence.split()
    word_count = dict()
    for i in words:
        print(word_count)
        if i in word_count.keys():
            word_count[i] +=1
        else:
            word_count[i] =1

    return 

def arr(data:dict):
    keys = data.keys()



print(count_words("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3"))


from datetime import date
import datetime
class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.dob = date_of_birth

    def get_age(self):
        dob_list = self.dob.split("-")
        yob = int(dob_list[2])
        present_year = date.today().year
        return f"Age: {present_year - yob}"
    

name = input("Enter Name: ")
country = input(("Enter Country: "))
date_of_birth = input("Enter Date of Birth(format: DD-MM-YYYY)): ")

user1 = Person(name = name, country=country, date_of_birth=date_of_birth)
print(user1.get_age())