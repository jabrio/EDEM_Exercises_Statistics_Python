
![Logo](https://n3m5z7t4.rocketcdn.me/wp-content/plugins/edem-shortcodes/public/img/logo-Edem.png)

## EDEM_Exercises_Statistics_Python
Activities that we carried out for statistics programming subject at EDEM.


**00 | Objectives**

```
- Make you fluent and comfortable in data management with Python.
- Make you competent in data-based decision making.
- Learning to learn Python autonomously.
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



