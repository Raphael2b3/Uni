def dez2bin(num):
    out = []
    while num > 0:
        out.append(num & 1)
        num >>= 1
    if not out:
        out.append(0)
    out.reverse()
    print(out)
    return out


def bin2dez(bits):
    out = 0
    for bit in bits:
        out <<= 1
        out += bit

    return out


def schriftlich_dez2n(num, n=2):
    out = []
    while num > 0:
        d = num % n
        print(num, "%", n, "=", d)
        num //= n
        out.insert(0, d)
    print(out, bin2dez(out))
    return out


def schriftlich_n2dez(nums, n=2):
    out = 0
    i = len(nums) - 1
    for num in nums:
        out += num * n ** i
        print("+", num, "*", n, "^", i, end=" ")
        print("=    /*",out,"*/")
        i -= 1
    print("\n =", out)
    return out


def schriftlich_n2dez_hornerschema(nums, n=2):
    out = nums[0]
    print("(...(", end=f"{nums[0]}*{n})*")
    for num in nums[1:]:
        print(n, "+", num, end=")* ")
        out = out * n + num
    print("1\n =", out)
    return out


def bin2hex(nums):
    r = schriftlich_dez2n(bin2dez(nums), 16)
    print("bin2hex ", nums, "to", r)

    return r


def hex2bin(nums):
    r = schriftlich_dez2n(schriftlich_n2dez(nums, 16), 2)
    print("hex2bin ", nums, "to", r)
    return r


if __name__ == '__main__':
    basis = 2
    B = schriftlich_dez2n(41892, basis)
    schriftlich_n2dez_hornerschema(B, basis)
