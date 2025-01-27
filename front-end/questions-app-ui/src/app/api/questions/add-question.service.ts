import { Injectable } from '@angular/core';
import { environment } from '../../../environment';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { fetchAuthSession } from 'aws-amplify/auth';
import { Observable } from 'rxjs';


interface QuestionForm {
  question: string;
  answer_one: string;
  answer_two: string;
  answer_three: string;
  answer_four: string;
  answer_five: string;
  correctGroup: string;
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
      { [formData.answer_one]: formData.correctGroup === 'one'  },
      { [formData.answer_two]: formData.correctGroup === 'two' },
    ];

    if (formData.answer_three !== '') {
      answers.push({ [formData.answer_three]: formData.correctGroup === 'three' });
    }

    if (formData.answer_four !== '') {
      answers.push({ [formData.answer_four]: formData.correctGroup === 'four' });
    }

    if (formData.answer_five !== '') {
      answers.push({ [formData.answer_five]: formData.correctGroup === 'five' });
    }

    return {
      topic_id: topic_id,
      questions: formData.question,
      answers,
      explanation: formData.explanation,
      difficulty: +formData.difficulty
    };
  }

  async addQuestion(formData: QuestionForm, topic_id: string): Promise<Observable<any>>{
    const headers = await this.getAuthHeaders();
    const payload = this.transformFormData(topic_id,formData);
    console.log(payload)
    return this.http.post<any>(this.apiUrl, payload, { headers });
  }
}
