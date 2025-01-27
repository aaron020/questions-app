import { CommonModule } from '@angular/common';
import { Component, OnInit, signal } from '@angular/core';
import { GetOneTopicService, TopicResponse } from '../../api/topics/get-one-topic.service';
import { ActivatedRoute } from '@angular/router';
import { AuthTopicService } from '../../api/topics/auth-topic.service';

@Component({
  selector: 'app-topic-questions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topic-questions.component.html',
  styleUrl: './topic-questions.component.css'
})
export class TopicQuestionsComponent implements OnInit {
  is_topic_owner = false
  topic: TopicResponse = {'topic_id':'','topic_name':'','description':''}

  constructor(private topicService: GetOneTopicService, private route: ActivatedRoute, private topicAuth: AuthTopicService){}

  ngOnInit(){
    this.route.params.subscribe(async params => {
      this.loadTopic(params['topic'])
      this.is_topic_owner = await this.topicAuth.checkTopicOwner(params['topic'])
    });
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
