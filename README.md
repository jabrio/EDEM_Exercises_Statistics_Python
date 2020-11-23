
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

- [ ] **Session 01: Describing nominal and quantitative data**
- [ ] Session 02: Subsetting data & avoiding artifacts
- [ ] Session 03: Recoding data
- [ ] Session 04: Bivariate analysis

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
- [ ] **Session 02: Subsetting data & avoiding artifacts**
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
- [ ] **Session 03: Recoding data**
- [ ] Session 04: Bivariate analysis

###### we want to classify the rentals in: Low rentals, Average rentals and High rentals:
###### The breakpoints will be c1=M-S and c2=M+S

```
wbr.loc[  (wbr['cnt']<(c1)) ,"cnt_str"]= "Low rentals"
wbr.loc[ ((wbr['cnt']>(c1)) & (wbr['cnt']<(c2))) ,"cnt_str"]= "Average rentals"
wbr.loc[  (wbr['cnt']>(c2)) ,"cnt_str"]= "High rentals"
```

```
wbr.groupby(["cnt_str"]).size()
```
Average rentals = **443** | High rentals = **143** | Low rentals = **145**

##### New order & plot the data

```
rental_list=["Low rentals", "Average rentals", "High rentals"]
order_rentals= CategoricalDtype(categories=rental_list, ordered=True)
wbr["order_rentals"]=wbr.cnt_str.astype(order_rentals)
B=wbr.groupby(["order_rentals"]).size()
plt.bar(rental_list, B, edgecolor="Black")
```

![Rentals_hist](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/12.png)

##### Quality control

```
plt.scatter(wbr.cnt, wbr.cnt_str, s=1)
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

plt.title("Quality Control OK" "\n")
```

![Rentals_QC](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/07.png)


### Session 04: Bivariate analysis

- [x] Session 01: Describing nominal and quantitative data
- [x] Session 02: Subsetting data & avoiding artifacts
- [x] Session 03: Recoding data
- [ ] **Session 04: Bivariate analysis**

##### A. Mean comparisons (Nominal vs Quantitative)

###### Why some days are rent more bikes than other days in Washington D.C.?
#### Case 01: Number of rentals by working day

##### Describing "Working day"

##### Recoding

```
wbr["wd_st"] = wbr.workingday
wbr.wd_st = wbr.wd_st.replace(to_replace=0, value="No")
wbr.wd_st = wbr.wd_st.replace(to_replace=1, value="Yes")

my_categories=["No", "Yes"]
my_datatype = CategoricalDtype(categories=my_categories, ordered=True)
wbr["wd_cat"] = wbr.wd_st.astype(my_datatype)

wbr.groupby(["wd_cat"]).size()
```
No = **231** | Yes = **500** 

##### Percentages

```
mytab=pd.crosstab(index=wbr["wd_cat"], columns="count")
print (mytab)
n=mytab.sum()
mytab2=mytab/n*100
print(mytab2)
```
No = **31.60** | Yes = **68.40** 

##### Plot the data

```
plt.bar(mytab2.index, mytab2['count'])
plt.xlabel('Working Day')
plt.title('Figure 03. Percentage of Working Days')
```
![Working_day](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/08.png)

##### ¿Rentals depend on the working day?

![WD+CNT](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/22.png)

```
wbr.groupby("wd_cat").cnt.mean()
```
No = **4330.17** | Yes = **4584.82**

##### T test

```
cnt_wd=wbr.loc[wbr.wd_cat=='Yes', "cnt"]
cnt_nwd=wbr.loc[wbr.wd_cat=='No', "cnt"]
```
```
stats.ttest_ind(cnt_wd, cnt_nwd, equal_var = False)
```
Ttest = **1.601** | pval = **0.11**

**pval>0.05 --> Rentals in Working day = Rentals in Holidays**

##### Plot the data

```
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="wd_cat", y="cnt", data=wbr,ci=95, join=0) 
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=M,
            linewidth=1,
            linestyle= 'dashed',
            color="green")
props = dict(boxstyle="round" ,facecolor="White", lw=0.5)
text_1='Mean:4504.3''\n''n:731' '\n' 't:1.601' '\n' 'Pval.:0.110'
plt.text(0.95, 5500,text_1, bbox=props)
plt.xlabel('Working Day')
plt.title('Figure 04. Average rentals by Working Day.''\n')
```
![Mean_Comparison_WD](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/09.png)

#### Case 02: Number of rentals by year

##### Recoding

```
wbr["wd_yr"] = wbr.yr
wbr.wd_yr = wbr.wd_yr.replace(to_replace=0, value="2011")
wbr.wd_yr = wbr.wd_yr.replace(to_replace=1, value="2012")

my_categories2=["2011", "2012"]
my_datatype2=CategoricalDtype(categories=my_categories2, ordered=True)
wbr["wd_cat_yr"] = wbr.wd_yr.astype(my_datatype2)
```

##### T test

```
cnt_wd_=wbr.loc[wbr.wd_cat_yr=='2011', "cnt"]
cnt_nwd_=wbr.loc[wbr.wd_cat_yr=='2012', "cnt"]
```
```
stats.ttest_ind(cnt_wd_, cnt_nwd_, equal_var = False)
```
Ttest = **18.577** | pval = **0.000**

**pval<0.05 --> Rentals in 2011 ≠ Rentals in 2012**

##### Plot the data

```
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="yr", y="cnt", data=wbr,ci=95, join=0) 
plt.yticks(np.arange(3000, 7000, step=500))
plt.ylim(2800,6200)
plt.axhline(y=M,
            linewidth=1,
            linestyle= 'dashed',
            color="green")
props = dict(boxstyle="round" ,facecolor="White", lw=0.5)
text_1='Mean:4504.3''\n''n:731' '\n' 't:18.6' '\n' 'Pval.:0.000'
plt.text(-0.4, 5500,text_1, bbox=props)
plt.xticks((0,1), ("2011", "2012"))
plt.xlabel("year")
plt.title('Figure 05. Average rentals by year.''\n')
```
![Mean_Comparison_YR](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/10.png)

#### Case 03: Number of rentals by Weather situation

```
wbr.groupby('ws').cnt.mean()
```
Cloudy = **4035.862** | Rainy = **1803.285** | Sunny = **4876.786**

##### T test

```
cnt_sunny=wbr.loc[wbr.ws=='Sunny', "cnt"] 
cnt_cloudy=wbr.loc[wbr.ws=='Cloudy', "cnt"]
cnt_rainy=wbr.loc[wbr.ws=='Rainy', "cnt"]
```
```
stats.f_oneway(cnt_sunny, cnt_cloudy, cnt_rainy)
```
Ttest = **40.066** | pval = **0.000**

**pval<0.05 --> Rentals differ in at least 2 of the 3 groups compared.**

##### Plot the data

```
plt.figure(figsize=(5,5))
ax = sns.pointplot(x="ws", y="cnt", data=wbr,ci=99.9, join=0) 
plt.yticks(np.arange(1000, 7000, step=500))
plt.ylim(800,6200)
plt.axhline(y=M,
            linewidth=1,
            linestyle= 'dashed',
            color="green")
props = dict(boxstyle="round" ,facecolor="White", lw=0.5)
text_1='Mean:4504.3''\n''n:731' '\n' 'F:40.06' '\n' 'Pval.:0.000'
plt.text(1.6, 5000,text_1, bbox=props)
plt.xlabel("\n" "year")
plt.title('Figure 06. Average rentals by weather situation.''\n')
```
![Mean_Comparison_WS](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/11.png)


##### B. Percentage comparisons (Nominal vs Nominal)

###### Why some days are rent more bikes than other days in Washington D.C.?
#### Case 01: ¿Is the same percentage of days with low/average/high rentals in working days vs not working days?

![Prc_Comparison_WD](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/23.png)

##### Crosstabulation
```
my_ct=pd.crosstab(wbr.order_rentals, wbr.wd_cat, normalize='columns', margins=True)*100
ct= pd.crosstab(wbr.order_rentals, wbr.wd_cat)
```
##### Chi2 test
```
stats.chi2_contingency(ct)
```
Chi2 = **4.983** | pval = **0.08**

**pval>0.05 --> Percentage of days with low/average/high rentals is the same in working days vs. not working days.**

##### Plot the data

```
my_ct.plot(kind="bar")
my_ct2= my_ct.transpose()
my_ct2.plot(kind="bar", edgecolor="Black", colormap="Blues")
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
plt.text(-0.4, 81, 'Chi2: 4.983''\n''n: 731' '\n' 'Pval.: 0.083', bbox=props)
plt.ylim(0,100)
plt.legend(['Low rentals','Average rentals','High rentals']) 
plt.xlabel("Working day" "\n")
plt.title("Figure 07. Percentage of Rental Level by Working Day" "\n")
plt.xticks(rotation='horizontal')
```
![Prc_Comparison_Plot](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/13.png)

#### Case 02: ¿Is the same percentage of days with low/average/high rentals in sunny/cloudy/rainy days?

![Prc_Comparison_WD](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/24.png)

##### Crosstabulation
```
my_ct_=pd.crosstab(wbr.order_rentals, wbr.order_new, normalize='columns', margins=True)*100
ct_02=pd.crosstab(wbr.order_rentals, wbr.order_new) 
```
##### Chi2 test
```
stats.chi2_contingency(ct_02)
```
Chi2 = **68.766** | pval = **0.000**

**pval<0.05 --> Percentage of days with low/average/high rentals is not the same in sunny/cloudy/rainy days.**

##### Plot the data

```
my_ct2_02=my_ct_.transpose()
my_ct2_02.plot(kind="bar", edgecolor="Black", colormap="Blues")
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
plt.text(-0.4, 81, 'Chi2: 4.13''\n''n: 731' '\n' 'Pval.: 0.000', bbox=props)
plt.ylim(0,100)
plt.legend(['Low rentals','Average rentals','High rentals']) 
plt.xlabel("Weather situation" "\n")
plt.title("Figure 08. Percentage of Rental Level \n by Weather situation" "\n")
plt.xticks(rotation='horizontal')
```
![Prc_Comparison_WD](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/14.png)

##### C. Correlation (Quantitative vs Quantitative)

###### Why some days are rent more bikes than other days in Washington D.C.?
#### Case 01: ¿Is there linear association between temperature and number of rentals??

![Correlation](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/25.png)

##### Pearson's r
```
X=wbr.temp_celsius
Y=wbr.cnt

from scipy.stats.stats import pearsonr
res=pearsonr(X, Y)
print(res)
```
Pearson's r = **0.627** | pval = **0.000**

**pval<0.05 --> There is a linear association between the number of rentals and the temperature.**

##### Plot the data

```
plt.figure(figsize=(5,5))
plt.scatter(X,Y,facecolors="none", edgecolor="C0")
plt.xlabel("Number of Rentals")
plt.ylabel("Temperature in Celsius")
plt.title("Figure 09. Daily rentals, by Temperature" "\n")
props = dict(boxstyle='round', facecolor='white', lw=0.5) 
text_scatter= "r: 0.62 \nn: 930 \nPval.: 0.000"
plt.text(2.5, 7500, text_scatter , bbox=props)
```
![Correlation_SP01](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/26.png)

#### Adding new variables: by Year.

```
plt.figure(figsize=(5,5))
plt.scatter (wbr.temp_celsius[wbr.yr==0], (wbr.cnt)[wbr.yr==0], s=20, marker="s", facecolors="none", edgecolors="C0", label="2011")
plt.scatter (wbr.temp_celsius[wbr.yr==1], (wbr.cnt)[wbr.yr==1], s=20, marker="s", facecolors="none", edgecolors="C1", label="2012")
plt.legend (loc="upper left")
plt.ylabel("Number of Rentals")
plt.xlabel("Temperature in Celsius")
plt.title("Figure 10. Daily rentals, by Temperature" "\n")
```
![Correlation_SP02](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/17.png)

#### Adding new variables: by Season.

```
plt.figure(figsize=(5,5))
plt.scatter (wbr.temp_celsius[wbr.season==1], (wbr.cnt)[wbr.season==1], s=20, marker="s", facecolors="none", edgecolors="C0", label="Winter")
plt.scatter (wbr.temp_celsius[wbr.season==2], (wbr.cnt)[wbr.season==2], s=20, marker="s", facecolors="none", edgecolors="C1", label="Spring")
plt.scatter (wbr.temp_celsius[wbr.season==3], (wbr.cnt)[wbr.season==3], s=20, marker="s", facecolors="none", edgecolors="C2", label="Summer")
plt.scatter (wbr.temp_celsius[wbr.season==4], (wbr.cnt)[wbr.season==4], s=20, marker="s", facecolors="none", edgecolors="C3", label="Fall")
plt.legend (loc="upper left")
plt.ylabel("Number of Rentals")
plt.xlabel("Temperature in Celsius")
plt.title("Figure 10. Daily rentals, by Temperature" "\n"))
```
![Correlation_SP02](https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/18.png)


