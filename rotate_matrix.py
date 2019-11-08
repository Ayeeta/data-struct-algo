def rotate_90_degrees(matrix):
    n = len(matrix) - 1
    d = 0   # diagonal
    
    while d < (n + 1) // 2:     # loop through 1st half of diagonal
        
        for i in range(d, n - d):   # loop through row
            
            temp = matrix[d][i]
            matrix[d][i] = matrix[n - i][d]
            matrix[n - i][d] = matrix[n - d][n - i]
            matrix[n - d][n - i] = matrix[i][n - d]
            matrix[i][n - d] = temp
        
        d += 1

