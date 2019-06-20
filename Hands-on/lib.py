from sklearn.linear_model import  LinearRegression

lst_train_x=[[1,2,3],[5,15,20]]
lst_train_y=[4,20]

lst_test_x=[[100,200,300],[15,20,25]]

lr=LinearRegression(normalize=True)
lr.fit(lst_train_x,lst_train_y)
ar_predict_y=lr.predict(lst_test_x)
print(ar_predict_y)