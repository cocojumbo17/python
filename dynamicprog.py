def levenstain(A, B):
    """find min changing to convert string A to string B"""
    F = [[i+j if i*j == 0 else 0 for i in range(len(A)+1)] for j in range(len(B)+1)]
    for i in range(1,len(B)+1):
        for j in range(1, len(A) + 1):
            if B[i-1] == A[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = 1+min(F[i - 1][j],F[i][j - 1],F[i - 1][j - 1])
    return F[len(B)][len(A)]

def main():
    #str1=input('First string:')
    #str2=input('Second string:')
    l = levenstain('vasia', 'vasya')
    print('l=', l)
if __name__=="__main__":main()