def count_squares(A, B, C):
    if A%C != 0:
        return (A//C) * (B//C) + (A%C) * B//C
    else:
        return A//C * B//C
    
A = 106
B = 54
C = 16
print(count_squares(A, B, C)) 