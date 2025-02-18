import { Component, OnInit } from '@angular/core';
import { TopicTestQuestionComponent } from '../../component/topic-test-question/topic-test-question.component';
import { TopicQuestionModifyComponent } from "../topic-question-modify/topic-question-modify.component";
import { ActivatedRoute } from '@angular/router';
import { StartTopicResponse, StartTopicTestService } from '../../api/topic-tests/start-topic-test.service';
import { firstValueFrom } from 'rxjs';
import { ValidateAnswerResponse, ValidateAnswerService } from '../../api/topic-tests/validate-answer.service';
import { QuestionWithCorrect } from '../../models/question';
import { TopicTestExplainComponent } from "../../component/topic-test-explain/topic-test-explain.component";
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-topic-test',
  standalone: true,
  imports: [TopicTestQuestionComponent, TopicTestExplainComponent, CommonModule],
  templateUrl: './topic-test.component.html',
  styleUrl: './topic-test.component.css'
})
export class TopicTestComponent implements OnInit {
  topic_test: StartTopicResponse = {topic_test_id: '', data: []}
  valid_answer: ValidateAnswerResponse = {  correct: false, data: {} as QuestionWithCorrect}
  showExplanation: boolean = false;

  constructor(private route: ActivatedRoute, private startTopicTestSevice: StartTopicTestService, private validateAnswerService: ValidateAnswerService){}


  ngOnInit(){
    this.route.params.subscribe(async params => {
      this.startTopicTest(params['topic'])
    });
  }


  async startTopicTest(topic_id: string){
    try{
      const topicTestObservable = await this.startTopicTestSevice.startTopicTest(topic_id)
      this.topic_test = await firstValueFrom(topicTestObservable)
      console.log(this.topic_test)
    }catch (error) {
      console.error('Error:', error);
    }
  }


  async validateAnswer(data: any){
    try{
      const validateAnswerObservable = await this.validateAnswerService.validateAnswer(data.topic_test_id, data.question_id, data.answer_id)
      this.valid_answer = await firstValueFrom(validateAnswerObservable)
      console.log(this.valid_answer)
      this.showExplanation = true
    }catch (error) {
      console.error('Error:', error);
    }
  }

  nextQuestion(){
    this.showExplanation = false
  }

}
