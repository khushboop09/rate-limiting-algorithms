import time
import random

class LeakyBucket:
    def __init__(self, capacity, forward_callback, drop_callback) -> None:
        # total no of tokens in buckets at any given time, here it means intially
        self.no_of_tokens_in_bucket = 0
        # total no. of requests that can be added to the bucket
        self.capacity = capacity
        #no. of packets that exits the bucket at a time
        self.output_rate = 1

        self.forward_callback = forward_callback
        self.drop_callback = drop_callback


    def handle(self, total_request_packets):
        print("No of requests received: "+str(total_request_packets))
        # capacity of the bucket at the moment
        capacity_left = self.capacity - self.no_of_tokens_in_bucket
        
        if(total_request_packets <= capacity_left):
            self.no_of_tokens_in_bucket += total_request_packets
            self.forward_callback(total_request_packets)
        else:
            #drop extra packets
            self.drop_callback(total_request_packets-capacity_left)
            self.no_of_tokens_in_bucket = self.capacity
        
        self.no_of_tokens_in_bucket -= self.output_rate
        print("Capacity left:"+str(self.capacity - self.no_of_tokens_in_bucket))

# this function is called when a packet is forwarded
def forward_callback(no_of_request_packet):
    print("Requests allowed: " + str(no_of_request_packet))

# this function is called when a packet is dropped
def drop_callback(no_of_request_packet):
    print("Request rate limited: " + str(no_of_request_packet))


packet = 0

throttle = LeakyBucket(10, forward_callback, drop_callback)

while True:
    time.sleep(1)
    #get random no. for request burst check
    total_requests = random.randint(4,9)
    throttle.handle(total_requests)