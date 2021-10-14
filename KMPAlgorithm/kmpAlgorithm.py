def computeLPSArray(pattern):
  pattert_len = len(pattern)
  lps = [0] * pattert_len
  length = 0

  i = 1
  while(i < pattert_len):
    if (pattern[i] == pattern[length]):
      length += 1
      lps[i] = length
      i += 1
    else:
      if (length != 0):
        length = lps[length - 1]
      else:
        lps[i] = 0
        i += 1

  return lps

def KMPSearch(P, T):
  M, N = len(P), len(T)

  lps = computeLPSArray(P)

  i, j = 0, 0
  while i < N:
    if (P[j] == T[i]):
      i += 1
      j += 1
    
    if (j == M):
      print('Encontrou o padrão no index: ', i - j)
      j = lps[j - 1]
    elif (i < N and P[j] != T[i]):
      if (j != 0):
        j = lps[j - 1]
      else:
        i += 1
  
P = input()
T = input()

KMPSearch(P, T)