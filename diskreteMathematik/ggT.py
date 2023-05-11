def ggT(a, b):
    gr = max((a, b))
    kl = min((a, b))

    q = gr // kl
    r = gr % kl
    print(f"{gr} = {q} * {kl} + {r}")
    return kl if r == 0 else ggT(kl, r)


def s_t(a, b, ggt):

    pass


def multiplikativ_inverse(a,b):
    pass


if __name__ == '__main__':
    print(ggT(27, 85))

