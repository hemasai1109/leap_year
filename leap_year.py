year=int(input('Enter the Year You want to check'))

if year%4==0 :
    if year%100==0:
        if year%400==0:
            print("Year is Leap Year")
        else:
            print("Year Is Not a Leap Year")
    else:
        print("Year Is a Leap Year")
else:
    print("Year Is Not a Leap Year")