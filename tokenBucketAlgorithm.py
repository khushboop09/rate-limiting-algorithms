import time

class TokenBucket:
    #initialise the bucket and tokens
    def __init__(self, no_of_tokens, time_unit, forward_callback, drop_callback):
        # no. of tokens to be added in given time unit
        self.no_of_tokens = no_of_tokens
        # time frame to add token in
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback
        # initial capacity of the bucket
        self.capacity = no_of_tokens
        # timestamp of last handled request packet
        self.last_check = time.time()

    #check rate limit
    def handle(self, request_packet):
        current = time.time()
        #time passed since the last handled request packet
        time_passed = current - self.last_check
        self.last_check = current
        # self.no_of_tokens/self.time_unit =>  rate
        # (time_passed*(self.no_of_tokens/self.time_unit)) => this tells how many tokens should be added
        self.capacity = self.capacity + (time_passed*(self.no_of_tokens/self.time_unit))

        # if capacity becomes more than allowed, tokens will overflow => reset to max, else proceed
        if self.capacity > self.no_of_tokens:
            self.capacity = self.no_of_tokens
        
        # if not enough tokens, then drop the request
        if self.capacity < 1:
            self.drop_callback(request_packet)
        else:
            self.capacity = self.capacity - 1
            self.forward_callback(request_packet)


# this function is called when a packet is forwarded
def forward_callback(request_packet):
    print("Request allowed: " + str(request_packet))

# this function is called when a packet is dropped
def drop_callback(request_packet):
    print("Request rate limited: " + str(request_packet))

packet = 0
throttle = TokenBucket(1, 1, forward_callback, drop_callback)

while True:
    time.sleep(0.2)
    throttle.handle(packet)
    packet += 1
