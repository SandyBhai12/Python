# a=int(input("enter the number"))
# b=int(input("enter the second number"))
# sum=a+b
# print(sum)

# side=float(input("enter the square of the size"))
# area=side*side
# print(area)

# value1=float(input("enter the value1"))
# value2=float(input("enter the value2"))
# avg=(value1+value2)/2
# print(avg)

# a=5
# b=10
# if(a>=b):
#     print(True)
# else:
#     print(False)

# str="sandy$bhau"
# print(str.find("$"))


# num1=int(input("enter the number to check "))
# num2=int(input("enter the number to check "))
# num3=int(input("enter the number to check "))
# num4=int(input("enter the number to check"))

# if(num1>=num2 and num1>=num3 and num1>=num4):
#     print(num1,"is greatest")
# elif(num2>=num3 and num2>=num4):
#     print(num2," is greatest")
# elif(num3>=num4):
#     print(num3," is greatest")
# else:
#     print(num4,"is the greatest")


# num=int(input("enter the number"))

# if(num%7==0):
#     print(num," : is divisble by 7")
# else:
#     print(num," : is not  divisble by 7")


# name1=input("enter the name")
# name2=input("enter the name")
# name3=input("enter the name")

# # list=[name1,name2,name3]
# list=[]
# list.append(name1)
# list.append(name2)
# list.append(name3)
# print(list)

# list=["m","a","a","m"]

# a=list.copy()
# a.reverse()

# if(list==a):
#     print(list," list is palindrome")
# else:

#      print(list," list is not a palindrome")

# grade=("C","D","A","A","B","B","A")
# Listgrade=["C","D","A","A","B","B","A"]
# print(grade.count("A"))
# Listgrade.sort()
# print(Listgrade)


# dist={
#     "name":"Sandeep",
#     "subject":{
#         "math":98,
#         "english":78,
#         "kannada":38,
#     }
# }

# print(dist.keys())
# print(dist.values()) #error 
# print(dist.items())
# print(dist.get("name")) # none


# marks={}
# x= int(input("enter the marks for Physics"))
# marks.update({"Physics":x})
# x= int(input("enter the marks for Chemistry"))
# marks.update({"Chemistry":x})
# x= int(input("enter the marks for Math"))
# marks.update({"Math":x})

# print(marks)

# i=1
# while(i<=100):
#     print(i)
#     i +=1

# i=100
# while(i>=1):
#     print(i)
#     i -=1

# n=5
# i=1
# while(i<=10):
#     print(n," X ",i,"= ",n*i)
#     i+=1

# list=[1,4,9,16,25,36,49,64,81,100]
# for ele in list:
    # print(ele)
# i=0
# while i<len(list):
#     print(list[i])
#     i+=1


# tup=(1,4,9,16,25,36,49,64,81,100)
# i=0
# for ele in tup:
    
#     if(ele==36):
#         print(ele," found it",i)
#     i+=1
# i=0
# while i<len(tup):
#     x=64
#     if(tup[i]==x):
#         print(i)
#     i+=1


# i=5
# sum=0
# while(i>0):
#     sum=sum+i
#     i-=1

# print(sum)


# n=5

# for i in range(1,n):
#     n=n*i
    

# print(n)


# def avgNumver(a,b,c):
#     avg=int((a+b+c)/3)
#     return avg

# print(avgNumver(10,20,30))


# heros=["ironman","captain america","thor","hulk","natsha","loki","houkai","antman"]

# def print_list(list):
#     for item in list:
#         print(item ,end=" ")

# print(print_list(heros))
# print()

def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact

# print(factorial(5))

def convertUsdToInr(value):
    return value ," $ is = ",value*83," rupeess"

# print(convertUsdToInr(3))

def oddOrEven(num):
    if(num%2==0):
        return "even"
    else:
        return "odd"
    
# print(oddOrEven(6))


def fact(n):
    if(n==0):
        return 1
    else:
        return fact(n-1)*n
 
# print(fact(5))   

def sum(n):
    if(n==0):
        return 0
    else:
        return sum(n-1)+n

# print(sum(5))

list=["sandeep","bhauu","kabuuu","sabuuu","labuu"]

def reve(list,index=0): #default index=0 its starts from 0 
    if(index ==len(list)):
        return len(list)
    print(list[index])
    reve(list,index+1)

reve(list)
