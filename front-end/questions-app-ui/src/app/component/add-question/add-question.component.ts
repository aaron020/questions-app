import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AddQuestionService } from '../../api/questions/add-question.service';
import { ToastrService } from 'ngx-toastr';
import { Modal } from 'flowbite';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-add-question',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './add-question.component.html',
  styleUrl: './add-question.component.css'
})
export class AddQuestionComponent {
  form: FormGroup;
  private modal: Modal | undefined;
  questionNumber = 2
  @Input() topic_id: string = '';

  @Output() toggleModalOutput = new EventEmitter<any>();
  @Output() loadQuestionsOutput = new EventEmitter<any>();

  constructor(private fb: FormBuilder, 
      private addQuestionService: AddQuestionService, private toastr: ToastrService){
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

  toggleModal(){
    this.defualtValues()
    this.toggleModalOutput.emit()
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

  defualtValues(){
    this.questionNumber = 2
    this.form.patchValue({
      question: '',
      answer_one: '',
      answer_two: '',
      answer_three: '',
      answer_four: '',
      answer_five: '',
      correctGroup: 'one',
      explanation: '',
      difficulty: '1'
    })
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
        const request = await this.addQuestionService.addQuestion(this.form.value, this.topic_id);
        request.subscribe({
          next: (response) => {
            console.log('Question created successfully')
            this.toggleModal()
            this.loadQuestionsOutput.emit()
            this.toastr.success('Question Added', 'Successfully added new question!')
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
