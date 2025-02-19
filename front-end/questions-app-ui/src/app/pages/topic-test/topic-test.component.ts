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
import { TopicTestResultComponent } from "../../component/topic-test-result/topic-test-result.component";
import { TopicTestResultResponse, TopicTestResultService } from '../../api/topic-tests/topic-test-result.service';

@Component({
  selector: 'app-topic-test',
  standalone: true,
  imports: [TopicTestQuestionComponent, TopicTestExplainComponent, CommonModule, TopicTestResultComponent],
  templateUrl: './topic-test.component.html',
  styleUrl: './topic-test.component.css'
})
export class TopicTestComponent implements OnInit {
  topic_test: StartTopicResponse = {topic_test_id: '', data: []} 
  valid_answer: ValidateAnswerResponse = {  correct: false, data: {} as QuestionWithCorrect}
  topic_test_result: TopicTestResultResponse = {total: 0, score: 0, unanswered_questions: [], answered_correct: [], answered_incorrect: []}
  showExplanation: boolean = false;
  showQuestions: boolean = true;
  showResults: boolean = false;
  noQuestionsFound: boolean = false;

  constructor(private route: ActivatedRoute, private startTopicTestSevice: StartTopicTestService, private validateAnswerService: ValidateAnswerService,
    private topicTestResultService: TopicTestResultService
  ){}


  ngOnInit(){
    this.route.params.subscribe(async params => {
      this.startTopicTest(params['topic'])
    });
  }


  async startTopicTest(topic_id: string){
    try{
      const topicTestObservable = await this.startTopicTestSevice.startTopicTest(topic_id)
      const value = await firstValueFrom(topicTestObservable)
      if (Array.isArray(value) && value.length === 0){
        this.showQuestions = false
        this.noQuestionsFound = true
      }else{
        this.topic_test = value
      }
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

  async finishTest(){
    try{
      const topicTestResultObservble = await this.topicTestResultService.getResult(this.topic_test.topic_test_id)
      this.topic_test_result = await firstValueFrom(topicTestResultObservble)
      this.showExplanation = false
      this.showQuestions = false
      this.showResults = true
    }catch (error) {
      console.error('Error:', error);
    }
  }

}
