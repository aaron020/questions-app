import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { AuthService } from '../../service/auth.service';
import { QuestionHiddenCorrect } from '../../models/question';
import { catchError, map, throwError } from 'rxjs';

export interface StartTopicResponse{
  topic_test_id: string,
  data: QuestionHiddenCorrect[]
}


@Injectable({
  providedIn: 'root'
})
export class StartTopicTestService {
  private apiUrl = `${environment.apiUrl}/topic_test/start`;

  constructor(private http: HttpClient, private authService: AuthService) { }

  async startTopicTest(topic_id: string){
    const httpParams = new HttpParams().set('topic_id', topic_id);
    const headers = await this.authService.getAuthHeaders();

    return this.http.post<StartTopicResponse>(this.apiUrl, {}, {headers, params: httpParams})
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
