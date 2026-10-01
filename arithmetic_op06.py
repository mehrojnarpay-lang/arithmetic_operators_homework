# n  deb nomlangan o'zgaruvchi yarating va besh  xonali turli xil raqamni belgilang

# n sonining raqamlar yig'indisni toping va uni sum deb nomlangan o'zgaruvchiga belgilang.

# n sonining raqamlar ko'paymasini toping va uni k deb nomlangan o'zgaruvchiga belgilang.

# total deb nomlangan o'zgaruvchi yarating va k ning qiymatini sum qiymatiga butunli bo'ling. 

# total o'zgaruvchisining natijasini chiqaring.
n = 43876
sum = (n // 10000) + ((n // 1000) % 10) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10)
k = (n // 10000) * ((n // 1000) % 10) * ((n // 100) % 10) * ((n // 10) % 10) * (n % 10)
total = k // sum
print(total)