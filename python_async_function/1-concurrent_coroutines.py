#!/usr/bin/env python3
"""An asynchronous coroutine that takes in an integer argument"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that takes in an integer argument"""
    delays = [wait_random(max_delay) for i in range(n)]
    completed_delays = []
    for delay in asyncio.as_completed(delays):
        completed_delays.append(await delay)
    return completed_delays
