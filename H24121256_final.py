def parse_matrix(input_str):
    matrix = {}
    rows = input_str.split('|')
    n = len(rows)  # The number of rows (or columns, since it's a square matrix)
    for i in range(n):
        elements = rows[i].split(',')
        for j in range(len(elements)):
            matrix[(i, j)] = int(elements[j])
    return matrix, n

def matrix_multiply(U, V, n):
    M = {}
    for i in range(n):
        for j in range(n):
            M[(i, j)] = sum(U.get((i, k), 0) * V.get((k, j), 0) for k in range(n))
    return M

def print_matrix(matrix, n):
    for i in range(n):
        row = [matrix.get((i, j), 0) for j in range(n)]
        print(row)

def main():
    u_input = input("Enter matrix U: ")
    v_input = input("Enter matrix V: ")
    
    U, n = parse_matrix(u_input)
    V, _ = parse_matrix(v_input)
    
    M = matrix_multiply(U, V, n)
    
    print("M = U x V")
    print_matrix(M, n)

# 直接呼叫 main 函數
main()
