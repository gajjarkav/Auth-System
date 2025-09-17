# a simple rate limiter for basic auth project 

import time 
from functools import wraps 
from fastapi import Request, HTTPException
def rate_limiter(max_requests: int, period: int):
    def decorator(func):
        calls = []

        @wraps(func)
        async def wrapper(request: Request,*args, **kwargs):
            now = time.time()
            calls_in_period = [call for call in calls if call > now - period]
            if len(calls_in_period) >= max_requests:
                raise HTTPException(status_code=429, detail="Too many requests, please try again later.")
            calls.append(now)
            return await func(request, *args, **kwargs)
        return wrapper
    return decorator