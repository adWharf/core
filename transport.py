#!/usr/bin/env python
# encoding: utf-8


"""
@author: william
@contact: 1342247033@qq.com
@site: http://www.xiaolewei.com
@file: kafka.py
@time: 27/05/2018 15:20
"""
import json
import functools
from kafka import KafkaConsumer
from kafka import KafkaProducer
from . import config
from . import logger


def sub(topics, client, group, **kwargs):
    kafka_server = '%s:%d' % (config.get('app.kafka.host'), config.get('app.kafka.port'))
    consumer = KafkaConsumer(topics,
                             client_id=client,
                             group_id=group,
                             bootstrap_servers=kafka_server,
                             **kwargs)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for msg in consumer:
                try:
                    logger.info('Receive data from kafka for consumer [%s]' % client)
                    kwargs['message'] = msg
                    func(*args, **kwargs)
                except Exception as e:
                    logger.error('Err when handle data')
                    logger.error(e)
                    pass

        return wrapper

    return decorator


def pub(topic, client, **kwargs):
    kafka_server = '%s:%d' % (config.get('app.kafka.host'), config.get('app.kafka.port'))
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             client_id=client,
                             compression_type='gzip',
                             bootstrap_servers=kafka_server,
                             retries=3,
                             **kwargs)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                logger.info('Send data to kafka by producer[%s]' % client)
                rtn = func(*args, **kwargs)
                producer.send(topic, rtn, **kwargs)
                return rtn
            except Exception as e:
                logger.error('Err when send data to kafka')
                logger.error(e)

        return wrapper

    return decorator
