marks = int (input ("Enter your marks: ") )

# if elif else you can add elif as many times as you need
# if statement should have a one tab space this is very imp

if marks >= 90 and marks <= 100: 
     grade = "A"

elif marks >= 75:
     grade = "B"
     
elif marks >= 60:
     grade = "C"
     
elif marks <=50 and marks >= 0:
     grade = "F"
     
else:
     print ("Invalid")     

     
print (grade)     