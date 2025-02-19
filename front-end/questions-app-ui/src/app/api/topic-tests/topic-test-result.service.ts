import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { AuthService } from '../../service/auth.service';
import { catchError, map, throwError } from 'rxjs';

export interface TopicTestResultResponse{
  total: number;
  score: number;
  unanswered_questions: string[];
  answered_correct: string[];
  answered_incorrect: string[];
}


@Injectable({
  providedIn: 'root'
})
export class TopicTestResultService {
  private apiUrl = `${environment.apiUrl}/topic_test/result`;

  constructor(private http: HttpClient, private authService: AuthService) { }

  async getResult(topic_test_id: string){
    const headers = await this.authService.getAuthHeaders();
    const httpParams = new HttpParams().set('topic_test_id', topic_test_id);

    return this.http.get<TopicTestResultResponse>(this.apiUrl, {headers, params: httpParams})
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
