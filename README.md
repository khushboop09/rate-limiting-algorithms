# Rate Limiting Algorithms in Python

1. Token Bucket Algorithm

    The token bucket algorithm works as follows:
    
    - A token bucket is a container with fixed capacity. Tokens are put in the bucket at pre-defined rate periodically. Once the bucket is full, we cannot add more tokens.

        For example: If the bucket capacity is 4 and we will put 2 tokens into the bucket every second. Rate limit is 4 tokens per second or 4 requests per second.
    
    - Each request uses 1 token from the bucket and the request goes through

    - If enough tokens are not there in the bucket, the request is dropped.

2. Leaky Bucket Algorithm

    The leaky bucket Algorithm is similar to token bucket algorithm except the requests are processed at a fixed rate. Usually implemented with a FIFO queue.

    It works as follows:

    - When a request arrives first check if the queue is full or not. If it is full, the request is dropped.

    - Otherwise, the request is added to the queue.

    - The requests are then pulled from the queue and prcoessed at regular intervals.

    The advantage of leaky bucket over token bucket algorithm is that we will have stable outflow rate of the requests, since the requests are processed at a fixed rate.

3. Fixed Window Counter Algorithm

    The fixed window counter algorithm works as follows:

    - The timeline is divided into fix-sized time windows and a counter is assigned for each window.

    - Each request increments the counter by one.

    - Once the counter reaches the predefined threshold value, new requests are dropped until the new window starts.

    For example: fixed-size time window is 3 requests per second, therefore we will divide the timeline into 1 sec windows. In each window if more than 3 requests are received, the extra requests are dropped. 

    The biggest con of this algorithm is sudden traffic spike can be noticeable at the edge of a window.

4. Sliding Window Log Algorithm

    The sliding window log algorithm works as follows:

    - We keep track of request timestamps for each user.

    - When a new request comes remove all the outdated timestamps i.e. timestamps older than the start of the current time window.

    - Add new request timestamp to the log.

    - If the log size is same or lower than the allowed count, request is accepted. Otherwise, it is rejected.

5. Sliding Window Counter Algorithm