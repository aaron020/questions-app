import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { signIn, fetchAuthSession, signOut, signUp} from 'aws-amplify/auth';
import { HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private authenticationSubject = new BehaviorSubject<boolean>(false);
  public isAuthenticated$ = this.authenticationSubject.asObservable();

  constructor() {
    this.checkInitialAuthState();
  }

  public async getAuthHeaders(): Promise<HttpHeaders> {
    try {
      const session = await fetchAuthSession();
      const idToken = session.tokens?.idToken?.toString();
      return new HttpHeaders().set('Authorization', `Bearer ${idToken}`);
    } catch (error) {
      console.error('Error getting auth token:', error);
      throw error;
    }
  }

  async signUp(email: string, username: string, password: string){
    try{
      const result = await signUp({
        username,
        password,
        options:{
          userAttributes:{
            email
          }
        }
      })

      if(result.isSignUpComplete){
        console.log('New user created')
        return { success: true };
      }else{
        console.log(result)
        return { success: false, error: 'Sign-up failed' };
      }
    }catch(error){
      console.log(error)
      return { success: false, error: 'Sign-up failed' };
    }
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

  async signOut(): Promise<{ success: boolean; error?: string }> {
    try {
      await signOut();
      this.authenticationSubject.next(false);
      return { success: true };
    } catch (error) {
      console.error('Logout error:', error);
      return {
        success: false,
        error: 'Failed to logout. Please try again.'
      };
    }
  }

  public async checkInitialAuthState() {
    try {
      const session = await fetchAuthSession();
      this.authenticationSubject.next(session.tokens !== undefined);
    } catch {
      this.authenticationSubject.next(false);
    }
  }
}