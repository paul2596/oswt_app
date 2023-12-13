# IMPACT OF THE USE OF WEATHER INFORMATION ON THE ACCURACY OF POWER PRODUCTION MODELS FOR OFFSHORE WIND TURBINES
# Introduction

Weather patterns play an important role in the field of wind power generation. Enhancing dependability and performance of the power prediction models is necessary in order to carry out planned maintenance, cut down operational costs and to make improvements on existing technology [1].

The main objective of this project is to assess the impact of using additional weather information considering variations in temperature, pressure and also assessing the influence of a stability parameter like Obukhov Length[2] on model performance

# Objectives
#### 1. Identify Features That Influence Power Production of a Wind Turbine : 
Temperature features (Air, Sea Surface, Land Surface, Dew point),  Pressure, Relative humidity and Obukhov Length (Atmospheric stability).

#### 2. To Study Influence of Wind Flowing Across Land Versus Wind Flowing Across Sea on the Additional Features : 
Split turbine dataset based on 2 sectors one for Westerly Winds flowing across land and another for Easterly Winds flowing across sea.

#### 3. Extract Additional Features Related to Weather Information That Were Identified: 
Climate reanalysis source like ERA5 was used to extract data for a point on land at the western side of the turbine and at sea on the eastern side of the turbine.

#### 4. Combine Data From the Two Sources: 
Data from the turbine and ERA5 were combined based on the direction of data split and coordinate from which ERA5 climate reanalysis data was extracted. 
* For turbine data filtered based on wind flow across land, the ERA5 data extracted from a point on land was used. 
* For turbine data filtered based on wind flow across sea the ERA5 data extracted  from a point at sea was used.

#### 5. Develop a Base Model for Comparison 
Base model was developed with key features selected from the turbine like wind speed, wind direction, pitch angle.


# Process Overview
![image](https://github.com/paul2596/oswt_app/assets/71576923/2af8402a-79c0-4d87-91e1-15f28abb42fa)


# Outlier Removal
![image](https://github.com/paul2596/oswt_app/assets/71576923/db33915e-b2a0-4a49-9a78-e45ac774ce7a)

Outliers were identified in the readings which could be due to the downtime during maintenance or
other test conditions, this can be seen from the plot for power generated versus wind speed in Figure(a) above. The outliers
were excluded by referring to the power curve which was obtained by isolating datapoints by setting a contamination
value using isolated forest [3] and fitting a cubic spline to the isolated points as indicated by the red spline in Figure(a).
Based on the power curve obtained in Figure(a) we see that for around 3000kW there are deviations which could be
caused by test conditions or anomalies that we are not informed of; we remove outliers in this region. Further, we see
that there are significant number of readings with zero power output for higher wind speeds, this could be because of
the downtime of the turbine.

The cut in speed for the turbine is 3.5m/s, considering a margin for error we remove the outliers where power
output is less than 1kW when wind speed is greater than 4.5m/s. The cleaned data for the timeline considered can be
seen in Figure(b) above

# Feature Selection
![image](https://github.com/paul2596/oswt_app/assets/71576923/21c2e31b-86ef-41d9-a6b1-da8240b6c09f)

Feature Correlation analysis was done to identify highly correlating features captured from the turbine. From the Figure(a) above
We see that wind speeds have a high correlation with power.It can also be noted that wind speed(T) captured at turbine
has a higher correlation compared to wind speed(MM) which is captured from the met mast, this could be because of
the distance at which the met mast is located. The other features like wind direction and pitch angle do not show a high
correlation, these features were further explored using the feature importance obtained from random forest.
The features to build a base model without additional weather information were finalized after following a backward
elimination process using feature importance from random forest as shown in Figure(b)

# Directional Split
![image](https://github.com/paul2596/oswt_app/assets/71576923/74643f62-e37f-4352-aed4-f732d20f09a4)

To study the directional characteristics of wind and the influence on the additional features in more detail, we perform
a directional split. For this the latitude and longitude coordinates for 3 different points were considered as shown
in Figure(a) where Point A is at the location of the turbine, point C and B are connected with A by lines passing
tangential to the shore, this forms a triangular section. Post locating the points, the angle made by the tangential lines
AB and AC with reference to the North (degN) were calculated using the equation for azimuth distance.
The angle made with reference to the North based on Azimuth angle (Az) for 2 points A and B is given by:

![image](https://github.com/paul2596/oswt_app/assets/71576923/7cdfa199-367b-461b-aa4c-0e78280da432)

After using the angles to perform the directional split we use a wind rose[4] to visualize the characteristics of wind
before and after performing the split as shown in Fig (b)and(c).

# Test Cases
![image](https://github.com/paul2596/oswt_app/assets/71576923/3fdb66f5-b771-493b-9dc3-aeab68ff0bec)


Different test cases were formed by combining the base model with additional weather information like, 
Temperature (T), Pressure (P), 2m Ambient Air Temperature (T2M), 2m Dew Point Temperature (D2M) (T2M and D2M are used to calculate relative humidity) , Temperature difference between sea/land surface and 2m ambient air (TD), Relative humidity(RH) and Obukhov length (ObhL) (A measure of turbulence and atmospheric stability ) [2]

# Results
From the plots comparing MAE scores with the base model, we see that Case 2 on adding temperature it influences power prediction and improves accuracy. For Case 3 on adding pressure there is no positive influence on model performance. Case 4 where temperature difference is used has a positive impact for wind flow across land compared to the case of wind flow across sea, this could be because land surface gets heated up easily and air would rise up creating a low pressure region and influence wind flow. But this is not the case for wind flowing across sea as water can absorb more heat and the air wouldn't heat up. For Case 5 we see that when 2m air and dew point temperatures which influence relative humidity are considered, the model performance improves. When the same 2 features were used to calculate relative humidity and used in Case 6 it does not have a postive impact on model performance. This could be because the model is able to capture the variation better from the two features when they are used separately. In Case 7 when Obukhov Length was used as an additional feature we see that this does not influence the power prediction. This could be because there might be lesser turbulence and influence of atmospheric stability. In case of a wind farm there would be more turbines in close vicinity which would be subjected to a wake effect as wind flows from one turbine to the other. Obukhov length does not have a positive impact on the power production model for the single test turbine that was used in our study.

![image](https://github.com/paul2596/oswt_app/assets/71576923/2571754d-0a66-456b-848a-5b1b5645d256)


![image](https://github.com/paul2596/oswt_app/assets/71576923/f8d66ccf-4b49-4681-b613-c09648b01c81)



# Final App 
![image](https://github.com/paul2596/oswt_app/assets/71576923/0aece5d6-fcb4-4476-b6f4-9d650488b242)





Uploading final_app.mp4…





# References
1. Alfredo Peinado Gonzalo, Tahar Benmessaoud, Mani Entezami, Fausto Pedro GarcÃ­a MÃ¡rquez, Optimal maintenance management of offshore wind turbines by minimizing the costs, https://doi.org/10.1016/j.seta.2022.102230.
2. Mike Optis, Jordan Perr-Sauer, The importance of atmospheric turbulence and stability in machine-learning models of wind farm power production,
https://doi.org/10.1016/j.rser.2019.05.031
3. Z. Lin, X. Liu, and M. Collu, “Wind power prediction based on high-frequency scada data along with isolation forest and deep learning neural networks,” International Journal of Electrical Power Energy Systems, vol. 118, p. 105835, 2020. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S0142061519332491
4. “How to read a wind rose,” https://www.epa.gov/sites/default/files/2019-01/documents/how_to_read_a_wind_rose.pdf, accessed: 2023-08-10.

