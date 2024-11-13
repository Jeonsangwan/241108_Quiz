import matplotlib.pyplot as plt
import random
x = [random.uniform(0, 100) for _ in range(1000)]
y = [random.uniform(0, 100) for _ in range(1000)]

plt.clf()

plt.scatter(x, y, label='Random Data Points', color='green', marker='o', s=30, alpha=0.5)

plt.title('Scatter Plot Example')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.legend()

plt.savefig('./results/scatter_chart_1.png')

#plt.close() -> 그래프 표시하지 않고 바로 저장