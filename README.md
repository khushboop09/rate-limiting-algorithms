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

3. Fixed Window Counter
4. Sliding Window Log
5. Sliding Window Counter