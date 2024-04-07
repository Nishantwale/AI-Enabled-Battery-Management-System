# README File - Team The Futurists

## Requirements:
- Adafruit_DHT library must be installed on Raspberry Pi.
- Pushbulllet.py must be installed on Raspberry Pi.

## Key Points:
1. As per the flow diagram, the setup has been completed successfully.
2. Data from the sensors has been read successfully.
3. Data has been stored successfully on the cloud server (ThingSpeak).
4. Live data of BMS can be shared by adding a Gmail ID of any person or BMS ycompany.
5. Companies can fetch data and they use for further improvement of BMS and their technologies.
6. A .csv file of data values has been successfully obtained for further ML Model Training.
   

## All the queries of Judges Implemented Successfully:
1. Some times even the .csv file shows the unusual patterns which are anonymous behavior. For concerning this data security issue we went with the Anomaly Detector. This will ensure to protect the data leakage and will also give the user a secure way to tackle with their data. 
2. We used Pushbullet platform for intimating user using APIs Keys (Notify User).
  - Notification -------> Android, iOS, any browser.
  - Filtered notfications.
3. Trained the Linear Regression ML Model to visulaize the BMS data for further analyzing and relationship between the attributes.
4. We have implemented Decison Tree on which basis we can find the dependant factors on the independant factors.

## Current Work on Machine Learning Algorithms:
- Support Vector Regression (SVR)
- Decision Tree Regression
- Random Forest Regression
- Linear Regression

## Future work on Machine Learning Algorithms:
- Polynomial Regression
- ElasticNet Regression
- Gradient Boosting Regression

## Future work on Hardware Components:
- Ideal Temperature of battery = 20°C - 35°C
    - Heater Function = Tempearture < 20°C---------> coolent heater Turned on.
- Insect Trap = IR sensors senses disturbance------> Trapped
