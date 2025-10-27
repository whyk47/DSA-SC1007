# Q1: alpha = 0.5: h keys, 0.5h nodes, total h + 2*0.5h = 2h words
# alpha = 1: h keys, h nodes, total = h + 2h = 3h words
# alpha = 2: h keys, 2h nodes, total = h + 2*2h = 5h words
# 2h words -> 0.5h/2h = 0.25 
# 3h words -> h/3h = 0.333 
# 5h words -> 2h/5h = 0.4

# Q2: Best case: All n/2 keys hashed and distributed evenly into the n slots. 
# Avg complexity:(n/2*0 + n/2*1)/n = 0.5 = theta(1)
# worst case: all n/2 keys hashed to consecutive slots
# Avg complexity: (n/2*0 + 1 + 2 + ... + n/2)/n = 0.5n/2*(1+n/2)/n = n/8+0.25 = theta(n)

# Q3: for a string S = c0c1...c(n-1) 
# k = a0*(2^p)^0 + a1*(2^p)^1 + ... + a(n-1)*(2^p)^(n-1)
# 2^p mod m = 2^p mod (2^p - 1) = 1, (2^p)^k mod m = 1^k mod m = 1
# h(k) = a0 + a1 + ... + a(n-1)
# swapping ai and aj, i != j will not change the hash value