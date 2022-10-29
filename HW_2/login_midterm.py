import re

def main():
  
    while True:
        mail = input("Enter your email: ").strip()
        if re_mail:=re.search(r"^\w+@(\w+\.)?\w+\.\w{3}$", mail):
            break
        else:
            print("Wrong Email")

    while True:
        password = input("Enter your password: ").strip()
        if re_pass:=re.search(r"^\w{4,8}", password):
            break
        else:
            print("Wrong Password")

    while True:
        try:
            mid = int(input("Enter midterm score(0-100): "))
            final = int(input("Enter final score(0-100): "))

            avg = (mid*4+final*6)/10
            if 0 <= avg <= 100:
                print("Your average score is", str(avg))
                if 90 <= avg <= 100: 
                    print("AA")
                elif 85 <= avg < 90:
                    print("BA")
                elif 80 <= avg < 85:
                    print("BB")
                elif 75 <= avg < 80:
                    print("CB")
                elif 70 <= avg < 75:
                    print("CC")
                elif 60 <= avg < 70:
                    print("DC")
                elif 50 <= avg < 60:
                    print("DD")
                else:
                    print("FF")
                break
            else:
                print("Enter correct scores")
                
        except:
            print("Try Again")

            


if __name__ == "__main__":
    main()