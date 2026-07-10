============================================================
DATASET LOADED SUCCESSFULLY
============================================================

First 5 Rows
       country  year iso_code  population  gdp  cement_co2  \
0  Afghanistan  1750      AFG   2802560.0  NaN         0.0   
1  Afghanistan  1751      AFG         NaN  NaN         0.0   
2  Afghanistan  1752      AFG         NaN  NaN         0.0   
3  Afghanistan  1753      AFG         NaN  NaN         0.0   
4  Afghanistan  1754      AFG         NaN  NaN         0.0   

   cement_co2_per_capita  co2  co2_growth_abs  co2_growth_prct  ...  \
0                    0.0  NaN             NaN              NaN  ...   
1                    NaN  NaN             NaN              NaN  ...   
2                    NaN  NaN             NaN              NaN  ...   
3                    NaN  NaN             NaN              NaN  ...   
4                    NaN  NaN             NaN              NaN  ...   

   share_global_other_co2  share_of_temperature_change_from_ghg  \
0                     NaN                                   NaN   
1                     NaN                                   NaN   
2                     NaN                                   NaN   
3                     NaN                                   NaN   
4                     NaN                                   NaN   

   temperature_change_from_ch4  temperature_change_from_co2  \
0                          NaN                          NaN   
1                          NaN                          NaN   
2                          NaN                          NaN   
3                          NaN                          NaN   
4                          NaN                          NaN   

   temperature_change_from_ghg  temperature_change_from_n2o  total_ghg  \
0                          NaN                          NaN        NaN   
1                          NaN                          NaN        NaN   
2                          NaN                          NaN        NaN   
3                          NaN                          NaN        NaN   
4                          NaN                          NaN        NaN   

   total_ghg_excluding_lucf  trade_co2  trade_co2_share  
0                       NaN        NaN              NaN  
1                       NaN        NaN              NaN  
2                       NaN        NaN              NaN  
3                       NaN        NaN              NaN  
4                       NaN        NaN              NaN  

[5 rows x 79 columns]

Last 5 Rows
        country  year iso_code  population           gdp  cement_co2  \
50406  Zimbabwe  2020      ZWE  15526887.0  2.317871e+10       0.496   
50407  Zimbabwe  2021      ZWE  15797220.0  2.514009e+10       0.542   
50408  Zimbabwe  2022      ZWE  16069061.0  2.590159e+10       0.387   
50409  Zimbabwe  2023      ZWE  16340829.0           NaN       0.387   
50410  Zimbabwe  2024      ZWE  16634366.0           NaN       0.387   

       cement_co2_per_capita     co2  co2_growth_abs  co2_growth_prct  ...  \
50406                  0.032   8.491          -1.776          -17.298  ...   
50407                  0.034  10.223           1.732           20.398  ...   
50408                  0.024  12.232           2.009           19.653  ...   
50409                  0.024  13.443           1.211            9.904  ...   
50410                  0.023  13.701           0.258            1.918  ...   

       share_global_other_co2  share_of_temperature_change_from_ghg  \
50406                     NaN                                 0.106   
50407                     NaN                                 0.105   
50408                     NaN                                 0.104   
50409                     NaN                                 0.103   
50410                     NaN                                 0.102   

       temperature_change_from_ch4  temperature_change_from_co2  \
50406                        0.001                        0.001   
50407                        0.001                        0.001   
50408                        0.001                        0.001   
50409                        0.001                        0.001   
50410                        0.001                        0.001   

       temperature_change_from_ghg  temperature_change_from_n2o  total_ghg  \
50406                        0.002                          0.0     24.146   
50407                        0.002                          0.0     27.907   
50408                        0.002                          0.0     29.917   
50409                        0.002                          0.0     31.029   
50410                        0.002                          0.0     31.066   

       total_ghg_excluding_lucf  trade_co2  trade_co2_share  
50406                    14.463      1.991           23.450  
50407                    16.408      2.137           20.899  
50408                    18.830      1.380           11.283  
50409                    20.318      1.876           13.957  
50410                    20.773        NaN              NaN  

[5 rows x 79 columns]

Dataset Shape
(50411, 79)

Column Names
Index(['country', 'year', 'iso_code', 'population', 'gdp', 'cement_co2',
       'cement_co2_per_capita', 'co2', 'co2_growth_abs', 'co2_growth_prct',
       'co2_including_luc', 'co2_including_luc_growth_abs',
       'co2_including_luc_growth_prct', 'co2_including_luc_per_capita',
       'co2_including_luc_per_gdp', 'co2_including_luc_per_unit_energy',
       'co2_per_capita', 'co2_per_gdp', 'co2_per_unit_energy', 'coal_co2',
       'coal_co2_per_capita', 'consumption_co2', 'consumption_co2_per_capita',
       'consumption_co2_per_gdp', 'cumulative_cement_co2', 'cumulative_co2',
       'cumulative_co2_including_luc', 'cumulative_coal_co2',
       'cumulative_flaring_co2', 'cumulative_gas_co2', 'cumulative_luc_co2',
       'cumulative_oil_co2', 'cumulative_other_co2', 'energy_per_capita',
       'energy_per_gdp', 'flaring_co2', 'flaring_co2_per_capita', 'gas_co2',
       'gas_co2_per_capita', 'ghg_excluding_lucf_per_capita', 'ghg_per_capita',
       'land_use_change_co2', 'land_use_change_co2_per_capita', 'methane',
       'methane_per_capita', 'nitrous_oxide', 'nitrous_oxide_per_capita',
       'oil_co2', 'oil_co2_per_capita', 'other_co2_per_capita',
       'other_industry_co2', 'primary_energy_consumption',
       'share_global_cement_co2', 'share_global_co2',
       'share_global_co2_including_luc', 'share_global_coal_co2',
       'share_global_cumulative_cement_co2', 'share_global_cumulative_co2',
       'share_global_cumulative_co2_including_luc',
       'share_global_cumulative_coal_co2',
       'share_global_cumulative_flaring_co2',
       'share_global_cumulative_gas_co2', 'share_global_cumulative_luc_co2',
       'share_global_cumulative_oil_co2', 'share_global_cumulative_other_co2',
       'share_global_flaring_co2', 'share_global_gas_co2',
       'share_global_luc_co2', 'share_global_oil_co2',
       'share_global_other_co2', 'share_of_temperature_change_from_ghg',
       'temperature_change_from_ch4', 'temperature_change_from_co2',
       'temperature_change_from_ghg', 'temperature_change_from_n2o',
       'total_ghg', 'total_ghg_excluding_lucf', 'trade_co2',
       'trade_co2_share'],
      dtype='object')

Dataset Information
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50411 entries, 0 to 50410
Data columns (total 79 columns):
 #   Column                                     Non-Null Count  Dtype  
---  ------                                     --------------  -----  
 0   country                                    50411 non-null  object 
 1   year                                       50411 non-null  int64  
 2   iso_code                                   42480 non-null  object 
 3   population                                 41167 non-null  float64
 4   gdp                                        15251 non-null  float64
 5   cement_co2                                 29173 non-null  float64
 6   cement_co2_per_capita                      25648 non-null  float64
 7   co2                                        29384 non-null  float64
 8   co2_growth_abs                             27216 non-null  float64
 9   co2_growth_prct                            26239 non-null  float64
 10  co2_including_luc                          23796 non-null  float64
 11  co2_including_luc_growth_abs               23496 non-null  float64
 12  co2_including_luc_growth_prct              23496 non-null  float64
 13  co2_including_luc_per_capita               23757 non-null  float64
 14  co2_including_luc_per_gdp                  16790 non-null  float64
 15  co2_including_luc_per_unit_energy          10133 non-null  float64
 16  co2_per_capita                             26509 non-null  float64
 17  co2_per_gdp                                17528 non-null  float64
 18  co2_per_unit_energy                        10826 non-null  float64
 19  coal_co2                                   21925 non-null  float64
 20  coal_co2_per_capita                        21314 non-null  float64
 21  consumption_co2                            5053 non-null   float64
 22  consumption_co2_per_capita                 4643 non-null   float64
 23  consumption_co2_per_gdp                    4448 non-null   float64
 24  cumulative_cement_co2                      29151 non-null  float64
 25  cumulative_co2                             27563 non-null  float64
 26  cumulative_co2_including_luc               23796 non-null  float64
 27  cumulative_coal_co2                        21925 non-null  float64
 28  cumulative_flaring_co2                     16111 non-null  float64
 29  cumulative_gas_co2                         18147 non-null  float64
 30  cumulative_luc_co2                         37450 non-null  float64
 31  cumulative_oil_co2                         25458 non-null  float64
 32  cumulative_other_co2                       3254 non-null   float64
 33  energy_per_capita                          10586 non-null  float64
 34  energy_per_gdp                             7787 non-null   float64
 35  flaring_co2                                16174 non-null  float64
 36  flaring_co2_per_capita                     14910 non-null  float64
 37  gas_co2                                    18147 non-null  float64
 38  gas_co2_per_capita                         17446 non-null  float64
 39  ghg_excluding_lucf_per_capita              35842 non-null  float64
 40  ghg_per_capita                             36179 non-null  float64
 41  land_use_change_co2                        37450 non-null  float64
 42  land_use_change_co2_per_capita             36635 non-null  float64
 43  methane                                    38150 non-null  float64
 44  methane_per_capita                         36179 non-null  float64
 45  nitrous_oxide                              38500 non-null  float64
 46  nitrous_oxide_per_capita                   36439 non-null  float64
 47  oil_co2                                    25459 non-null  float64
 48  oil_co2_per_capita                         24722 non-null  float64
 49  other_co2_per_capita                       2659 non-null   float64
 50  other_industry_co2                         3254 non-null   float64
 51  primary_energy_consumption                 10631 non-null  float64
 52  share_global_cement_co2                    22270 non-null  float64
 53  share_global_co2                           27563 non-null  float64
 54  share_global_co2_including_luc             23796 non-null  float64
 55  share_global_coal_co2                      21925 non-null  float64
 56  share_global_cumulative_cement_co2         22270 non-null  float64
 57  share_global_cumulative_co2                27563 non-null  float64
 58  share_global_cumulative_co2_including_luc  23796 non-null  float64
 59  share_global_cumulative_coal_co2           21925 non-null  float64
 60  share_global_cumulative_flaring_co2        11089 non-null  float64
 61  share_global_cumulative_gas_co2            15167 non-null  float64
 62  share_global_cumulative_luc_co2            37450 non-null  float64
 63  share_global_cumulative_oil_co2            23833 non-null  float64
 64  share_global_cumulative_other_co2          2170 non-null   float64
 65  share_global_flaring_co2                   11089 non-null  float64
 66  share_global_gas_co2                       15167 non-null  float64
 67  share_global_luc_co2                       37450 non-null  float64
 68  share_global_oil_co2                       23833 non-null  float64
 69  share_global_other_co2                     2170 non-null   float64
 70  share_of_temperature_change_from_ghg       41238 non-null  float64
 71  temperature_change_from_ch4                38280 non-null  float64
 72  temperature_change_from_co2                41238 non-null  float64
 73  temperature_change_from_ghg                41238 non-null  float64
 74  temperature_change_from_n2o                38280 non-null  float64
 75  total_ghg                                  38150 non-null  float64
 76  total_ghg_excluding_lucf                   37813 non-null  float64
 77  trade_co2                                  4712 non-null   float64
 78  trade_co2_share                            4712 non-null   float64
dtypes: float64(76), int64(1), object(2)
memory usage: 30.4+ MB

Statistical Summary
               year    population           gdp    cement_co2  \
count  50411.000000  4.116700e+04  1.525100e+04  29173.000000   
mean    1920.349249  6.017294e+07  3.300495e+11      7.890109   
std       65.859123  3.308412e+08  3.086383e+12     62.988171   
min     1750.000000  2.150000e+02  4.998000e+07      0.000000   
25%     1875.000000  3.272140e+05  7.874038e+09      0.000000   
50%     1925.000000  2.291264e+06  2.743861e+10      0.000000   
75%     1975.000000  9.986553e+06  1.212627e+11      0.524000   
max     2024.000000  8.161973e+09  1.301126e+14   1666.885000   

       cement_co2_per_capita           co2  co2_growth_abs  co2_growth_prct  \
count           25648.000000  29384.000000    27216.000000     26239.000000   
mean                0.060026    420.227035        6.268847        42.598225   
std                 0.123566   1972.092032       62.199548      1721.913018   
min                 0.000000      0.000000    -1928.339000      -100.000000   
25%                 0.000000      0.381000       -0.005000        -1.070500   
50%                 0.001000      5.081000        0.044000         3.813000   
75%                 0.077000     53.656500        1.018000        10.884000   
max                 2.484000  38598.578000     1804.657000    180870.000000   

       co2_including_luc  co2_including_luc_growth_abs  ...  \
count       23796.000000                  23496.000000  ...   
mean          544.144592                      7.483698  ...   
std          2273.281696                     99.512520  ...   
min           -84.560000                  -2298.978000  ...   
25%             6.667750                     -0.727500  ...   
50%            28.120000                      0.112000  ...   
75%           124.303250                      2.765250  ...   
max         43184.086000                   2614.874000  ...   

       share_global_other_co2  share_of_temperature_change_from_ghg  \
count             2170.000000                          41238.000000   
mean                 7.190616                              2.272236   
std                 17.448980                              9.282343   
min                  0.000000                             -0.824000   
25%                  0.144000                              0.003000   
50%                  0.588500                              0.081000   
75%                  2.416500                              0.373000   
max                100.000000                            100.000000   

       temperature_change_from_ch4  temperature_change_from_co2  \
count                 38280.000000                 41238.000000   
mean                      0.002871                     0.008014   
std                       0.015362                     0.045687   
min                      -0.001000                     0.000000   
25%                       0.000000                     0.000000   
50%                       0.000000                     0.000000   
75%                       0.000000                     0.001000   
max                       0.377000                     1.216000   

       temperature_change_from_ghg  temperature_change_from_n2o     total_ghg  \
count                 41238.000000                 38280.000000  38150.000000   
mean                      0.011224                     0.000509    490.799608   
std                       0.062888                     0.003048   2414.076755   
min                      -0.001000                     0.000000    -19.725000   
25%                       0.000000                     0.000000      1.502000   
50%                       0.000000                     0.000000     14.605500   
75%                       0.002000                     0.000000     76.508500   
max                       1.678000                     0.085000  54433.398000   

       total_ghg_excluding_lucf    trade_co2  trade_co2_share  
count              37813.000000  4712.000000      4712.000000  
mean                 310.521459    -6.986781        21.468641  
std                 1812.363570   259.018184        62.637598  
min                    0.000000 -2177.807000       -98.281000  
25%                    0.221000    -2.262250        -6.828750  
50%                    2.222000     1.641000         8.381500  
75%                   27.863000    11.425500        32.782250  
max                43714.777000  1768.846000      1023.042000  

[8 rows x 77 columns]

GENERALIZATIONS ABOUT THE DATASET

1. The dataset contains historical CO2 emission data for different countries.
2. Each row represents one country in a particular year.
3. Higher population generally leads to higher CO2 emissions.
4. Countries with higher GDP usually produce more CO2 because of industrial activities.
5. Higher energy consumption per person generally increases CO2 emissions.
6. Coal, oil, and gas are the major contributors to total CO2 emissions.
7. Cement production contributes to industrial CO2 emissions.
8. Methane emissions are commonly associated with agriculture and livestock.


RELATIONSHIP BETWEEN FEATURES

Country -> Identifies the nation.
Year -> Indicates the observation year.
Population -> Larger population often increases energy demand.
GDP -> Higher GDP is usually related to higher industrial emissions.
Energy_per_capita -> More energy consumption usually increases CO2.
Coal_CO2 + Oil_CO2 + Gas_CO2 -> Major sources of Total CO2.
Cement_CO2 -> Related to construction activities.
Methane -> Related to agriculture and livestock.


Missing Values
country                            0
year                               0
iso_code                        7931
population                      9244
gdp                            35160
                               ...  
temperature_change_from_n2o    12131
total_ghg                      12261
total_ghg_excluding_lucf       12598
trade_co2                      45699
trade_co2_share                45699
Length: 79, dtype: int64

Missing Values After Cleaning
country                           0
year                              0
iso_code                       7931
population                        0
gdp                               0
                               ... 
temperature_change_from_n2o       0
total_ghg                         0
total_ghg_excluding_lucf          0
trade_co2                         0
trade_co2_share                   0
Length: 79, dtype: int64

Total Countries
254

Year Range
1750 - 2024

Top 10 Countries by Average CO2
country
World                    6724.086742
OECD (GCP)               5652.511817
Non-OECD (GCP)           4625.621766
High-income countries    4187.906127
Europe (GCP)             3134.111554
Asia (GCP)               3112.347914
North America (GCP)      2813.686211
Asia                     2275.036865
Europe                   2010.439385
United States            1932.740276
Name: co2, dtype: float64

Average Population
49559024.584475614

Average GDP
118988442145.71623

Average Energy Per Capita
14402.141775564862

Correlation Matrix
                                 year  population       gdp  cement_co2  \
year                         1.000000    0.085638  0.066263    0.115035   
population                   0.085638    1.000000  0.382327    0.794324   
gdp                          0.066263    0.382327  1.000000    0.474964   
cement_co2                   0.115035    0.794324  0.474964    1.000000   
cement_co2_per_capita        0.352924    0.091135  0.095060    0.173910   
...                               ...         ...       ...         ...   
temperature_change_from_n2o  0.147650    0.810108  0.427388    0.787759   
total_ghg                    0.135904    0.857134  0.381857    0.811258   
total_ghg_excluding_lucf     0.140181    0.796746  0.405896    0.843288   
trade_co2                   -0.012838   -0.248230 -0.039541   -0.415415   
trade_co2_share              0.088477   -0.047337 -0.011654   -0.046416   

                             cement_co2_per_capita       co2  co2_growth_abs  \
year                                      0.352924  0.160155        0.059849   
population                                0.091135  0.696430        0.506558   
gdp                                       0.095060  0.369415        0.169672   
cement_co2                                0.173910  0.755172        0.512170   
cement_co2_per_capita                     1.000000  0.136711        0.090219   
...                                            ...       ...             ...   
temperature_change_from_n2o               0.134491  0.767059        0.415209   
total_ghg                                 0.142876  0.781157        0.501559   
total_ghg_excluding_lucf                  0.164433  0.798454        0.480597   
trade_co2                                -0.041052 -0.123699       -0.323172   
trade_co2_share                           0.003062 -0.038751       -0.029596   

                             co2_growth_prct  co2_including_luc  \
year                                0.002502           0.126606   
population                         -0.002495           0.883002   
gdp                                -0.001054           0.406689   
cement_co2                         -0.001634           0.851463   
cement_co2_per_capita              -0.004672           0.154564   
...                                      ...                ...   
temperature_change_from_n2o        -0.002518           0.904712   
total_ghg                          -0.002816           0.956126   
total_ghg_excluding_lucf           -0.002525           0.929356   
trade_co2                          -0.000044          -0.160012   
trade_co2_share                    -0.001181          -0.045838   

                             co2_including_luc_growth_abs  ...  \
year                                             0.033884  ...   
population                                       0.319356  ...   
gdp                                              0.073291  ...   
cement_co2                                       0.296713  ...   
cement_co2_per_capita                            0.048974  ...   
...                                                   ...  ...   
temperature_change_from_n2o                      0.249920  ...   
total_ghg                                        0.315773  ...   
total_ghg_excluding_lucf                         0.285973  ...   
trade_co2                                       -0.184818  ...   
trade_co2_share                                 -0.018438  ...   

                             share_global_other_co2  \
year                                       0.096681   
population                                 0.654084   
gdp                                        0.435298   
cement_co2                                 0.787086   
cement_co2_per_capita                      0.127350   
...                                             ...   
temperature_change_from_n2o                0.769956   
total_ghg                                  0.724094   
total_ghg_excluding_lucf                   0.775929   
trade_co2                                 -0.092427   
trade_co2_share                           -0.041508   

                             share_of_temperature_change_from_ghg  \
year                                                     0.052769   
population                                               0.651701   
gdp                                                      0.193370   
cement_co2                                               0.418323   
cement_co2_per_capita                                    0.059728   
...                                                           ...   
temperature_change_from_n2o                              0.656029   
total_ghg                                                0.778306   
total_ghg_excluding_lucf                                 0.680936   
trade_co2                                               -0.017833   
trade_co2_share                                         -0.030672   

                             temperature_change_from_ch4  \
year                                            0.150038   
population                                      0.871983   
gdp                                             0.393113   
cement_co2                                      0.811262   
cement_co2_per_capita                           0.137309   
...                                                  ...   
temperature_change_from_n2o                     0.969260   
total_ghg                                       0.984187   
total_ghg_excluding_lucf                        0.964722   
trade_co2                                      -0.148196   
trade_co2_share                                -0.049315   

                             temperature_change_from_co2  \
year                                            0.147351   
population                                      0.760475   
gdp                                             0.404393   
cement_co2                                      0.739607   
cement_co2_per_capita                           0.140530   
...                                                  ...   
temperature_change_from_n2o                     0.981284   
total_ghg                                       0.959751   
total_ghg_excluding_lucf                        0.968202   
trade_co2                                      -0.001868   
trade_co2_share                                -0.038151   

                             temperature_change_from_ghg  \
year                                            0.149938   
population                                      0.795648   
gdp                                             0.406280   
cement_co2                                      0.765145   
cement_co2_per_capita                           0.141110   
...                                                  ...   
temperature_change_from_n2o                     0.987719   
total_ghg                                       0.973576   
total_ghg_excluding_lucf                        0.975492   
trade_co2                                      -0.037978   
trade_co2_share                                -0.041199   

                             temperature_change_from_n2o  total_ghg  \
year                                            0.147650   0.135904   
population                                      0.810108   0.857134   
gdp                                             0.427388   0.381857   
cement_co2                                      0.787759   0.811258   
cement_co2_per_capita                           0.134491   0.142876   
...                                                  ...        ...   
temperature_change_from_n2o                     1.000000   0.954943   
total_ghg                                       0.954943   1.000000   
total_ghg_excluding_lucf                        0.962768   0.977512   
trade_co2                                      -0.036622  -0.156550   
trade_co2_share                                -0.044713  -0.045528   

                             total_ghg_excluding_lucf  trade_co2  \
year                                         0.140181  -0.012838   
population                                   0.796746  -0.248230   
gdp                                          0.405896  -0.039541   
cement_co2                                   0.843288  -0.415415   
cement_co2_per_capita                        0.164433  -0.041052   
...                                               ...        ...   
temperature_change_from_n2o                  0.962768  -0.036622   
total_ghg                                    0.977512  -0.156550   
total_ghg_excluding_lucf                     1.000000  -0.144991   
trade_co2                                   -0.144991   1.000000   
trade_co2_share                             -0.042095   0.119282   

                             trade_co2_share  
year                                0.088477  
population                         -0.047337  
gdp                                -0.011654  
cement_co2                         -0.046416  
cement_co2_per_capita               0.003062  
...                                      ...  
temperature_change_from_n2o        -0.044713  
total_ghg                          -0.045528  
total_ghg_excluding_lucf           -0.042095  
trade_co2                           0.119282  
trade_co2_share                     1.000000  

[77 rows x 77 columns]

SUMMARY

1. Imported the sustainability dataset using Pandas.
2. Explored the dataset using head, tail, shape, columns, info, and describe.
3. Studied the relationship between different features.
4. Checked missing values.
5. Filled missing numerical values using the median.
6. Filled missing country names with 'Unknown'.
7. Performed analysis such as total countries, year range, average values, and top CO2 emitting countries.
8. Generated the correlation matrix.
9. Saved the cleaned dataset as 'cleaned_sustainability_dataset.csv'.
10. The dataset is now cleaned and ready for further analysis or visualization.
