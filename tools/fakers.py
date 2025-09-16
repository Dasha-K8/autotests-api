# генарация фековых данных для  отправки в апи

import time

def get_random_email() -> str:
    return f"test.{time.time()}@example.com"
