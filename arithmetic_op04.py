# n deb nomlangan o'zgaruvchi yarating va unga uch xonali raqamni belgilang.

# n ning birinchi raqamini toping va x1 ga belgilang.

# n ning ikkinchi raqamini toping va x2 ga belgilang.

# n ning uchinchi raqamini toping va x3 ga belgilang.

# total deb nomlangan o'zgaruvchi yarating va unga (x1 + x2 * x3) ushbu ifodani ta'minlan.

# total qiymatini chop eting.
n = 999
x1 = n // 100
x2 = (n // 10) % 10
x3 = n % 10
total = x1 + x2 * x3
print(total)