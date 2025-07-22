import csv

report = {}

def update_report(en,category,value):
    if en not in report:
        report[en] = {'Candidate':[],
                      'Pass':0,
                      'Fail':0,
                        'Best':-1,
                        'Worst':101}
    if type(value) is str and value in 'Pass,Fail':
        report[en][value] += 1
    elif category == "Candidate":
        if value not in report[en][category]:
            report[en][category].append(value)
    elif category == 'Score':
        hi = report[en]['Best']
        lo = report[en]['Worst']
        if value > hi:
            report[en]['Best'] = value
        elif value < lo:
            report[en]['Worst'] = value


with open('exam_results.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for dict in reader:
        ci = dict['Candidate ID']
        en = dict['Exam Name']
        sc = int(dict['Score'])
        gr = dict['Grade']
        update_report(en,'Candidate',ci)
        update_report(en, 'Score', sc)
        update_report(en, 'Grade', gr)

fieldnames = ['Exam Name','Number of Candidates','Number of Passed Exams','Best Score','Worst Score']
# print(report)
with open('examreport.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    for examtype in report.keys():
        writer.writerow([examtype,len(report[examtype]['Candidate']),report[examtype]['Pass'],report[examtype]['Fail'],report[examtype]['Best'],report[examtype]['Worst']])

# with open('examreportd.csv','w',newline='') as csvfile:
#     writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
#     writer.writeheaders()
#
#     for examtype in report.keys():
#         report[examtype]['Candidate'] = len(report[examtype]['Candidate'])
#         writer.writerow([examtype,len(report[examtype]['Candidate']),report[examtype]['Pass'],report[examtype]['Fail'],report[examtype]['Best'],report[examtype]['Worst']])
