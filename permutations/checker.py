def read_matrix(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Filter out lines that start with ";;;"
    matrix = [line.strip() for line in lines if not line.startswith(";;;")]

    # Convert each line into a list of integers
    matrix = [list(map(int, line.split()[:-1])) for line in matrix]

    return matrix


def is_permutation(matrix1, matrix2):

    if len(matrix1) != len(matrix2):
        return False

    # Check if each row in matrix1 is present in matrix2
    for row in matrix1:
        if row not in matrix2:
            return False
    return True


def main():
    # Paths to the files
    file1 = '74L85.020.mhs'
    file2 = '74L85.020.01.mhs'

    # Read the matrices
    matrix1 = read_matrix(file1)
    matrix2 = read_matrix(file2)

    # Check if matrix2 is a permutation of matrix1
    if is_permutation(matrix1, matrix2):
        print("The second matrix is a permutation of the first matrix. The two instances have the same solutions")
    else:
        print("The second matrix is NOT a permutation of the first matrix. The two instances do not have the same solutions")


if __name__ == "__main__":
    main()
