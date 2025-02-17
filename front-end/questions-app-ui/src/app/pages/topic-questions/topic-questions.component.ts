import { CommonModule } from '@angular/common';
import { Component, OnInit, signal } from '@angular/core';
import { GetOneTopicService, TopicResponse } from '../../api/topics/get-one-topic.service';
import { ActivatedRoute } from '@angular/router';
import { AuthTopicService } from '../../api/topics/auth-topic.service';
import { Modal } from 'flowbite';
import { AddTopicComponent } from '../../component/add-topic/add-topic.component';

@Component({
  selector: 'app-topic-questions',
  standalone: true,
  imports: [CommonModule, AddTopicComponent],
  templateUrl: './topic-questions.component.html',
  styleUrl: './topic-questions.component.css'
})
export class TopicQuestionsComponent implements OnInit {
  is_topic_owner = false
  loading = true;
  private modalAdd: Modal | undefined;
  topic: TopicResponse = {'topic_id':'','topic_name':'','description':''}

  constructor(private topicService: GetOneTopicService, private route: ActivatedRoute, private topicAuth: AuthTopicService){}

  ngOnInit(){
    this.route.params.subscribe(async params => {
      this.loadTopic(params['topic'])
      this.is_topic_owner = await this.topicAuth.checkTopicOwner(params['topic'])
      this.loading = false;
    });
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

  loadTopic(topic_id: string){
    this.topicService.getTopic(topic_id).subscribe({
      next: (response: TopicResponse) => {
        this.topic = response;
        console.log(this.topic)

      },
      error: (error) => {
        console.log(error)
      }
    })
  }

}
