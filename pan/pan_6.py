import pandas as pd
df=pd.read_csv('Testdata.csv')
jap_data_list=df.国語.values.tolist()
jap_average=sum(jap_data_list)/len(jap_data_list)

math_data_list=df.数学.values.tolist()
math_average=sum(math_data_list)/len(math_data_list)

eng_data_list=df.英語.values.tolist()
eng_average=sum(eng_data_list)/len(eng_data_list)

print('国語の平均は:{0}'.format(jap_average))
print('数学の平均は:{0}'.format(math_average))
print('英語の平均は:{0}'.format(eng_average))