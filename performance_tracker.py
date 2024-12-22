def avgmarks(students):
    avgs = {student : sum(marks)/len(marks) for student,marks in students.items()}
    topper = max(avgs,key=avgs.get)
    print(f"Average Marks: {avgs}")
    return (f"Top Performer : {topper}")
    # print(f"Top Performer : {topper}")

students = {"John": [85, 78, 92], "Alice": [88, 79, 95], "Bob": [70, 75, 80]}
print(avgmarks(students))