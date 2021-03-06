import time

class Buffer:
    def __init__(self, buffer_size = int, buffer = []):
        self.buffer_size = buffer_size
        self.queue = buffer

    def is_empty(self):
        if len(self.queue) == 0:
            return True

    def __str__(self):
        return str([str(self.buffer_size), str(self.queue)])

class LeakyBucket:
    def __init__(self, capacity, output_rate, buffer_size, forward_callback, drop_callback):
        self.capacity = capacity
        self.buffer = Buffer(buffer_size)
        self.output_rate = output_rate
        self.tokens_in_bucket = str
        self.forward_callback = forward_callback
        self.drop_callback = drop_callback

    def handle(self, request_packet):
        count = 0
        if self.buffer.is_empty():
            for i in range(0, len(request_packet)):
                if i < self.output_rate:
                    self.forward_callback(request_packet[i])
                else:
                    if count < self.buffer.buffer_size:
                        self.buffer.queue.append(request_packet[i])
                        count = len(self.buffer.queue)
                    else:
                        self.drop_callback(request_packet[i])
        else:
            j=0
            for i in range(0, len(request_packet)+len(self.buffer.queue)):
                if i < self.output_rate:
                    if self.buffer.is_empty():
                        self.forward_callback(self.buffer.queue[0])
                        del self.buffer.queue[0]
                    else:
                        self.forward_callback(request_packet[j])
                        j += 1
                else:
                    if len(self.buffer.queue) < self.buffer.buffer_size:
                        if j < len(request_packet):
                            self.buffer.queue.append(request_packet[j])
                            j += 1
                    else:
                        if j < len(request_packet):
                            self.drop_callback(request_packet[j])
                            j += 1

# this function is called when a packet is forwarded
def forward_callback(request_packet):
    print("Requests allowed: " + str(request_packet))

# this function is called when a packet is dropped
def drop_callback(no_of_request_packet):
    print("Request rate limited: " + str(no_of_request_packet))

throttle = LeakyBucket(10, 2, 5, forward_callback, drop_callback)

while True:
    time.sleep(1)
    request_packet = input("Enter a string send by the server: ")
    throttle.handle(request_packet)