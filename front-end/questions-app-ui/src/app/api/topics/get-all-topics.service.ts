import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { catchError, Observable, throwError } from 'rxjs';

export interface Topic {
  topic_id: string,
  topic_name: string,
  description: string,
  category: string
}

export interface TopicResponse {
  topics: Topic[];
  last_evaluated_key: LastEvaluatedKey;
  has_more: boolean;
}

export interface LastEvaluatedKey{
  topic_id: string,
  user_id: string
}

@Injectable({
  providedIn: 'root'
})
export class GetAllTopicsService {
  private apiUrl = `${environment.apiUrl}/topics/all`;


  constructor(private http: HttpClient) { }

  getTopics(limit: number, topic_id: string, user_id: string, has_more: boolean): Observable<TopicResponse>{
    let httpParams = new HttpParams().set('limit', limit.toString());
    
    if (has_more){
      httpParams = httpParams.set('topic_id', topic_id);
      httpParams = httpParams.set('user_id', user_id);
    }

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
