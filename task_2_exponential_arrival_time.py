import argparse
import math

#define the retransmitted Queue
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def seek(self):
        if self.items == []:
            return None
        
        return sorted(self.items, reverse = True)[-1]
        
    def dequeue(self):
        
        self.items = sorted(self.items, reverse = True)  
        return self.items.pop()
                                                            
    def size(self):
        return len(self.items)
    
    def return_queue(self):
        return self.items

#imputs are
#mean inter arrival times
#mean orbitting time
#service time
#buffer size
#value of master clock at which the simulation will be terminated

def accept_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mean_inter_arrival_time", required = True, type = float, help = "set the input mean inter arrival time.")
    ap.add_argument("--mean_orbitting_time", required = True, type = float, help = "set the input mean orbitting time.")
    ap.add_argument("--service_time", required = True, type = float, help = "set the input service time.")
    ap.add_argument("--buffer_size", required = True, type = float, help = "set the input buffer size.")
    ap.add_argument("--end_simulation_time", required = True, type = float, help = "set simulation ending time.")
    args = vars(ap.parse_args())
    return args


xi = 1

#function to generate random number using congruential method
def rng(a, c, m):
    global xi
    xi = (a*xi + c)%m
    return xi/m

#function to generate exponential random variate using inverse transformation method
def random_variate_generator(lambda_mean, psuedo_random_number):
    logarithm = math.log(psuedo_random_number)
    random_variate = -(logarithm)*lambda_mean
    return random_variate

#main function to return generated random variate and seed
def random_number_main(lambda_mean, m=2**32, a=1103515245, c=12345):
    psuedo_random_number = rng(a, c, m)
    random_variate = random_variate_generator(lambda_mean, psuedo_random_number)
    return random_variate, psuedo_random_number


#wirtes output at every instance of master clock to a text file
def write_to_text_file(string):
    with open('results_exponential_arrival_time.txt', 'a') as f:
        f.write(string+'\n')            


#function to obtain new service completion time
def get_new_service_completion_time(cls):
    return cls + 10

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

    #time of first arrival = 2 seconds
    master_clock = 2
    cla = None
    cls = None
    retransmitted_queue = Queue()
    
    current_buffer_value = 0
    # Events occuring arae events_new_arrival = "1" events_service_completion = "2" events_retransmitted_arrival = "3"
    event_FLAG = "1"
    while master_clock <= end_simulation_time :

        #first check the type of event that is occuring and do as required
        if event_FLAG == "1":
            """
            do something about the new arrival
            """
            #uncomment for integer increment
            #cla = get_new_arrival_time(master_clock)

            random_variate, psuedo_random_number = random_number_main(lambda_mean= mean_inter_arrival_time)
            cla = random_variate + master_clock


            if current_buffer_value < buffer_size :
                current_buffer_value += 1
                if cls == None:
                    cls = get_new_service_completion_time(master_clock)
                
            else:
                #increment for integer increment
                #clr = get_new_retransmitted_time(master_clock)

                random_variate, psuedo_random_number = random_number_main(lambda_mean= mean_orbitting_time)
                clr = random_variate + master_clock

                retransmitted_queue.enqueue(clr)
                
        elif event_FLAG == "2":
            """
            do something about the service completion
            """
            cls = get_new_service_completion_time(master_clock)
            current_buffer_value = current_buffer_value - 1
        else:
            """
            Do something about a retransmission arrival
            """
            if current_buffer_value < buffer_size :
                current_buffer_value +=1
            else:
                #uncomment below for integer increment
                #clr = get_new_retransmitted_time(master_clock)
                
                random_variate, psuedo_random_number = random_number_main(lambda_mean= mean_orbitting_time)
                clr = random_variate + master_clock                

                retransmitted_queue.enqueue(clr)
        
        entire_queue = retransmitted_queue.return_queue()
        #write the current status of the simulation process to output file 
        string = str(master_clock)+"\t"+str(cla)+"\t"+str(cls)+"\t"+str(current_buffer_value)+"\t"+str(entire_queue)
        write_to_text_file(string)

        #predict the next event which is going to occur
        #Priority is assigned as 1.) Retransmitted Packet
        #                        2.) New Arrival
        #                        3.) Service completion
        
        clr  = retransmitted_queue.seek()
        
        if clr  == None:
            clr = float("inf")
            
        if clr <= cla and clr <= cls:
            event_FLAG = "3"
            master_clock = clr
            retransmitted_queue.dequeue()
        elif cla <= cls and cla < clr:
            event_FLAG = "1"
            master_clock = cla
        else:
            event_FLAG = "2"
            master_clock = cls



if __name__ == "__main__":

    args = accept_arguments()
    print ("The given input arguments are:\n",args)
    main(args)
