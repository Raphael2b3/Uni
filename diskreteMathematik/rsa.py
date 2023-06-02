import ggT

def phi(P, Q):
    return (P - 1) * (Q - 1)


p, q = 59, 53
PHI = phi(p, q)
N = p * q
e = PHI // 2 + 10
# wähle e < phi(p, q) wobei e Teiler fremd zu N
while True:
    if ggT.ggT(e, PHI) == 1:
        break
    e += 1

_, (__, d) = ggT.erweiterter_euklid(PHI, e)

d = d % PHI
print("p", p, "    q", q, "  N", N, "   phi", PHI, "    e", e, "   d", d)

wort = "MYNAMEISBOB"
nums = str2nums(wort, 1)
rec = nums2str(nums)

print(nums, rec, wort)

# 3*11067 %33200
chiffrats = [num ** e % N for num in nums]
print(chiffrats, "[num**e % N for num in nums]")

entschl = [(chiffrat ** d) % N for chiffrat in chiffrats]
print(nums, entschl)
