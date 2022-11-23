import json

def lambda_handler(event, context):
    
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiYXBpX2ZpbGVfbWFuYWdlciJ9.FucuBV_EJ3If6pH6KBNnQrHf0fERLskdrGNPSTXnKu4'
     # 1 - Log the event
    print('*********** The event is: ***************')
    print(event)
    # 2 - See if the person's token is valid
    if event['authorizationToken'] == token:
        auth = 'Allow'
    else:
        auth = 'Deny'
    # 3 - Construct and return the response
    reponse = {
        "principalId": "abc123",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [{
                "Action": "execute-api:Invoke",
                "Resource": ["arn:aws:execute-api:us-east-2:946387485379:xoecj8rqah/*/*/*"],
                "Effect": auth
            }]
        }
    }
    return reponse
