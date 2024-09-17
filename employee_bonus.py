import csv

def main():
    #open file
    employee_file = open('employee_data.csv', 'r')
    # create csv variable
    employee_csv = csv.reader(employee_file)
    # assign header for later reference
    header = next(employee_csv) 
    # start for loop to do each line
    for rec in employee_csv:
        # assign reference variables to change each loop
        name = rec[1]
        salary = float(rec[3])
        # bonus calculation
        bonus = float(rec[7]) * float(salary)
        # total pay calculation
        pay = bonus + salary
        # List of print statements; potential for automation?
        print(f'{header[1]+':'} {name}')
        print(f'{header[3]+':':<7} $ {salary:,.2f}\n{header[7]+':':<7} $ {bonus:,.2f}')
        print(f'{'Pay'+':':<7} $ {pay:,.2f}')
        input()

main()
