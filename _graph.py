import matplotlib.pyplot as plt


# # 第一个表示x轴,第二个列表表示y轴
# plt.plot([1, 0, 9], [4, 5, 6])
# plt.show()
#
# # plt.plot(x,y)
# # 对折线进行修饰
# # color设置为红色，alpha设置为透明度，linestyle表示线的样式，linewidth表示线的宽度
# # color还可以设置为16进制的色值，可在网上查看各种颜色对应的色值
# plt.plot(x, y, color='red', alpha=0.5, linestyle='--', linewidth=1)
# plt.show()
# '''线的样式
# -	实线(solid)
# --  短线(dashed)
# -.	短点相间图
# :	虚电线(dotted)
# '''


def plot():
    tmpp_file_path = "_graph_in.txt"
    f = open(tmpp_file_path)
    s = f.read().strip()
    f.close()

    num_list = [float(x.strip()) for x in s.split("\n")]
    print(num_list)
    print(len(num_list))

    color_list = ['blue', 'blue', 'blue','red', 'red','red']
    time_list = ["0.25h","0.5h", "1h", "2h", "3h", "4h"]
    total_num = len(color_list) * len(time_list)
    print(total_num)
    plt.figure(figsize=(16, 8))
    for i in range(len(color_list)):
        x = time_list.copy()
        x.insert(0, "0h")
        y = num_list[i * len(time_list):(i + 1) * len(time_list)]
        y.insert(0, 0)
        plt.plot(x, y, color=color_list[i], marker='o')
    plt.show()

def p():
    pass


if __name__ == '__main__':
    plot()
