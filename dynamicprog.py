def levenstain(A, B):
    """find min numbers of changing to convert string A to string B"""
    F = [[i + j if i * j == 0 else 0 for i in range(len(A) + 1)] for j in range(len(B) + 1)]
    for i in range(1, len(B) + 1):
        for j in range(1, len(A) + 1):
            if B[i - 1] == A[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(B)][len(A)]


def pifunction(S):
    """find prefix-suffix of string"""
    Pi = [0] * len(S)
    for i in range(1, len(S)):
        k = Pi[i - 1]
        while k > 0 and S[i] != S[k]:
            k = Pi[k - 1]
        if S[i] == S[k]:
            k += 1
        Pi[i] = k
    return Pi

def substr(S, sub):
    full_str = sub + '#' + S
    pi = pifunction(full_str)
    sublen = len(sub)
    res=[]
    for i in range(len(pi)):
        if (pi[i] == sublen):
            res.append(i-2*sublen)
    return res


def main():
    # str1=input('First string:')
    # str2=input('Second string:')
    l = levenstain('vasia', 'vasya')
    print('l=', l)
    S = 'Hello world. How are you? I hope you are fine.'

    pif = pifunction('Hello world. How are you? I hope you are fine.')
    print(pif)
    indexes = substr(S, 'o')
    print(indexes)

if __name__ == "__main__": main()
