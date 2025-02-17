import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';
import { Observable } from 'rxjs';

interface TopicPayload {
  topic_name: string;
  description: string;
  category: number;
}


@Injectable({
  providedIn: 'root'
})
export class AddTopicService {
  private apiUrl = `${environment.apiUrl}/topics`;

  constructor(private http: HttpClient) { }

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


  async addTopic(topicData: TopicPayload) : Promise<Observable<any>>{
    const headers = await this.getAuthHeaders();
    console.log(topicData)
    return this.http.post<any>(this.apiUrl, topicData, { headers });
  }
}
