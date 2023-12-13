# Introduction

Weather patterns play an important role in the field of wind power generation. Enhancing dependability and performance of the power prediction models is necessary in order to carry out planned maintenance, cut down operational costs and to make improvements on existing technology [1].

The main objective of this project is to assess the impact of using additional weather information considering variations in temperature, pressure and also assessing the influence of a stability parameter like Obukhov Length[2] on model performance

# Objectives
#### Identify Features That Influence Power Production of a Wind Turbine : 
Temperature features (Air, Sea Surface, Land Surface, Dew point),  Pressure, Relative humidity and Obukhov Length (Atmospheric stability).

#### To Study Influence of Wind Flowing Across Land Versus Wind Flowing Across Sea on the Additional Features : 
Split turbine dataset based on 2 sectors one for Westerly Winds flowing across land and another for Easterly Winds flowing across sea.

#### Extract Additional Features Related to Weather Information That Were Identified: 
Climate reanalysis source like ERA5 was used to extract data for a point on land at the western side of the turbine and at sea on the eastern side of the turbine.

#### Combine Data From the Two Sources: 
Data from the turbine and ERA5 were combined based on the direction of data split and coordinate from which ERA5 climate reanalysis data was extracted. 
* For turbine data filtered based on wind flow across land, the ERA5 data extracted from a point on land was used. 
* For turbine data filtered based on wind flow across sea the ERA5 data extracted  from a point at sea was used.

#### Develop a Base Model for Comparison 
Base model was developed with key features selected from the turbine like wind speed, wind direction, pitch angle.


# Process Overview
![image](https://github.com/paul2596/oswt/assets/71576923/f38458e9-02e3-4172-8af5-e6400d6ebd12)

# Test Cases
![image](https://github.com/paul2596/oswt/assets/71576923/f969f305-a7f3-4acc-b8fd-1c461fe60ec6)
Temperature (T), Pressure (P), 2m Ambient Air Temperature (T2M), 2m Dew Point Temperature (D2M) (T2M and D2M are used to calculate relative humidity) , Temperature difference between sea/land surface and 2m ambient air (TD), Relative humidity(RH) and Obukhov length (ObhL) (A measure of turbulence and atmospheric stability ) [2]

# Results
From the plots comparing MAE scores with the base model, we see that Case 2 on adding temperature it influences power prediction and improves accuracy. For Case 3 on adding pressure there is no positive influence on model performance. Case 4 where temperature difference is used has a positive impact for wind flow across land compared to the case of wind flow across sea, this could be because land surface gets heated up easily and air would rise up creating a low pressure region and influence wind flow. But this is not the case for wind flowing across sea as water can absorb more heat and the air wouldn't heat up. For Case 5 we see that when 2m air and dew point temperatures which influence relative humidity are considered, the model performance improves. When the same 2 features were used to calculate relative humidity and used in Case 6 it does not have a postive impact on model performance. This could be because the model is able to capture the variation better from the two features when they are used separately. In Case 7 when Obukhov Length was used as an additional feature we see that this does not influence the power prediction. This could be because there might be lesser turbulence and influence of atmospheric stability. In case of a wind farm there would be more turbines in close vicinity which would be subjected to a wake effect as wind flows from one turbine to the other. Obukhov length does not have a positive impact on the power production model for the single test turbine that was used in our study.

![image](https://github.com/paul2596/oswt/assets/71576923/71dacdb6-c15d-483b-a25c-84280cc24b72)

![image](https://github.com/paul2596/oswt/assets/71576923/9620dc2e-20ea-49a1-978b-25045c8bedeb)


# Final App 
![image](https://github.com/paul2596/oswt/assets/71576923/e67bf2a8-fcab-4a4a-a48f-0fe3a17d769d)


https://github.com/paul2596/oswt/assets/71576923/9f23bc8d-b714-4248-8f2d-89e8c5f95c5c



# References
1. Alfredo Peinado Gonzalo, Tahar Benmessaoud, Mani Entezami, Fausto Pedro GarcÃ­a MÃ¡rquez, Optimal maintenance management of offshore wind turbines by minimizing the costs, https://doi.org/10.1016/j.seta.2022.102230.
2. Mike Optis, Jordan Perr-Sauer, The importance of atmospheric turbulence and stability in machine-learning models of wind farm power production,
https://doi.org/10.1016/j.rser.2019.05.031


