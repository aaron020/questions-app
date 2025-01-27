import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthTopicService {
    private apiUrl = `${environment.apiUrl}/topics/auth`;

  constructor(private http: HttpClient) { }


  async checkTopicOwner(topic_id: string): Promise<boolean>{
    try{
      const httpParams = new HttpParams().set('topic_id', topic_id);
      const headers = await this.getAuthHeaders();
      const response = await firstValueFrom(
        this.http.get<any>(this.apiUrl, 
          {
            headers,
            params: httpParams,
            observe: 'response'
          }
        )
      )

      return response?.status === 200
    }
    catch(error){
      console.log(error)
      return false
    }
  }


  private async getAuthHeaders(): Promise<HttpHeaders> {
    try {
      const session = await fetchAuthSession();
      const idToken = session.tokens?.idToken?.toString();
      return new HttpHeaders().set('Authorization', `Bearer ${idToken}`);
    } catch (error) {
      console.error('Error getting auth token:', error);
      throw error;
    }
  }
}
