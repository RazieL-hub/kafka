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
            message = json.loads(msg.value)
            print(f"TYPE EVENT !!!!! {message.get('type_event')}")
            print(f"SEND TYPE !!!!! {message.get('send_type')}")
            print(f"PARAMETERS !!!!! {message.get('parameters')}")
            print(f"EMAIL FROM PARAMETERS !!!!! {message['parameters'].get('email')}")
            print(f"CHAT_ID FROM PARAMETERS !!!!! {message['parameters'].get('CHAT_ID')}")
            print(f"TEXT FROM PARAMETERS !!!!! {message['parameters'].get('text')}")


    finally:
        # Will leave consumer group; perform autocommit if enabled.
        await consumer.stop()


asyncio.run(consume())
