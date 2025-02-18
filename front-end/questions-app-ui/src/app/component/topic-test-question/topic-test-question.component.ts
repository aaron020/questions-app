import { Component, EventEmitter, Input, Output } from '@angular/core';
import { StartTopicResponse } from '../../api/topic-tests/start-topic-test.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-topic-test-question',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './topic-test-question.component.html',
  styleUrl: './topic-test-question.component.css'
})
export class TopicTestQuestionComponent {
  questionNumber = 1
  selectedAnswer: string = '';
  nextQuestion: boolean = false;
  @Output() submitAnswerEmitter = new EventEmitter<any>();
  @Output() nextQuestionEmitter = new EventEmitter<any>();

  @Input() topic_test: StartTopicResponse = {topic_test_id: '', data: []};

  submitAnswer(){
    this.submitAnswerEmitter.emit({
      answer_id : this.selectedAnswer,
      question_id : this.topic_test.data[this.questionNumber].question_id,
      topic_test_id: this.topic_test.topic_test_id
    })
    this.nextQuestion = true
  }

  onNextQuestion(){
    this.nextQuestionEmitter.emit()
    this.selectedAnswer = ''
    this.nextQuestion = false
    this.questionNumber = this.questionNumber + 1
  }

}
