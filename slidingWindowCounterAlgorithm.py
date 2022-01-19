import time

class SlidingWindowCounter:
    def __init__(self, capacity, time_unit, forward_callback, drop_callback) -> None:
        self.capacity = capacity
        self.time_unit = time_unit
        self.current_time = time.time()
        self.previous_count = capacity
        self.current_count = 0

        self.forward_callback = forward_callback
        self.drop_callback = drop_callback


    def handel(self, request_packet):
        # if the current time unit is passed, switch over to a new time unit
        if (time.time() - self.current_time) > self.time_unit:
            self.current_time = time.time()
            self.previous_count = self.current_count
            self.current_count = 0

        # estimates count = previous count * ((time unit - time into the current counter)/time unit) + current count
        estimated_count = (self.previous_count * (self.time_unit - (time.time() - self.current_time))/self.time_unit) + self.current_count

        if estimated_count > self.capacity:
            return self.drop_callback(request_packet)

        self.current_count += 1
        return self.forward_callback(request_packet)


# this function is called when a packet is forwarded
def forward_callback(request_packet):
    print("Request allowed: " + str(request_packet))

# this function is called when a packet is dropped
def drop_callback(request_packet):
    print("Request rate limited: " + str(request_packet))


throttle = SlidingWindowCounter(5, 1, forward_callback, drop_callback)
packet = 0

while True:
    time.sleep(0.1)
    throttle.handel(packet)
    packet += 1