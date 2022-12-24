student=[[44,'karthik',75,79],[22,'p joshna',80,84],[58,'sunilreddy',78,80],[54,'naresh',88,90]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
