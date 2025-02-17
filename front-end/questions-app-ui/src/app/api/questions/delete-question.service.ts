import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';

@Injectable({
  providedIn: 'root'
})
export class DeleteQuestionService {
  private apiUrl = `${environment.apiUrl}/topics/questions`;

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

  async deleteQuestion(question_id: string, topic_id: string){
    const httpParams = new HttpParams().set('topic_id', topic_id)
                                       .set('question_id',question_id)
    const headers = await this.getAuthHeaders();
    return this.http.delete<any>(this.apiUrl, { headers , params: httpParams});
  }
}
