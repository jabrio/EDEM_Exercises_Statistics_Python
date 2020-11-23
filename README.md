
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





