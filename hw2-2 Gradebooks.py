subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = []
for i in range(len(subjects)):
    tmp = []
    tmp.append(subjects[i])
    tmp.append(grades[i])
    gradebook.append(tmp)
    
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

gradebook[5][1] = 98
gradebook[2].remove(85)
gradebook[2].append('Pass')

last_semester_gradebook =[["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
