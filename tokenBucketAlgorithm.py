import time

class Tokencapacity:

    def __init__(self, no_of_tokens, time_unit, forward_callback, drop_callback):
        self.no_of_tokens = no_of_tokens
        self.time_unit = time_unit
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback
        self.capacity = no_of_tokens
        self.last_check = time.time()

    def rate_limit(self, request_packet):
        current = time.time()
        time_passed = current - self.last_check
        self.last_check = time_passed

        self.capacity = self.capacity + (time_passed*(self.no_of_tokens/self.time_unit))

        if self.capacity > self.no_of_tokens:
            self.capacity = self.no_of_tokens

        if self.capacity < 1:
            self.drop_callback(request_packet)
        else:
            self.capacity = self.capacity - 1
            self.forward_callback(request_packet)


def forward_callback(request_packet):
    print("Request allowed: " + str(request_packet))

def drop_callback(request_packet):
    print("Request rate limited: " + str(request_packet))

packet = 0
throttle = Tokencapacity(1, 1,forward_callback, drop_callback)

while True:
    time.sleep(0.2)
    throttle.rate_limit(packet)
    packet += 1