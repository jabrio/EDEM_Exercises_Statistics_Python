
![Logo](https://n3m5z7t4.rocketcdn.me/wp-content/plugins/edem-shortcodes/public/img/logo-Edem.png)

## EDEM_Exercises_Statistics_Python
Activities that we carried out for statistics programming subject at EDEM.


**00 | Introduction: Objectives & contents**

```
- Make you fluent and comfortable in data management with Python.
- Make you competent in data-based decision making.
- Learning to learn Python autonomously.
```
```
- Session 01: Describing nominal and quantitative data.
- Session 02: Subsetting data & avoiding artifacts.
- Session 03: Recoding data.
- Session 04: Bivariate analysis.
```

**01 | Libraries**

```
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import scipy.stats as stats   
import seaborn as sns
```

**02 | Read File**

```
os.chdir('the path to your working directory here')
os.getcwd()
```
```ruby
wbr = pd.read_csv ("WBR_11_12_denormalized_temp.csv", sep=';', decimal=',')
```
```
wbr.shape
```
##### (731, 16)

```
wbr.head()
wbr.tail()
```

### Session 01: Describing nominal and quantitative data

##### A. Quantitative data
```
wbr.cnt.describe()
```
![wbr.cnt.describe](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/19.png) 

```
M=wbr.cnt.mean()
S=wbr.cnt.std()
c1=M-S
c2=M+S
```

##### Plot the data

```
x=wbr.cnt
plt.hist(x, edgecolor="Black")
plt.ylabel("Frecuency")
plt.xlabel("Daily rentals")
plt.title("Figure 01. Daily Bicycle rentals in Washington DC \n by Capital Bikeshare. 2011-2012")
```

```
plt.axvline(x=M,
            linewidth=1,
            linestyle="solid",
            Color="red",
            label="Mean")

plt.axvline(x=c1,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="- SD")

plt.axvline(x=c2,
            linewidth=1,
            linestyle="dashed",
            Color="green",
            label="+ SD")
```

```
text="n=731"
props=dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(0,130,text, bbox=props)
plt. legend(loc='upper left', bbox_to_anchor=(0.73, 0.98))
```
![plt.hist](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/03.png) 

##### B. Nominal data

##### Recoding

```
wbr.groupby(["weathersit"]).size()

wbr.loc[(wbr["weathersit"]==1),"ws"]="Sunny"
wbr.loc[(wbr["weathersit"]==2),"ws"]="Cloudy"
wbr.loc[(wbr["weathersit"]==3),"ws"]="Rainy"

wbr.groupby(["ws"]).size()
```

Cloudy = **247** | Rainy = **21** | Sunny = **463**

##### Order the variables & make percentages

```
bar_list=["Sunny", "Cloudy", "Rainy"]
order_new= CategoricalDtype(categories=bar_list, ordered=True)
wbr["order_new"]=wbr.ws.astype(order_new)

```
```
mytable=wbr.groupby(["order_new"]).size()
mytable_02=mytable/n*100
print(mytable_02)
```
Sunny = **63.33** | Cloudy = **33.79** | Rainy = **2.88**

##### Plot the data

```
plt.bar(bar_list, mytable_02, edgecolor="Black")
plt.ylabel("Percentage")
plt.title ("Figure 02. Percentage of weather situation")
text="n=731"
props=dict(boxstyle="round", facecolor="white", lw=0.5)
plt.text(2,60,text, bbox=props)
```

![plt.bar](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/04.png) 

### Session 02: Subsetting data & avoiding artifacts

- [x] Session 01: Describing nominal and quantitative data
- [ ] Session 02: Subsetting data & avoiding artifacts
- [ ] Session 03: Recoding data
- [ ] Session 04: Bivariate analysis

##### A. Subsetting

```
wbr_2011=wbr[wbr.yr==0] --> year 2011.
wbr_2012=wbr[wbr.yr==1] --> year 2012.
```

##### B. Avoiding artifacts

```
plt.hist(wbr_02.temp_celsius, edgecolor="Black")
plt.xlabel("Temp_Celsius")
```
![Temp_celsius](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/05.png)

```
wbr.temp_celsius.describe()
```

![temp_celsius_describe](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/20.png)

##### Delete wrong values

```
wbr_02['temp_celsius_c']=wbr_02.temp_celsius.replace(99,np.nan)
```
```
wbr_02.temp_celsius_c.describe()
```
![temp_celsius_describe](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/21.png)

##### Plot the data

```
plt.hist(wbr_02.temp_celsius_c, edgecolor="Black")
plt.xlabel("Temp_Celsius")
plt.ylabel("Frecuency")
plt.title ("Temperature in Washington DC. 2011-2012" "\n")
```
![temp_celsius_plot](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/06.png)

### Session 03: Recoding data

- [x] Session 01: Describing nominal and quantitative data
- [x] Session 02: Subsetting data & avoiding artifacts
- [ ] Session 03: Recoding data
- [ ] Session 04: Bivariate analysis
