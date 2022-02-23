line=0
with open('program.py') as f:
    for data_line in f:
        if (data_line != ""):
            line += 1
            print("Line ",line,": ",data_line.strip())

