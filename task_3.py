import argparse
import math
from operator import itemgetter
import heapq
import random 
import json

random.seed(1)

def accept_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mean_inter_arrival_time", required = True, type = float, help = "set the input mean inter arrival time.")
    ap.add_argument("--mean_orbitting_time", required = True, type = float, help = "set the input mean orbitting time.")
    ap.add_argument("--service_time", required = True, type = float, help = "set the input service time.")
    ap.add_argument("--buffer_size", required = True, type = float, help = "set the input buffer size.")
    ap.add_argument("--end_simulation_time", required = True, type = float, help = "set simulation ending time.")
    ap.add_argument("--file_initial", required = True, type = str, help = "file initialiser")    
    args = vars(ap.parse_args())
    return args

#function to generate exponential random variate using inverse transformation method
def random_variate_generator(lambda_mean):
    logarithm = math.log(1-random.random())
    random_variate = -(logarithm)*lambda_mean
    return random_variate

#wirtes output at every instance of master clock to a text file
def write_to_text_file(string):
    with open('task_3_new.txt', 'a') as f:
        f.write(string+'\n')            

#function to obtain new service completion time
def get_new_service_completion_time(cls,service_time):
    return cls + service_time

#function to obtain new retransmitted time 
def get_new_retransmitted_time(clr):
    return clr + 5

#function to obtain new arrival time
def get_new_arrival_time(cla):
    return cla + 6

#Main function which iterates over master clock till end simulation time
def main(args):
    mean_inter_arrival_time = args["mean_inter_arrival_time"]
    mean_orbitting_time = args["mean_orbitting_time"]
    service_time = args["service_time"]
    buffer_size = args["buffer_size"]
    end_simulation_time = args["end_simulation_time"]
    file_initial = args["file_initial"]
    #time of first arrival = 2 seconds
    master_clock = 2
    cla = None
    cls = None
    #retransmitted_queue = Queue()
    heap = []
    
    #New additions to code
    data_storage_dict = {}
    unique_id = 0
    current_buffer_value = 0
    current_requests_in_buffer = []    
    #Events occuring arae events_new_arrival = "1" events_service_completion = "2" events_retransmitted_arrival = "3"
    event_FLAG = "1"
    flag = 'OFF'
    counter = 0 
    while True:

        #first check the type of event that is occuring and do as required
        if event_FLAG == "1":
            """
            do something about the new arrival
            """        
            data_storage_dict[unique_id] = [master_clock,master_clock,0]                
            random_variate = random_variate_generator(lambda_mean=mean_inter_arrival_time) 
                       
            cla = random_variate + master_clock
            
            #cla = get_new_arrival_time(cla)            
            if current_buffer_value < buffer_size :
                current_buffer_value += 1
                #put request inside buffer
                current_requests_in_buffer.insert(0,unique_id) 
                if not cls or cls == float("inf"):
                    cls = get_new_service_completion_time(master_clock, service_time)
            else:
                random_variate = random_variate_generator(lambda_mean=mean_orbitting_time)                
                clr = random_variate + master_clock
                #clr = get_new_retransmitted_time(clr)                
                data_storage_dict[unique_id][1] = clr
                heapq.heappush(heap, (clr, unique_id))           
            #increment counter for request ids
            unique_id += 1

        elif event_FLAG == "2":
            """
            do something about the service completion
            """
            
            current_buffer_value = current_buffer_value - 1                        
            which_request = current_requests_in_buffer.pop()
            data_storage_dict[which_request][2] = master_clock
            #cls = get_new_service_completion_time(master_clock, service_time)
            if current_requests_in_buffer:
                cls = get_new_service_completion_time(master_clock, service_time)
            else:
                cls = float("inf")                
            counter += 1
            #print(counter)
            if counter == end_simulation_time:
                break       
        else:
            """
            Do something about a retransmission arrival
            """
            if current_buffer_value < buffer_size :
                current_buffer_value +=1
                current_requests_in_buffer.insert(0, fetch_id)  
            else:
                random_variate = random_variate_generator(lambda_mean=mean_orbitting_time)
                clr = random_variate + master_clock                
                #clr = get_new_retransmitted_time(clr)                
                data_storage_dict[fetch_id][1] = clr                
                heapq.heappush(heap, (clr, fetch_id))
                
        #write the current status of the simulation process to output file 
        #string = str(master_clock)+"\t"+str(cla)+"\t"+str(cls)+"\t"+str(current_buffer_value)+"\t"+str(heap)
        #write_to_text_file(string)

        #predict the next event which is going to occur
        #Priority is assigned as 1.) Retransmitted Packet
        #                        2.) New Arrival
        #                        3.) Service completion

        if heap:
            clr , fetch_id = heap[0]
        else:
            clr = None
        
        if clr  == None:
            clr = float("inf")
        #print(cls,cla,clr,"adbweubf")
        if clr <= cla and clr <= cls:
            event_FLAG = "3"
            master_clock = clr
            heapq.heappop(heap)        
        elif cla <= cls and cla < clr:
            event_FLAG = "1"
            master_clock = cla
        else:
            #print("i am stuck here")
            if cls == float("inf"):
                #print ("hi")
                if clr <= cla:            
                    event_FLAG = "3"                    
                    master_clock = clr 
                else:
                    event_FLAG = "1"
                    master_clock = cla
            else:
                #print(cls,'hi')               
                event_FLAG = "2"
                master_clock = cls
        """        
        #check if you have to exit loop
        while counter < unique_id:
            if data_storage_dict[counter][2] != 0:
                counter += 1
                if counter == end_simulation_time:
                    flag = 'ON'
                    break 
                if counter in data_storage_dict:
                    continue
                else:
                    break            
            else:
                break
         
        if flag == 'ON':
            break                
        """
    count = 0
    print(data_storage_dict)
    
    with open("buffer_task_"+file_initial+".txt",'w') as f:
        for key,value in data_storage_dict.items():
            if value[2] == 0:
                count += 1
            f.write(str(key)+" "+str(value)+"\n")
        #print(data_storage_dict.items())
        #w.writerows(data_storage_dict.items())
    print(count)
    
if __name__ == "__main__":

    args = accept_arguments()
    print ("The given input arguments are:\n",args)
    main(args)
