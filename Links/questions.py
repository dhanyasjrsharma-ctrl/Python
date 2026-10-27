# marks={'shivam':90,'abhi':80,'kunal':70,'dhanya':95,'siddhi':78}
# largest=0
# slargest=0
# l=[]
# for i in marks.values():
#     if i>largest:
#         slargest=largest
#         largest=i
# for key,values in marks.items():
#     if values==largest:
#         l.append(key)
#     elif values==slargest:
#         l.append(key)
# print(l)


# marks={'shivam':90,'abhi':80,'kunal':70,'dhanya':95,'siddhi':78}


# largest = 0
# second = 0
# l = []

# for i in marks.values():
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# for key, value in marks.items():
#     if value == largest or value == second:
#         l.append(key)

# print(l)

# present = 0
# absent = 0
# for i in range (1,8):
#     status = input("enter P or A: ")
#     if status == "P":
#         present += 1
#     elif status == "A":
#         absent += 1
# print(f"total present days,{present}")
# print(f"total absent days,{absent}")

# p,a=0,0
# print("enter your attendence:->")
# for i in range(1,8):
#     n=input(f"day {i}.:-> ")
#     if n in "pP":
#         p+=1
#     elif n in "aA":
#         a+=1
#     else:   
#         print("enter valid attendence")
#         for i in range(i,i+1):
#             n=input(f"day {i}.:-> ")
            
# print(f"you were present for {p} days and absent for {a} days")

