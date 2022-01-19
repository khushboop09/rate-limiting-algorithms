import time

class FixedWindow:
    def __init__(self, capacity, forward_callback, drop_callback):
        self.current_time = int(time.time())
        self.capacity = capacity
        self.counter = 0
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

    def handle(self, request_packet):
        if int(time.time()) != self.current_time:
            self.current_time = int(time.time())
            self.counter = 0
        elif self.counter >= self.capacity:
            return self.drop_callback(request_packet)

        self.counter += 1
        return self.forward_callback(request_packet)


# this function is called when a packet is forwarded
def forward_callback(request_packet):
    print("Request allowed: " + str(request_packet))

# this function is called when a packet is dropped
def drop_callback(request_packet):
    print("Request rate limited: " + str(request_packet))


throttle = FixedWindow(2, forward_callback, drop_callback)

packet = 0

while True:
    time.sleep(0.2)
    throttle.handle(packet)
    packet += 1
