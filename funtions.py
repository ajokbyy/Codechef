def total_exp(exp):
    total = 0
    for i in exp:
        total = total + i
    return total

abhi_exp_list = [2300, 2400, 2000, 2400]
mi_exp_list = [300, 400, 2000, 4000]


print(total_exp(abhi_exp_list))
print(total_exp(mi_exp_list))
