import matplotlib.pyplot as plt
import numpy as np #import = 불러와라, numpy = 행렬연산 빠르게 처리하는 친구, np = numpy를 np라고 부를게

#랜덤 데이터 생성
data = np.random.randn(1000) #1000개의 랜덤 데이터

plt.clf()

plt.hist(data, bins = 20, color = 'skyblue', edgecolor = 'black') #옵션내용 gpt에 물어보자

plt.title('Histogram Chart')

plt.xlabel('Values')
plt.ylabel('Frequency')

plt.savefig('./results/histogram.png')