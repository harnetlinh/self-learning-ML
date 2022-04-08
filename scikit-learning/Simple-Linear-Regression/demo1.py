import random
from sklearn.linear_model import LinearRegression

feature_set = []
target_set = []

number_of_rows = 200

random_number_limit = 2000

for i in range(0, number_of_rows):
    x = random.randint(0, random_number_limit)
    y = random.randint(0, random_number_limit)
    z = random.randint(0, random_number_limit)
    function = (10 * x) + (2 * y) + (3*z)
    feature_set.append([x, y, z])
    target_set.append(function)



model = LinearRegression()
model.fit(feature_set, target_set)
test_set = [[-1, 10, 0]]
prediction = model.predict(test_set)
print('Prediction:'+str(prediction)+'\t' + 'Coefficient:'+str(model.coef_))
