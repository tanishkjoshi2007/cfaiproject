name = input("Enter Name: ")
cgpa = float(input("Enter CGPA: "))

print("\nChoose Interest")
print("1. AI")
print("2. Web Development")
print("3. Cyber Security")
print("4. Data Science")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("\nRecommended Careers:")
    print("AI Engineer")
    print("Machine Learning Engineer")
    print("Data Scientist")

elif choice == 2:
    print("\nRecommended Careers:")
    print("Frontend Developer")
    print("Backend Developer")
    print("Full Stack Developer")

elif choice == 3:
    print("\nRecommended Careers:")
    print("Ethical Hacker")
    print("Security Analyst")
    print("Cyber Security Engineer")

elif choice == 4:
    print("\nRecommended Careers:")
    print("Data Analyst")
    print("Data Scientist")
    print("Business Analyst")

if cgpa >= 8:
    print("\nMatch Score: 90%")
elif cgpa >= 7:
    print("\nMatch Score: 80%")
else:
    print("\nMatch Score: 70%")