import csv

def main():
    # open and read original file
    cust_file = open('customers.csv', 'r')
    # define csv variable
    cust_csv = csv.reader(cust_file)
    # define header

    def writing():
        # create new file
        cust_country = open('customer_country.csv', 'w')
        # create header for referencing
        header = next(cust_csv)
        # print headers
        cust_country.write(f'Full Name, {header[4]} \n')
        # for loop to print, using write instead of print to write in file
        n = 0
        for rec in cust_csv:
            # n counter to count number of customers
            n += 1
            # combines first and last name, comma country
            cust_country.write(f'{rec[1]} {rec[2]}, {rec[4]} \n')
        # After for loop, writes total number of customers
        cust_country.write(f'There is a total of {n} customers')

        cust_country.close()
    writing()

main()






    