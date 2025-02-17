



def lambda_handler(event, context):
    event['response'] = {
        'autoConfirmUser': True,
        'autoVerifyEmail': True,
    }

    return event
