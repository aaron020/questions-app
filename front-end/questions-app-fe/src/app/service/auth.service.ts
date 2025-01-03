import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { signIn, fetchAuthSession } from 'aws-amplify/auth';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authenticationSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.authenticationSubject.asObservable();

  constructor() {
    this.checkInitialAuthState();
  }

  async signIn(username: string, password: string) {
    try {
      const signInResult = await signIn({
        username,
        password,
        options: { preventSignOut: false }
      });

      if (signInResult.isSignedIn) {
        const session = await fetchAuthSession();
        console.log('Sign in successful');
       // console.log('Access Token:', session.tokens?.idToken?.toString());
        
        this.authenticationSubject.next(true);
        return { success: true };
      }

      return { success: false, error: 'Sign-in failed' };

    } catch (error: unknown) {  // Explicitly type the error as unknown
      // Type guard to check if error is an object with a name property
      if (error && typeof error === 'object' && 'name' in error) {
        const authError = error as { name: string };
        console.log(authError.name)
        return { 
          success: false, 
          error: authError.name === 'NotAuthorizedException' ? 
            'Incorrect username or password' : 
            'An error occurred during sign-in'
        };
      }
      
      // If error doesn't match our expected structure, return a generic message
      console.error('Sign-in error:', error);
      return { 
        success: false, 
        error: 'An unexpected error occurred' 
      };
    }
  }

  private async checkInitialAuthState() {
    try {
      const session = await fetchAuthSession();
      this.authenticationSubject.next(session.tokens !== undefined);
    } catch {
      this.authenticationSubject.next(false);
    }
  }
}