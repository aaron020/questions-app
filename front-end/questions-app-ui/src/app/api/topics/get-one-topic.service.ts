import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpErrorResponse, HttpParams } from '@angular/common/http';
import { catchError, throwError } from 'rxjs';


export interface TopicResponse {
  topic_id: string,
  topic_name: string,
  category: string,
  description: string
}

@Injectable({
  providedIn: 'root'
})
export class GetOneTopicService {
  private apiUrl = `${environment.apiUrl}/topics`;

  constructor(private http: HttpClient) { }

  getTopic(topic_id: string){
    const httpParams = new HttpParams().set('topic_id', topic_id);

    return this.http.get<TopicResponse>(this.apiUrl,  { params: httpParams })
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
