import { Component } from '@angular/core';
import { GetAllTopicsService, Topic, TopicResponse } from '../../api/topics/get-all-topics.service';
import { CommonModule } from '@angular/common';
import { AddTopicComponent } from '../../component/add-topic/add-topic.component';
import { Modal } from 'flowbite';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-topics',
  standalone: true,
  imports: [CommonModule, AddTopicComponent],
  templateUrl: './topics.component.html',
  styleUrl: './topics.component.css'
})
export class TopicsComponent {
  loading = true
  private modalAdd: Modal | undefined;

  topics: Topic[] = [];
  lastEvaluatedKey: string = '';

  constructor(private topicService: GetAllTopicsService, public authService: AuthService){}

  ngOnInit() {
    this.loadTopics();
    const modalElement = document.getElementById('topic-modal');
    if (modalElement) {
      const modal = new Modal(modalElement);
      this.modalAdd = modal;
    }
  }

  toggleModalAdd() {
    if (this.modalAdd) {
      this.modalAdd.toggle();
    }
  }

  loadTopics(){
    this.topicService.getTopics(20).subscribe({
      next: (response: TopicResponse) => {
        this.topics = response.topics;
        this.lastEvaluatedKey = response.last_evaluated_key;
        this.loading = false
      },
      error: (error) => {
        console.log('Error')
      }
    })
  }

}
