# IOT_project_01


Launch Script

1.)For hand simulation task

```
./task_2_hand_simulation.sh
```

set command line arguments accordingly

```
python3 task_2_hand_simulation.py --mean_inter_arrival_time 6 \
                  --mean_orbitting_time 5  \
                  --service_time 10 \
                  --buffer_size 2 \
                  --end_simulation_time 200

```

2.) For exponential simulation task

```
./task_2_exponential_arrival_time.sh
```

```
python3 task_2_exponential_arrival_time.py --mean_inter_arrival_time 6 \
                  --mean_orbitting_time 5  \
                  --service_time 10 \
                  --buffer_size 2 \
                  --end_simulation_time 200
```

3.)To run the simulation please use th shell script :


```
./task_3.sh
```

or from command line use


```
python3 task_3.py --mean_inter_arrival_time 6 \
                  --mean_orbitting_time 5  \
                  --service_time 5 \
                  --buffer_size 3 \
                  --end_simulation_time 51000 \
                  --file_initial 100
```


the file_initial input records the data for the T and D values in a text file named file_name_{file_initial}.txt
here the file name will be as mentioned in the task_3.py line 186 . 



to run the visualisations run the following for task 1 n or 2 respectively

```
python visualise_1.py
```
```
python visualise_2.py
```


to run the above visualisation code the following dependencies need to be installed 

```
import matplotlib.pyplot as plt
from matplotlib import interactive
import ast 
import re
import math
```


Check the project task lists here:
1.)[Task1](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/Simulation-task%201.pdf)
2.)[Task2](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/Simulation-task%202%20(new).pdf)
3.)[Task3](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/Simulation-task%203%20(new).pdf)

The output graphs and discussions can be found here: [task3 project report](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/Task%203.pdf)


Task description:
---


The task involves the simulation of an internet of things based system. the system consists of multiple sensors which transmit requests to an IOT server for same task query. The system involves a buffer wherein multiple requests can pileup. Also if buffer is full then the requests are retransmitted and come back and again check if buffer is empty.


All the request times are modelled on an exponential basis. We use a psuedo random number generator based on linear congruential generator. This random number generated is provided a seed to simulate the same results everytime. The reandom number is provided to a exponential random variate generator. The output of this exponential variate is used to calculate the next arrival time of a request. 


The system takes the following inputs :

```
1.) Mean Arrival time for a new request
2.) Mean Arrival time for a Retransmiited request
3.) Mean time for a Service to  request complete a request inside the procesor
4.) Buffer size 
5.) File to store output data of simulation.
6.) end simulation time / or the number of new requests for which we can run simulation.                 
```


This is the first graph where we can see that the new arrival time increases exponentially and the confidence interval also increases as we increase the Service complete time
![Figure 1](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/graphs/plot_of_T.png)


Also if we increase the buffer size the mean orbittal time time goes exponentially down and with that the confidence interval size decreases.
![Figure 2](https://github.ncsu.edu/ovbarve/IOT_project_01/blob/master/graphs/plot_of_D_buffer.png)
