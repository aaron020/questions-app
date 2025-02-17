import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpErrorResponse, HttpHeaders, HttpParams } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';
import { catchError, map, throwError } from 'rxjs';



export interface QuestionResponse {
  topic_id: string;
  question_id: string;
  questions: string;
  answers: Answer[];
  explanation: string;
  difficulty: number;
}

export interface Answer {
  answer: string,
  correct: boolean
}

@Injectable({
  providedIn: 'root'
})
export class GetQuestionsService {
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

  async getQuestions(topic_id: string){
    const httpParams = new HttpParams().set('topic_id', topic_id);
    const headers = await this.getAuthHeaders();

    return this.http.get<QuestionResponse[]>(this.apiUrl, {headers, params: httpParams})
    .pipe(
        map(response => response || []), 
        catchError(this.handleError)
    )

  }

  private handleError(error: HttpErrorResponse) {
    let errorMessage = 'An error occurred';

    if (error.error instanceof ErrorEvent) {
      errorMessage = `Error: ${error.error.message}`;
    } else {
      errorMessage = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }

    console.error(errorMessage);
    return throwError(() => new Error(errorMessage));
  }


}
