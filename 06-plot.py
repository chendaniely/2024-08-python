import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
tips

sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()

sns.lmplot(x="total_bill", y="tip", hue="sex", col="day", row="smoker", data=tips)
plt.show()

import plotnine as p9
from plotnine import ggplot, aes, geom_point

(ggplot(tips, aes(x="total_bill", y="tip"))
 + geom_point()
 + p9.facet_wrap("sex")
 + p9.theme_xkcd()
)

