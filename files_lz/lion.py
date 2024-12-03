import matplotlib.pyplot as plt
import pandas as pd
 
df = pd.read_orc(r"REALTIME.docx") 
print(df)
result = df['lion.py'].value_counts()
 
print(result.head()) # первые 5 элементов
print(result.values) # частоты  - по убыванию
print(result.keys()) # слова
print(result.values[0]) # частота самого частого слова
print(result.keys()[0]) # самое частотное слово
 
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
x_data = [i for i in range(len(result.values))]
plt.bar(x_data, result.values,color=colors)
plt.xticks(x_data,result.keys(),rotation=45) 
plt.ylabel("Frequency")
plt.savefig('img.png', dpi=800)
plt.show()
