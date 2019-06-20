from sklearn.linear_model import  LinearRegression

lst_train_x=[[11.8,17.6,21.4],[9.7,15.7,21.6],[10.2,16.3,21.2],[11.2,16.3,20.6],[10.1,16.3,22.1],[11.1,17.1,22],[12.1,18.6,21.2],[12.4,18.4,21.4],[11.6,17.7,19],[12.7,17,21.1]]
lst_train_y=[24.9,26.3,26.5,25.4,25.1,24.9,25.2,24.6,25.9,27.4]

lst_test_x=[[10.8,18,20.3]]

lr=LinearRegression(normalize=True)
lr.fit(lst_train_x,lst_train_y)
ar_predict_y=lr.predict(lst_test_x)
print('7月の予想平均気温は{0}'.format(ar_predict_y))