import csv

steps_file = open('steps.csv', 'r')
steps_csv = csv.reader(steps_file)

next(steps_csv)

steps_index = {}
days_counter = {}
avg_steps = {}

for i in range(1, 13, 1):
    steps_index[i] = 0
    days_counter[i] = 0
    avg_steps[i] = 0

# steps_index = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
# days_counter = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}
# avg_steps = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0}

for rec in steps_csv:
    steps_index[int(rec[0])] += int(rec[1])
    days_counter[int(rec[0])] += 1
    # steps_index[int(rec[0])] = steps_index[int(rec[0])] + int(rec[1])
    # days_counter[int(rec[0])] = days_counter[int(rec[0])] + 1

for month in avg_steps:
    avg_steps[month] = steps_index[month] / days_counter[month]


mth_num = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June', 
           7:'July', 8:'August', 9:'September', 10:'October', 11:'November', 12:'December'}

for month in mth_num:
    print(f'{mth_num[month]:<10} - {avg_steps[month]:>10,.2f}')




 


