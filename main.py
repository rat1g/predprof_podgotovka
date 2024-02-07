

class Studentiki:
    id = 0
    full_name = ''
    id_project = 0
    clas = ''
    score = 0

students = []
f = open('students.csv')
skip = f.readline()
j = 0

for i in f:
    s = i.split(',')
    if int(s[3][:-1]) == 10:
        students.append(Studentiki())
        students[j].full_name = s[1]
        students[j].score = s[4]
        j += 1

for i in range(len(students)):
    j = 1
    t = students[i]
    while j > 0 and students[j-1].score > t.score:
        students[j] = students[j-1]
        j -= 1
    students[j] = t

print(f'''
10 класс:
1 место: {students[2].full_name[0]}.{students[2].full_name.split()[0]}
2 место: {students[4].full_name[0]}.{students[4].full_name.split()[0]}
3 место: {students[6].full_name[0]}.{students[6].full_name.split()[0]}
''')