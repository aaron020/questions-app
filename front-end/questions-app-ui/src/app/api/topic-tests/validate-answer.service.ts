import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { AuthService } from '../../service/auth.service';
import { QuestionWithCorrect } from '../../models/question';
import { catchError, map, throwError } from 'rxjs';


export interface ValidateAnswerResponse {
  correct: boolean,
  data: QuestionWithCorrect
}

@Injectable({
  providedIn: 'root'
})
export class ValidateAnswerService {
  private apiUrl = `${environment.apiUrl}/topic_test/validate/answer`;

  constructor(private http: HttpClient, private authService: AuthService) { }

  async validateAnswer(topic_test_id: string, question_id: string, answer_id: string){
    const payload = {
      'topic_test_id': topic_test_id,
      'question_id': question_id,
      'answer_id': answer_id
    }
    const headers = await this.authService.getAuthHeaders();
    return this.http.post<ValidateAnswerResponse>(this.apiUrl, payload, {headers})
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
