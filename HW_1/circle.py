PI = 3.1415

def circle(r):
    return PI*r*r

if __name__ == "__main__":
    while True:
        try:
            r = float(input("Enter radius value to calculate area of circle: "))
            print(circle(r))
            break
        except:
            print("Enter float value")
