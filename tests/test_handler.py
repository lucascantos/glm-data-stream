import pytest
import json
from handler import glm_data

def test_glm_data():
    event = {
        'debug': True,
        'path': 'tests/sample/OR_GLM-L2-LCFA_G16_s20211041500000_e20211041500204_c20211041500226.nc'
        OR_ABI-L2-ACHTM2-M6_G16_s20211101801533_e20211101801590
        ABI-L2-ACHTM
    }
    event = {'Records': [{'EventSource': 'aws:sns', 'EventVersion': '1.0', 'EventSubscriptionArn': 'arn:aws:sns:us-east-1:123901341784:NewGOES16Object:0b8748d1-d256-49f2-a501-00e17f9dddd4', 'Sns': {'Type': 'Notification', 'MessageId': 'ff0bd2d4-49ae-5935-8af4-8a2d50350e53', 'TopicArn': 'arn:aws:sns:us-east-1:123901341784:NewGOES16Object', 'Subject': 'Amazon S3 Notification', 'Message': '{"Records":[{"eventVersion":"2.1","eventSource":"aws:s3","awsRegion":"us-east-1","eventTime":"2021-04-20T18:03:00.714Z","eventName":"ObjectCreated:Put","userIdentity":{"principalId":"AWS:AIDAJIC4U5R2TXT7T3MI6"},"requestParameters":{"sourceIPAddress":"198.85.226.62"},"responseElements":{"x-amz-request-id":"XV14618T1FZDPY3D","x-amz-id-2":"EUciy1XBvAEah2navLEAWLnPwJMkP7Fkys+8qEJItcSP7gGSnFlXIYmDHpAPuZhdjPjs+Q1KJZR/Nxa8Y5/9Z6tKDSyb6S0f"},"s3":{"s3SchemaVersion":"1.0","configurationId":"NewObject","bucket":{"name":"noaa-goes16","ownerIdentity":{"principalId":"A2AJV00K47QOI1"},"arn":"arn:aws:s3:::noaa-goes16"},"object":{"key":"ABI-L2-ACHTM/2021/110/18/OR_ABI-L2-ACHTM2-M6_G16_s20211101801533_e20211101801590_c20211101802501.nc","size":471471,"eTag":"ee1bb8bbdbd0ea4544282d8ecfe3846e","sequencer":"00607F175A407642AD"}}}]}', 'Timestamp': '2021-04-20T18:03:07.973Z', 'SignatureVersion': '1', 'Signature': 'n/Rj3JAZ2rXOJx9NgnKDP2Caz/Xb9jpj8jDBZlmh79QyPYNwObmY7PVyCt2NfpMD+uwVXN6FCqAYTpRiq9vlySabZyzajDRQXRpf1Vf+IAX3PtFfLiEG1RY/FYpGyVK6Fn/ZA41Y3sfBtwq1pvq7Q4C8DHFUp9ysZHO6yToUbsmU19GNk9PUkCCJPS5aJ4sOnCks76jPxW++MtE/0TNd84j2NdMmM5e7TZeRONCg0WCPxUiAcIyex8BoR0en+OK0EVUImh8XXCoNiIjhS5biR0PZEoXzfbuTOgtOJma3Pdr/b5xkRayKPD3Fuba+o6muO8tyymAxzdvvAbZNv7lvkA==', 'SigningCertUrl': 'https://sns.us-east-1.amazonaws.com/SimpleNotificationService-010a507c1833636cd94bdb98bd93083a.pem', 'UnsubscribeUrl': 'https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:123901341784:NewGOES16Object:0b8748d1-d256-49f2-a501-00e17f9dddd4', 'MessageAttributes': {}}}]}
    message = json.loads(event['Records'][0]['Sns']['Message'])
    print(message['Records'][0]['s3']['object']['key'])
    # response = json.loads(glm_data(event))
    # assert response['lightnings'] == []

