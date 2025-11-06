def lcs(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    lcs_length = L[m][n]
    index = lcs_length
    lcs_str = [""] * (index + 1)
    lcs_str[index] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_str[index - 1] = X[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return lcs_length, "".join(lcs_str)
X = "AGGTAB"
Y = "GXTXAYB"
length, sequence = lcs(X, Y)
print("String 1:", X)
print("String 2:", Y)
print("Length of LCS:", length)
print("LCS sequence:", sequence)
