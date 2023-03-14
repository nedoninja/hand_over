def sor(sp):
    if len(sp) <= 1:
        return sp
    sp0, sp1 = [], []
    for i in sp:
        if i < sp[0]:
            sp0.append(i)
        elif i > sp[0]:
            sp1.append(i)
    return sor(sp0) + [sp[0]] + sor(sp1)


def sor1(sp, sps):
    if len(sp) <= 1:
        return (sp, sps)
    sp0, sp1, sp2 = [], [], []                     
    sp10, sp11, sp12 = [], [], []
    for i in range(len(sp)):
        if sp[i] < sp[0]:
            sp0.append(sp[i])
            sp10.append(sps[i])
        elif sp[i] == sp[0]:
            sp1.append(sp[i])
            sp11.append(sps[i])
        else:
            sp2.append(sp[i])
            sp12.append(sps[i])
    sp0, sp2 = sor1(sp0, sp10), sor1(sp2, sp12)
    return (sp0[0] + sp1 + sp2[0], sp0[1] + sp11 + sp2[1])


n = int(input())
sp = sor([int(i) for i in input().split()])
k = int(input())
cp = sor1([int(i) for i in input().split()], list(range(k)))
a = 0
ans = []
i = 0
while i < len(sp) and a < k:
    if sp[i] < cp[0][a]:
        i += 1
    else:
        ans.append(i)
        a += 1
for j in range(k - len(ans)):
    ans.append(i)
sp = {}
for j in range(len(cp[1])):
    sp[cp[1][j]] = ans[j]
for j in range(len(cp[1])):
    print(sp[j])