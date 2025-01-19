import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { GetOneTopicService, TopicResponse } from '../../api/topics/get-one-topic.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-topic-questions',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './topic-questions.component.html',
  styleUrl: './topic-questions.component.css'
})
export class TopicQuestionsComponent implements OnInit {
  topic: TopicResponse = {'topic_id':'','topic_name':'','description':''}

  constructor(private topicService: GetOneTopicService, private route: ActivatedRoute,){}

  ngOnInit(){
    this.route.params.subscribe(params => {
      this.loadTopic(params['topic'])
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
