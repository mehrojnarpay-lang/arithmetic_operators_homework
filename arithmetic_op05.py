# n  deb nomlangan o'zgaruvchi yarating va unga to'rt xonali raqamni belgilang

# n sonining teskarisini toping va uni total deb nomlangan o'zgaruvchiga belgilang.

# sub deb nomlanga o'zgaruvchi yarating va dastlabki n qiymatdan keyingi total qiymatni ayirmasini ta'minlang.

# sub o'zgaruvchisini chiqaring
n = 8643
total = (n % 10) * 1000 + ((n // 10) % 10) * 100 + ((n // 100) % 10) * 10 + (n // 1000)
sub = n - total
print(sub)