import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { Amplify } from 'aws-amplify';
import { SsmService } from './app/service/ssm.service';

async function initializeApp() {
  const ssmService = new SsmService();

  try{
    const userPoolIdParam = await ssmService.getParameter('COGNITO_USER_POOL_ID');
    const clientIdParam = await ssmService.getParameter('COGNITO_CLIENT_ID');

    console.log(userPoolIdParam)
    console.log(clientIdParam)

    Amplify.configure({
      Auth: {
        Cognito: {
          userPoolId: userPoolIdParam,
          userPoolClientId: clientIdParam
        }
      }
    })

    bootstrapApplication(AppComponent, appConfig)
      .catch((err) => console.error(err));

  }catch(err){
    console.error('Failed to initialize application:', err);
  }
  
}

initializeApp();


