"""
某销售公司发放的奖金根据利润提成。利润低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成。

定义函数func()，传入参数profit为利润，计算出奖金数额，最后通过参数profit为140000调用func()函数，并格式化输出："本月奖金为xx元"。
"""
def func(profit):
    bonus = 0
    thresholds = [100000,200000,400000,600000,1000000]
    profits = [100000,100000,200000,200000,400000]
    rates = [0.1,0.075,0.05,0.03,0.015,0.01]
    for i in range(5):
        if profit > thresholds[i]:
            bonus = bonus + profits[i]*rates[i]
        else:
            bonus = bonus + (profit-thresholds[i-1])*rates[i]
            break
    print(f"本月奖金为{bonus}元")
func(140000)