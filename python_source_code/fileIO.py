# with open("sample.txt","r") as f:
    # data=f.read()

# new_data=data.replace("Java","Python")

# with open("sample.txt","w") as f:
#     data=f.write(new_data)


# with open("sample.txt","r") as f:
#     data=f.read()
#     if(data.find(word)!=-1):
#         print("found ")
#     else:
#         print("not found")

def check_line_count():
    word="T"
    data=True
    line_no=1
    with open("sample.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no +=1

    return -1
# check_line_count()

def check_even():
    count=0
    with open("demo.txt","r") as f:
        data=f.read()
        nums=data.split(",")
        for value in nums:
            if(int(value)%2==0):
                count +=1
    return count

print(check_even())


        


    