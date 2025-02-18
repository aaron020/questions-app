import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { ValidateAnswerResponse } from '../../api/topic-tests/validate-answer.service';
import { AnswerWithCorrect, QuestionWithCorrect } from '../../models/question';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-topic-test-explain',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topic-test-explain.component.html',
  styleUrl: './topic-test-explain.component.css'
})
export class TopicTestExplainComponent implements OnChanges {
  @Input() validate_answer: ValidateAnswerResponse = {correct: false, data: {} as QuestionWithCorrect};
  correctAnswer: string = ''


  ngOnChanges(changes: SimpleChanges) {
    console.log('Checking Correct')
    console.log(this.validate_answer)
    if (changes['validate_answer'] && changes['validate_answer'].currentValue) {
      this.correctAnswer = this.determineCorrect();
    }
  }

  determineCorrect(): string{
    for (const val of this.validate_answer.data.answers){
      if (val.correct){
        return val.answer
      }
    }
    return ''
  }


}
