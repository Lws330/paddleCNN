import random as rnd

strategy = ['stick', 'choose', 'switch']


def MC(strategy, times):
    wins = 0
    for trail in range(times):
        # 假定，车在0号门,我们不一定选择哪一个门
        envelops = [0, 1, 2]
        # 第一次随机选取一扇门
        first_choice = rnd.choice(envelops)
        # 根据第一次的选择情况的不同，第二次选择面临两种不同的备选组合

        # 如果第一次选择了0号门，那么在打开另外两个羊门中的一个后
        # 第二次将要在0号门和未打开的羊门（1 or 2）中作出选择
        if first_choice == 0:
            envelops = [0, rnd.choice([1, 2])]
        # 如果第一次没有选中0，那么此时被打开的必然是另一个羊门，那么
        # 在第二次选择时，将在0和自己现在所处的门（first_choice）作出选择
        else:
            envelops = [0, first_choice]

        # 采取不同的策略进行第二次选择

        # 保持原来位置不变
        if strategy == 'stick':
            second_choice = first_choice
        # 在除去一个羊门后的两个门中，随机选择一个
        elif strategy == 'choose':
            second_choice = rnd.choice(envelops)
        # 排除一扇羊门后，放弃原来的选择，直接选择另一扇门
        elif strategy == 'switch':
            envelops.remove(first_choice)
            second_choice = envelops[0]

        # 记得，奖品在0号门
        if second_choice == 0:
            wins += 1
    # 计算获奖的概率值
    p = wins / times
    print('第二次选择采用' + strategy + '方法，获奖的概率为：' + str(p) + '(模拟次数为' + str(times) + ')')


MC('stick', 10000)
MC('choose', 10000)
MC('switch', 10000)