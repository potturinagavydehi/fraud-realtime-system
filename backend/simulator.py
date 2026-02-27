import random
import uuid
import time

def generate_transaction():
    return {
        "id": str(uuid.uuid4()),
        "amount": round(random.uniform(10, 5000), 2),
        "velocity": random.randint(1, 10),
        "is_foreign": random.choice([True, False]),
        "Time": random.uniform(0, 172800),
        "V": [random.uniform(-3, 3) for _ in range(28)]
    }