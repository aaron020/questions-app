import { bootstrapApplication, provideClientHydration } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { Amplify } from 'aws-amplify';
import { SsmService } from './app/service/ssm.service';
import { environment } from './environment';
import { provideHttpClient } from '@angular/common/http';
import { BrowserAnimationsModule, provideAnimations } from '@angular/platform-browser/animations';
import { provideToastr, ToastrModule } from 'ngx-toastr';

Amplify.configure({
  Auth: {
    Cognito: {
      userPoolId: environment.userPoolId,
      userPoolClientId: environment.clientId
    }
  }
})

// bootstrapApplication(AppComponent, appConfig)
//   .catch((err) => console.error(err));

bootstrapApplication(AppComponent, {
  ...appConfig,
  providers: [
    ...(appConfig.providers || []),
    provideClientHydration(),
    provideHttpClient(),
    provideAnimations(),
    provideToastr()
  ],
})
  .catch((err) => console.error(err));


