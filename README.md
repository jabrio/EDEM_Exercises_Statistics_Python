
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
```
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
! [wbr.cnt.describe()] (https://github.com/jabrio/EDEM_Exercises_Statistics_Python/blob/main/Images/19.png)


