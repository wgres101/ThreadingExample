#spawn the three channels

import threading;
import time;

exitFlag = 0

class myThread (threading.Thread):
    
    def __init__(self, threadID,  name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter   
         
    def run(self):
        print("Starting " + self.name)
        print_time(self, self.name, self.counter, 5)
        print("Exiting " + self.name)
        
def print_time(self, threadName, counter, delay):
        while counter:
            if exitFlag:
                threadName.exit()
                time.sleep(delay)    
                print ("%s: s%" % (threadName, time.ctime( time.time() ) ))
                counter -= 1
       
                
#Create New Threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)

#Start New Threads
 
thread1.start()
thread2.start()
 
print ("Exiting Main Thread")       
 