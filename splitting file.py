with open("resume",'r') as file:
    lines = file.readlines()

with open("resume_a.txt",'w') as file:
    for line in lines[:int(len(lines)/4)]:
        file.write(line)

with open("resume_B.txt",'w') as file:
    for line in lines[int(len(lines)/4):]:
        file.write(line)