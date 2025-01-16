import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { environment } from './environment';
import { Amplify } from 'aws-amplify';
import { provideToastr } from 'ngx-toastr';
import { provideAnimations } from '@angular/platform-browser/animations';


Amplify.configure({
  Auth: {
    Cognito: {
      userPoolId: environment.userPoolId,
      userPoolClientId: environment.clientId
    }
  }
})

bootstrapApplication(AppComponent, {
  ...appConfig,
  providers: [
    ...(appConfig.providers || []),
    provideHttpClient(),
    provideToastr(),
    provideAnimations(),
  ],
})
  .catch((err) => console.error(err));
