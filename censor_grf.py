from matplotlib import pyplot as plt

MODE = "EOS"


if MODE == "EOS":

    node_num = 165040
    x = [0, 163930 / node_num, 164930 / node_num, 165030 / node_num, 165040 / node_num]
    y = [0, 0.1386, 0.1101, 0.2515, 0.4998]
    new_y = []
    sum_y = 0
    for i in y:
        sum_y += i
        new_y.append(sum_y)
    # past = 0
    # area = 0
    # iter = 0
    # for each in y:
    #     current = each + past
    #     area += (past + current) * (x[iter + 1] - x[iter]) / 2

    #     past = current
    #     iter += 1

    # print(1-2*(1/2-area))

    plt.figure()

    plt.plot(x, new_y, '-r')
    plt.plot([0, 1], [0, 1], 'b')
    plt.legend(['Lorenz curve', 'Line of equality'])
    plt.title("EOS")
    plt.show()

elif MODE == "BTC":
    total_node_num = 1340000


    y = [0.2, 0.5, 1.0, 1.0, 1.0, 1.5, 1.5, 3.4, 4.9, 6.8, 8.3, 9.0, 10.0, 10.3, 10.5, 13.7, 15.4]
    temp = 0
    for i in y:
        temp += i
    y.insert(0, 100 - temp)

    res_node_num = total_node_num - len(y)
    x = [res_node_num / total_node_num]
    for _ in range(len(y)-1):
        x.append(1 / total_node_num)

    past = 0
    area = 0
    iter = 0
    for each in y:
        each = each / 100
        current = each + past
        area += (past + current) * x[iter] / 2
        iter += 1

    result = 1 - 2 * (1/2 - area)

    x.insert(0, 0)
    y.insert(0, 0)

    new_y = []
    sum = 0
    for i in y:
        sum += i
        new_y.append(sum/100)

    new_x = []
    sum2 = 0
    for i in x:
        sum2 += i
        new_x.append(sum2)


    plt.plot(new_x, new_y, '-r')
    plt.plot([0, 1], [0, 1], 'b')
    plt.legend(['Lorenz curve', 'Line of equality'])
    plt.title("BTC")
    plt.show()


elif MODE == "ETH":
    total_node_num = 670000

    y = [1, 1, 1, 1, 2, 3, 3, 4, 4, 4, 8, 10, 10, 13, 13, 21]
    temp = 0
    for i in y:
        temp += i
    y.insert(0, 100 - temp)

    res_node_num = total_node_num - len(y)
    x = [res_node_num / total_node_num]
    for _ in range(len(y)-1):
        x.append(1 / total_node_num)

    past = 0
    area = 0
    iter = 0
    for each in y:
        each = each / 100
        current = each + past
        area += (past + current) * x[iter] / 2
        iter += 1

    result = 1 - 2 * (1/2 - area)

    x.insert(0, 0)
    y.insert(0, 0)

    new_y = []
    sum = 0
    for i in y:
        sum += i
        new_y.append(sum/100)

    new_x = []
    sum2 = 0
    for i in x:
        sum2 += i
        new_x.append(sum2)


    plt.plot(new_x, new_y, '-r')
    plt.plot([0, 1], [0, 1], 'b')
    plt.legend(['Lorenz curve', 'Line of equality'])
    plt.title("ETH")
    plt.show()