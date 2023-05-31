import ggT

start = ord(" ")
ende = ord("_")
dif = ende - start + 1


def keyvalue(c):
    return ord(c) - start

def valuekey(k):
    return chr((k % dif) + start)


def phi(P, Q):
    return (P - 1) * (Q - 1)

def str2nums(st,split):
    out = []
    for i in range(0, len(st), split):
        strblock = st[i:i+split]
        out.append(str2num(strblock))
    return out


def nums2str(nums):
    out = ""
    for num in nums:
        out += num2str(num)
    return out
def str2num(st):
    out = 1
    for w in st:
        o = keyvalue(w)
        out *= 10**2
        out += o
    return out


def num2str(num):
    out = ""
    while num != 1:
        tmp = num // 10**2
        tmp *= 10**2
        z = num - tmp
        c = valuekey(z)
        out = c+out
        num //= 10 ** 2
    return out



e = 2
p, q = 101, 333
PHI = phi(p, q)
N = p * q
# wähle e < phi(p, q) wobei e Teiler fremd zu N
while True:
    if ggT.ggT(e, PHI) == 1:
        break
    e += 1
_, (__, d) = ggT.erweiterter_euklid(PHI, e)


print("e", e,"N",N,"phi", PHI, "d", d)

wort = "MY NAME IS BOB"
nums = str2nums(wort,2)
rec = nums2str(nums)

print(nums, rec, wort)

# 3*11067 %33200
chiffrats = [num**e % N for num in nums]
print(chiffrats, "[num**e % N for num in nums]")

entschl = [(chiffrat**d) % N for chiffrat in chiffrats]
print(entschl)
print(nums, entschl)

