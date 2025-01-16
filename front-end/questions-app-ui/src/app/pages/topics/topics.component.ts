import { Component } from '@angular/core';
import { GetAllTopicsService, Topic, TopicResponse } from '../../api/topics/get-all-topics.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-topics',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topics.component.html',
  styleUrl: './topics.component.css'
})
export class TopicsComponent {

  topics: Topic[] = [];
  lastEvaluatedKey: string = '';

  constructor(private topicService: GetAllTopicsService){}

  ngOnInit() {
    this.loadTopics();
  }

  loadTopics(){
    this.topicService.getTopics(20).subscribe({
      next: (response: TopicResponse) => {
        this.topics = response.topics;
        this.lastEvaluatedKey = response.last_evaluated_key;
        console.log(this.topics);
      },
      error: (error) => {
        console.log('Error')
      }
    })
  }

}
