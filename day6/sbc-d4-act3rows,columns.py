rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for row in range(rows):
    current_row = ""
    for col in range(columns):
        if row == 0 or row == rows - 1 or col == 0 or col == columns - 1:
            current_row += '* ' # for border
        else:
            current_row += '  ' # for inside border
    print(current_row)