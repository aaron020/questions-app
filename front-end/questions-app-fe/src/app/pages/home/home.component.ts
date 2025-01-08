import { Component } from '@angular/core';
import { GetAllTopicsService, Topic, TopicResponse } from '../../service/api/topics/get-all-topics.service';
import { error } from 'console';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
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
