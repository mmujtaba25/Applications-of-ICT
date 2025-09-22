ob_marks: float = float(input("Obtained Marks: "))
total_marks: float = float(input("Total Marks: "))

percentage: float = ob_marks / total_marks * 100

while True:
    try:
        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        elif percentage < 50:
            grade = "You Failed :("
        else:
            raise

        print(f"Your grade is: {grade}")
        break
    except:
        print("Invalid Input")
        continue
