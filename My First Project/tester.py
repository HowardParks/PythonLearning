line=0
with open('My First Project/program.py') as f:
    for data_line in f:
        if (len(data_line) > 1):
            line += 1
            print("Line ",line,": ",data_line.rstrip())

