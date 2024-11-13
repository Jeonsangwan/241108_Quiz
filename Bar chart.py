import matplotlib.pylab as plt

categories = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Grape']
values = [25, 30, 15, 20, 35]
#plot 초기화
plt.clf()
#막대 그래프 생성
plt.bar(categories, values, color='skyblue')
#그래프 제목
plt.title('Fruit Sales')
#x y 축 이름
plt.xlabel('Fruits')
plt.ylabel('Sales')
#어디에 저장할건지
plt.savefig("./results/bar_chart.png")