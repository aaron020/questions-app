import { secret } from '@aws-amplify/backend';

export const awsconfig = {
    Auth: {
        Cognito: {
            userPoolId: secret('COGNITO_CLIENT_ID'),
            userPoolClientId: secret('COGNITO_USER_POOL_ID')
        }
    }
};