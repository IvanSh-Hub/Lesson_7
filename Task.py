

def calculation(x , y):
    return x*y

def print_operation_table(operation, num_rows, num_cols):
    for i in range(1, num_rows+1):
        for j in range(1, num_cols+1):
            print(operation(i, j), end = " ")
        print("\n")


print_operation_table(lambda x,y: x*y, 6,6)