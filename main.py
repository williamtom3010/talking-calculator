import pyttsx3
pyttsx3.speak("Enter your name")
name = input("Enter your name\t")


print("Hi " + name)
pyttsx3.speak("Hi " + name)
b=["yes"]
while "yes" in b:    
    print("Do you want to run the talking calculator made by William Tom Jacob")
    pyttsx3.speak("Do you want to run the talking calculator made by William Tom Jacob")
    print("Type yes or no")
    pyttsx3.speak("Type yes or no in lowercase")
    b=input()
    if "yes" in b:
      i=1
      pyttsx3.speak("Enter the number of variables you want to calculate")
      print("Enter the number of variables you want to calculate")
      a=input()
      pyttsx3.speak("enter the operator")
      print("enter the operator")
      print(" press + for addition \n press - for subtraction \n press * for multiplication \n press / for division")
      z=input()
      if z=="+":
        pyttsx3.speak("Enter one number at a time and press enter after entering each number")
        print("Enter one number at a time and press enter after entering each number")
        sum1=0
        while i<=int(a):
             c=input()
             sum=int(c) 
             sum2=sum1+sum
             sum1=sum2
             i=i+1
        else:
             print("The sum is")
             pyttsx3.speak("The sum is")
             print(sum2)
             pyttsx3.speak(sum2)
      elif z=="-":
        pyttsx3.speak("Enter the numbers")
        print("Enter the numbers")
        while i<=int(a):
             c=input()
             sub=int(c)
             if i==1:
                sub1=sub
                i=i+1
             else:
                sub2=sub1-sub
                sub1=sub2
                i=i+1
        else:
             print("The subtration is")
             pyttsx3.speak("The subtraction is")
             print(sub2)
             pyttsx3.speak(sub2)
      elif z=="*":
        pyttsx3.speak("Enter the numbers")
        print("Enter the numbers")
        prod1=1
        while i<=int(a):
             c=input()
             prod=int(c)
             prod2=prod*prod1
             prod1=prod2
             i=i+1
        else:
             print("The product is")
             pyttsx3.speak("The product is")
             print(prod2)
             pyttsx3.speak(prod2)
      elif z=="/":
        pyttsx3.speak("Enter the numbers")
        print("Enter the numbers")
        div1=1
        while i<=int(a):
             c=input()
             div=int(c)
             div2=div/div1
             div1=div2
             i=i+1
        else:
             print("The quotient is")
             pyttsx3.speak("The quotient is")
             print(div2)
             pyttsx3.speak(div2)
      else:
        pyttsx3.speak("Please enter a valid arithmetic operator")
        print("Please enter a valid arithmetic operator")
else:
     print("Thank you for using the calculator made by William Tom Jacob")
     pyttsx3.speak("Thank you for using the calculator made by William Tom Jacob")
