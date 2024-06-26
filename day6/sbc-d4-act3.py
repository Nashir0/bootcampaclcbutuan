def print_pattern(rows):
    # Upper 
    for i in range(rows, 0, -1):
        print('*' * i)
        #print(i)
        
    print("" + (" ") * (rows-2) + "") # middle #add concat

    # Lower 
    for i in range(2, rows + 1):
         print('*'*i)
try:
    num_rows = int(input("Enter number of rows: "))
    print_pattern(num_rows)
except ValueError:
    print("Please enter a valid integer.")