import { Component, Input } from '@angular/core';
import { TopicTestResultResponse } from '../../api/topic-tests/topic-test-result.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-topic-test-result',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topic-test-result.component.html',
  styleUrl: './topic-test-result.component.css'
})
export class TopicTestResultComponent {
  @Input() topic_test_result: TopicTestResultResponse = {total: 0, score: 0, unanswered_questions: [], answered_correct: [], answered_incorrect: []}

}
