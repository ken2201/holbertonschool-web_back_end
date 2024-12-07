#!/usr/bin/env python3
"""A function that returns a list of delays in ascending order"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_random(max_delay: int) -> float:
    """Returns a Task object"""
    return await wait_random(max_delay)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in ascending order"""
    delays = [task_wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
