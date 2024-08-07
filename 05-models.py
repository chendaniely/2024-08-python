import pandas as pd
import seaborn as sns
import statsmodels.formula.api as smf
from sklearn import linear_model

tips = sns.load_dataset("tips")

model = smf.ols("tip ~ total_bill", data=tips)

results = model.fit()

results.summary()


model = smf.ols("tip ~ total_bill + sex + smoker + size", data=tips)

results = model.fit()

results.summary()


lr = linear_model.LinearRegression()

lr.fit(X=tips[["total_bill"]], y=tips.tip)

lr.coef_
lr.intercept_



lr = linear_model.LinearRegression()
lr.fit(X=tips[["total_bill", "size"]], y=tips.tip)
lr.coef_
lr.intercept_

tips.info()
lr = linear_model.LinearRegression()
lr.fit(X=tips[["total_bill", "size", "smoker"]], y=tips.tip)
lr.coef_
lr.intercept_

tips_dummy = pd.get_dummies(tips)
tips_dummy_drop = pd.get_dummies(tips, drop_first=True)



tips.info()
lr = linear_model.LinearRegression()
lr.fit(X=pd.get_dummies(tips[["total_bill", "size", "smoker"]], drop_first=True), y=tips.tip)
lr.coef_
lr.intercept_

tips_model = pd.get_dummies(tips[["total_bill", "size", "smoker"]], drop_first=True)
tips.info()
lr = linear_model.LinearRegression()
lr.fit(X=tips_model, y=tips.tip)
lr.coef_
lr.intercept_

from patsy import dmatrices
formula = "tip ~ total_bill + size + smoker + day"

yX = dmatrices(formula, data=tips, return_type="dataframe")
y = yX[0]
X = yX[1]

x, y = [1, 2]
x
y
X

y, X = dmatrices(formula, data=tips, return_type="dataframe")
y

lr = linear_model.LinearRegression()
lr.fit(X=X, y=y)
lr.coef_
lr.intercept_
