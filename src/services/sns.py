import boto3
import os
from src.configs.configs import LIGHTNING_SNS

class SNS:
    def __init__(self, topic=LIGHTNING_SNS):
        '''
        Handler of SNS events and methods
        '''
        self.region = 'us-east-1'
        self.acc_id = '999740264686'
        self._topic = topic

    def set_topic(self, topic):
        self._topic = topic
    def get_topic(self):
        return f'arn:aws:sns:{self.region}:{self.acc_id}:{self._topic}'
    topic = property(get_topic, set_topic)

    def send(self, msg, attr=None, subject=None):
            '''
            Sends message to SNS Topic
            :parmas msg: message to be send
            :parmas attr: Atributes
            :parmas subject: Subject of message also used as filter
            '''
            sns = boto3.client('sns', region_name=self.region)
            kwargs = {
                'TopicArn': self.topic,
                'Message': msg
            }
            if attr is not None:
                kwargs['MessageAttributes'] = {
                    "action": {
                        "DataType": "String",
                        "StringValue": attr
                    }
                }
            if subject is not None:
                kwargs['Subject'] = subject
            sns.publish(**kwargs)
