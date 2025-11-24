import random

print("\n🤖 Hello! I am your Smart College Timetable Chatbot.")
print("I will help you create a personalized timetable.\n")
print("But first I really want to know your name .\n")

name = input("What is your name: ")
print("Hello", name + "! Let's start creating your timetable.\n")


print('🤖 : Please the number of working days in your college.')
days = int(input("Enter number of working days in the week: "))


day_names_all = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_names = day_names_all[:days]


print('🤖 : Please the number of working days in your college.')
periods = int(input("Enter number of periods per day: "))


print('🤖 : Please enter the number of subjects you have in this semester')
subjects = []
num_sub = int(input("Enter number of subjects: "))


print("\n 🤖 : Please enter the names of your subjects:")
print("\nEnter your subjects:")
for i in range(num_sub):
    s = input("Subject " + str(i+1) + ": ")
    subjects.append(s)


preferred_subject = {}   


print("🤖 : Here comes the organizing part")
print("\n📌 Choose which subject you want to study on each day:")
for d in day_names:
    print("\nDay:", d)
    print("Available subjects:", subjects)
    sub = input("Which subject do you want to study on " + d + "? ")

    while sub not in subjects:
        sub = input("Invalid! Choose from the given subjects: ")
    
    preferred_subject[d] = sub



print('🤖 : Revision is important to test yourself' , name )
test_day = input("\n📘 On which day do you want to test yourself? (" + ", ".join(day_names) + ") : ")

while test_day not in day_names:
    test_day = input("Invalid! Enter a correct day: ")

print("\nGreat! Creating your timetable...\n")



print("\n================= FINAL TIMETABLE =================\n")


print("{:<12}".format("Day"), end="")
for p in range(1, periods+1):
    print("{:<15}".format("P" + str(p)), end="")
print()


for d in day_names:
    print("{:<12}".format(d), end="")


    available = subjects.copy()

    
    chosen = preferred_subject[d]

    if chosen in available:
        available.remove(chosen)

    
    random.shuffle(available)

    
    day_list = [chosen]  

    
    for i in range(periods - 1):
        if i < len(available):
            day_list.append(available[i])
        else:
            day_list.append("-")

    
    if d == test_day:
        day_list[-1] = "TEST"

    
    for s in day_list:
        print("{:<15}".format(s), end="")
    print()

print("\n 🤖 : Congratulaions !!🎉 Your timetable has been successfully generated!")
print('🤖 : Hope this will help you to study better\n')
print('🤖 : Have a great day\n')