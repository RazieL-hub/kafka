from aiokafka import AIOKafkaConsumer
import asyncio
import json


async def consume():
    consumer = AIOKafkaConsumer(
        'test',
        bootstrap_servers='localhost:9093')
    # Get cluster layout and join group `my-group`
    await consumer.start()
    try:
        # Consume messages
        async for msg in consumer:
            print("consumed: ", msg.topic, msg.partition, msg.offset,
                  msg.key, json.loads(msg.value), msg.timestamp)
    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
