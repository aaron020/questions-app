import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { catchError, Observable, throwError } from 'rxjs';

export interface Topic {
  topic_id: string,
  topic_name: string,
  description: string
}

export interface TopicResponse {
  topics: Topic[];
  last_evaluated_key: string;
}

@Injectable({
  providedIn: 'root'
})
export class GetAllTopicsService {
  private apiUrl = `${environment.apiUrl}/topics`;


  constructor(private http: HttpClient) { }

  getTopics(limit: number): Observable<TopicResponse>{
    const httpParams = new HttpParams().set('limit', limit.toString());

    return this.http.get<TopicResponse>(this.apiUrl, { params: httpParams })
    .pipe(
      catchError(this.handleError)
    );
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
