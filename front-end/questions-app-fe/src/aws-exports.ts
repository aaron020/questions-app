import { secret } from '@aws-amplify/backend';

export const awsconfig = {
    Auth: {
        Cognito: {
            userPoolId: String(secret('COGNITO_CLIENT_ID')),
            userPoolClientId: String(secret('COGNITO_USER_POOL_ID'))
        }
    }
};