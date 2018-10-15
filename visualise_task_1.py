import matplotlib.pyplot as plt
from matplotlib import interactive
import ast 
import re
import math

super_means_t = []
super_means_d = []
confidence_interval_t = []
confidence_interval_d = []
def calculate_metrics(input_file):
    global super_means_t
    global super_means_d
    global confidence_interval_t    
    global confidence_interval_d
   
    t_array = []
    d_array = []
    with open(input_file,'r') as f:
        for row in f:
            
            string = re.findall(r"\[(.*?)\]", row)        
            current = ast.literal_eval(string[0])
            if current[2] != 0:
        
                t_array.append(current[2] - current[0])
                d_array.append(current[1] - current[0])        
            
                        
    #drop first 1000 values
    t_array = t_array[1000:]
    batch_mean_t = []
    batch_mean_d = []
    t_950 = []
    d_950 = []
    for i in range(50):
        batch_mean_t.append(sum(t_array[1000*i:1000*(i+1)])/1000)
        batch_mean_d.append(sum(d_array[1000*i:1000*(i+1)])/1000)
        t_950.append(sorted(t_array[1000*i:1000*(i+1)])[950])
        d_950.append(sorted(d_array[1000*i:1000*(i+1)])[950])
        
    super_mean_t = sum(batch_mean_t)/50
    super_mean_d = sum(batch_mean_d)/50
    
    super_950_t = sum(t_950) / 50    
    super_950_d = sum(d_950) / 50    
    
    print(super_950_t, super_950_d)

    super_means_t.append(super_mean_t)
    super_means_d.append(super_mean_d)
    numerator_t = 0
    numerator_d = 0


    for i in range(50):
        numerator_t += (batch_mean_t[i] - super_mean_t)**2           
        numerator_d += (batch_mean_d[i] - super_mean_d)**2

    sample_variance_t = math.sqrt(numerator_t / 50)
    sample_variance_d = math.sqrt(numerator_d / 50)
    
    
    
    confidence_interval_t_current = [super_mean_t - 1.96*(sample_variance_t/math.sqrt(50)), super_mean_t + 1.96*(sample_variance_t/math.sqrt(50))] 
    confidence_interval_d_current = [super_mean_d - 1.96*(sample_variance_d/math.sqrt(50)), super_mean_d + 1.96*(sample_variance_d/math.sqrt(50))]     
    confidence_interval_t.append(confidence_interval_t_current)
    confidence_interval_d.append(confidence_interval_d_current)
    
for i in range(1,6):
    calculate_metrics(input_file= "mycsvfile_"+str(i)+".txt")

figure_1 = plt.figure(1)

plt.plot([1, 2, 3, 4, 5], super_means_t)
#print(super_means_t)
#print(confidence_interval_t)
for i in range(5):    
    plt.plot(i+1, confidence_interval_t[i][0], 'bo')
    plt.plot(i+1, confidence_interval_t[i][1], 'bo')
interactive(True)
plt.title("Plot of the super mean of service completion time: T")
plt.ylabel('Super Mean value for servie completion T')
plt.xlabel('Service Time')
figure_1.savefig("plot_of_T.png")
figure_1.show()


figure_2 = plt.figure(2)
plt.plot([1, 2, 3, 4, 5], super_means_d)
#print(super_means_d)
#print(confidence_interval_d)

for i in range(5):
    plt.plot(i+1, confidence_interval_d[i][0], 'bo')
    plt.plot(i+1, confidence_interval_d[i][1], 'bo')
plt.title("Plot of the super mean of orbital time: D")
plt.ylabel('Super Mean value for orbital times D')
plt.xlabel('Service Time')
interactive(False)
figure_2.savefig("plot_of_D.png")
figure_2.show()
input()

