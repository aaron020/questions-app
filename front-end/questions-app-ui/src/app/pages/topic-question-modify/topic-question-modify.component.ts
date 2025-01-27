import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Modal } from 'flowbite';
import { GetQuestionsService, QuestionResponse } from '../../api/questions/get-questions.service';
import { firstValueFrom } from 'rxjs';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { AddQuestionService } from '../../api/questions/add-question.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-topic-question-modify',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './topic-question-modify.component.html',
  styleUrl: './topic-question-modify.component.css'
})
export class TopicQuestionModifyComponent implements OnInit {
  private modal: Modal | undefined;
  questions: QuestionResponse[] = []
  questionNumber = 2
  form: FormGroup;
  private topic_id = ''

  constructor(private route: ActivatedRoute, private questionService: GetQuestionsService, private fb: FormBuilder, 
    private addQuestionService: AddQuestionService, private toastr: ToastrService){
    // this.form = this.fb.group({
    //   question: ['', [Validators.required, Validators.max(200)]],
    //   answer_one: ['', [Validators.required, Validators.max(200)]],
    //   answer_two: ['', [Validators.required, Validators.max(200)]],
    //   answer_three: ['', [Validators.max(200)]],
    //   answer_four: ['', [Validators.max(200)]],
    //   answer_five: ['', [Validators.max(200)]],
    //   correctGroup: ['one'],
    //   explanation: ['', [Validators.required, Validators.max(200)]],
    //   difficulty: ['defualt', [Validators.required, Validators.pattern('^(?!default$).*$')]]
    // });
    this.form = this.fb.group({
      question: ['', [Validators.required, Validators.maxLength(200)]],
      answer_one: ['', [Validators.required, Validators.maxLength(200)]],
      answer_two: ['', [Validators.required, Validators.maxLength(200)]],
      answer_three: [''],
      answer_four: [''],
      answer_five: [''],
      correctGroup: ['one'],
      explanation: ['', [Validators.required, Validators.maxLength(200)]],
      difficulty: ['1']
    });
  }

  defaultAnswers() {
    this.form.patchValue({
      answer_one: '',
      answer_two: '',
      answer_three: '',
      answer_four: '',
      answer_five: '',
      correctGroup: 'one' 
    });
  }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.loadQuestions(params['topic'])
      this.topic_id = params['topic']
    });
    const modalElement = document.getElementById('question-modal');
    if (modalElement) {
      const modal = new Modal(modalElement);
      this.modal = modal;
    }
  }

  async loadQuestions(topic_id: string){
    try{
      const questionsObservable = await this.questionService.getQuestions(topic_id);
      this.questions = await firstValueFrom(questionsObservable);
      console.log(this.questions)
    }catch (error) {
      console.error('Error:', error);
    }
  }

  toggleModal() {
    if (this.modal) {
      this.modal.toggle();
    }
  }

  updateQuestionNumber(event: any){
    this.questionNumber = event.target.value;
    this.defaultAnswers()
    console.log(this.questionNumber)
  }

  async onAddQuestion() {
    console.log(this.form.value); 
    if (this.form.valid) {
      console.log('valid and sending'); 
      try{
        const request = await this.addQuestionService.addQuestion(this.form.value,this.topic_id);
        request.subscribe({
          next: (response) => {
            console.log('Question created successfully')
            this.toastr.success('Question Added', 'Successfully added new question!')
            this.loadQuestions(this.topic_id)
            this.toggleModal()
          },
          error: (error) => console.error('Error creating question:', error)
        });
      }catch (error) {
        console.error('Authentication error:', error);
      }
    }else{
      this.toastr.warning('Please ensure all fields are filled out!','Oops!', {
        closeButton: true
      })
    }
  }

}
