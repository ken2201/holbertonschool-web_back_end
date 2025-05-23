#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay
    (included) seconds and return the delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
