
![Logo](https://n3m5z7t4.rocketcdn.me/wp-content/plugins/edem-shortcodes/public/img/logo-Edem.png)

## EDEM_Exercises_Statistics_Python
Activities that we carried out for statistics subject at EDEM


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
###### (731, 16)

```
wbr.head()

```
 instant      dteday  season  yr  ...      hum  casual  registered   cnt
0        1  01/01/2011       1   0  ...  80.5833     331         654   985
1        2  02/01/2011       1   0  ...  69.6087     131         670   801
2        3  03/01/2011       1   0  ...  43.7273     120        1229  1349
3        4  04/01/2011       1   0  ...  59.0435     108        1454  1562
4        5  05/01/2011       1   0  ...  43.6957      82        1518  1600

[5 rows x 16 columns]

```
wbr.tail()
```

instant      dteday  season  yr  ...      hum  casual  registered   cnt
726      727  27/12/2012       1   1  ...  65.2917     247        1867  2114
727      728  28/12/2012       1   1  ...  59.0000     644        2451  3095
728      729  29/12/2012       1   1  ...  75.2917     159        1182  1341
729      730  30/12/2012       1   1  ...  48.3333     364        1432  1796
730      731  31/12/2012       1   1  ...  57.7500     439        2290  2729

[5 rows x 16 columns]

