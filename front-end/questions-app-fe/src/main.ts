import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { Amplify } from 'aws-amplify';
import { SsmService } from './app/service/ssm.service';
import { environment } from './environment';

Amplify.configure({
  Auth: {
    Cognito: {
      userPoolId: environment.userPoolId,
      userPoolClientId: environment.clientId
    }
  }
})

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));


