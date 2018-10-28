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
