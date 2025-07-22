import csv

report = []
candlist = {}
fieldnames = ['Exam Name','Number of Candidates','Number of Passed Exams','Best Score','Worst Score']
with open('exam_results.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for dict in reader:
        en = dict['Exam Name']
        if en not in report:
            default = [en, 0, 0, -1, 101]
            report[en] = {k:v for k,v in zip(fieldnames,default)}
            candlist[en] = []
        ci = dict['Candidate ID']
        sc = int(dict['Score'])
        gr = dict['Grade']
        if ci not in candlist[en]:
            candlist[en].append(ci)
        report[en]["Number of Candidates"] = len(candlist[en])
        if gr == "Pass":
            report[en]['Number of Passed Exams'] += 1
        if gr == "Fail":
            report[en]['Number of Failed Exams'] += 1
        if sc > report[en]['Best Score']:
            report[en]['Best Score'] = sc
        if sc < report[en]['Worst Score']:
            report[en]['Worst Score'] = sc

with open('examreportdict.csv',newlines='') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(report)
