import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# 读取csv文件
df = pd.read_csv("rmsd.csv", header=None)

# 提取第二列和第三列
x = df.iloc[:, 1]
y = df.iloc[:, 2]


# 定义刻度格式化函数
def format_fn(tick_val, tick_pos=None):
    return '{:.0f}'.format(tick_val / 200)  # 除以因子


# 将刻度格式化函数向量化
vec_format_fn = np.vectorize(format_fn)

# 绘制折线图
fig, ax = plt.subplots()
ax.plot(x, y, color='blue', linewidth=4)
plt.ylim([0, 5])
plt.xlim([-200, 20200])

# 设置x轴刻度
ax.xaxis.set_major_formatter(ticker.FuncFormatter(vec_format_fn))

# 设置边距
plt.subplots_adjust(top=0.96, bottom=0.13, left=0.06, right=0.98)

# 添加标签和标题
plt.xlabel("Time (ns)", fontsize=36, fontweight='bold')
plt.ylabel("RMSD (Å)", fontsize=36, fontweight='bold')

# 外框线宽度
for spine in ax.spines.values():
    spine.set_linewidth(3)
    spine.set_edgecolor('black')

# 加粗坐标轴刻度文本的字体
for tick in ax.get_xticklabels():
    tick.set_weight('bold')
for tick in ax.get_yticklabels():
    tick.set_weight('bold')
# 设置x轴和y轴刻度文本字体大小
ax.tick_params(axis='x', labelsize=36)
ax.tick_params(axis='y', labelsize=36)

# 刻度线加粗
ax.tick_params(axis='both', which='major', width=3)
# 显示图形
fig.set_size_inches(20, 9)
plt.savefig('./rmsd.png')

