import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';
import { Observable } from 'rxjs';


interface QuestionForm {
  question: string;
  answer_a: string;
  answer_b: string;
  answer_c: string;
  answer_d: string;
  answer_a_correct: boolean;
  answer_b_correct: boolean;
  answer_c_correct: boolean;
  answer_d_correct: boolean;
  explanation: string;
  difficulty: string;
}

interface QuestionPayload {
  topic_id: string;
  questions: string;
  answers: Answer[];
  explanation: string;
  difficulty: number;
}

interface Answer {
  [key: string]: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class AddQuestionService {
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
  
  private transformFormData(topic_id: string, formData: QuestionForm): QuestionPayload {
    const answers: Answer[] = [
      { [formData.answer_a]: formData.answer_a_correct },
      { [formData.answer_b]: formData.answer_b_correct },
      { [formData.answer_c]: formData.answer_c_correct },
      { [formData.answer_d]: formData.answer_d_correct }
    ];

    return {
      topic_id: topic_id,
      questions: formData.question,
      answers,
      explanation: formData.explanation,
      difficulty: +formData.difficulty
    };
  }

  async addQuestion(formData: QuestionForm): Promise<Observable<any>>{
    const headers = await this.getAuthHeaders();
    const payload = this.transformFormData('123',formData);
    console.log(payload)
    return this.http.post<any>(this.apiUrl, payload, { headers });
  }
}
