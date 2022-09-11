print("--------------------------Program 1 ----------------------------------")
print("1. Implement palindrome using iterator(for loop) and generator mechanism.")

"""
Approach:- 
1. input from user
2. reverse number using generator 
    a. first create a function reverse no and pass the number for reverse
    b. use while loop till number would be 0
    c. yield the rem
3. create a function for collecting no from separate digit
4. check user input and reversed no same or not 
    a. if same then its palindrome
    b. else not a paindrome

"""

# pass the number from user for checking the number is palindrome or not


inp = int(input("Enter the number : "))


def sep_dig(n):
    while n > 0:
        res = n % 10
        n = n // 10
        yield res


def rev_num(x):
    rev_dig = 0
    for i in sep_dig(x):
        rev_dig = (rev_dig * 10) + i
    return rev_dig


if inp == rev_num(inp):
    print(inp, "is palindrome")
else:
    print(inp, "is not a palindrome")

# program 2
print("---------------program 2--------------")
a=int(input("enter the a value:"))
b=int(input("enter the  b value:"))
X=str(a)
Y=str(b)
x=list(X)
y=list(Y)
res = []
sum=0
for i in range(0, len(x)):
    res.append(int(x[i]) + int(y[i]))
print("Addition of", x ," and", y , "is " + str(res))
for z in res:
       sum+=z
print("sum of given two values:",sum)
"""#Expalnation:converted the given integer into string and then to list, created empty list to append the result. with the for loop iterate the element as i and appended the value of x[i] and y[i] in the empty list
to get the sum  of the list again used for loop to add  iterating element with sum variable."""

#program 3
print("------------------program 3-------------------")
s="ab@cd!ef"
li=list(s)
#print(li)
i=0
j=len(li)-1
while i < j:
    if not li[i].isalpha():
        i += 1
    elif not li[j].isalpha():
        j -= 1
    else:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1

res = ''.join(li)
print(res)

"""Explanation: used isalpha() method tho check the given input is whether string r not .used "=" operator to swap the alphabets and using join() got the result"""

#program 4
print("-------------program 4---------------")
li = ["a", "b", "c", "d", "n", "a", "b", "m", "n", "m"]
n = {}
for a in li:
    if a in li:
        n[a] = n.get(a, 0)+1
        pass
    else:
        n[a]=n.count(a)
print(n)

"""Explanation:created empty dictionary to store the result in dict format using get() method if the items is reapeated more than once i added the count."""

#program 5
print("---------------program 5--------------")

t1 = (1, 2, 3, "a", "c")
t2 = ("b", "d", 9, 8, 7)


def sort_t1(a):
    strs = list(filter(lambda x: type(x) == str, a))
    ints = list(filter(lambda x: type(x) == int, a))

    out = sorted(ints) + sorted(strs)
    return out


def sort_typ(a):
    strs = list(filter(lambda x: type(x) == str, a))
    ints = list(filter(lambda x: type(x) == int, a))

    out = sorted(ints, reverse=True) + sorted(strs)
    return out


list_t1 = sort_t1(t1)
list_t2 = sort_typ(t2)

for t_1, t_2 in zip(list_t1, list_t2):
    print(t_1 + t_2)

#program 6
print("-------------program 6-------------")
import re
def rem_ip(ip_add):
  str = re.sub('(?!(\.0\.))(\.[0]{1,2})', '.', ip_add)
  return str
ip = "216.08.094.196"
print(rem_ip(ip))



#program 7
print("----------------program 7------------------")
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

output = []
def rem_nes_li(l):
    for i in l:
        if type(i) == list:
            rem_nes_li(i)
        else:
            output.append(i)

print('The original list: ', l)
rem_nes_li(l)
print('The list after removing: ', output)

#program 8
print("------------------------program 8-------------------")
import re

with open("D:\python\ 10 Functions.docx", "r") as file:
    file_content = file.read()
lines = len(file.readlines())
# special_char=re.compile('[@_!$%^&*()<>?/\|}{~:]#')
print("the no. of lines in file is ", len(file_content.split("\n")))
words_count = 0
chars_count = 0
vowels = 0
consonant = 0
for i in file_content.split("\n"):
    for j in i.split(" "):
        if not j.isalpha() and not j.isalnum():
            continue
        else:
            words_count += 1

    for j in i:
        if not j.isalpha() and not j.isalnum():
            continue
        else:
            chars_count += 1

    for j in i:
        if j.lower() in "aeiou":
            vowels += 1
        else:
            consonant += 1

print("the total words in file is ", words_count)
print("the total words in file is ", chars_count)
print("the total vowels in file is ", vowels)
print("the total consonant in file is ", consonant)
print('Total Number of lines:', lines)