import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { AddQuestionService } from '../../api/questions/add-question.service';
import { ToastrService } from 'ngx-toastr';
import { Modal } from 'flowbite';
import { CommonModule } from '@angular/common';
import { Answer, QuestionResponse } from '../../api/questions/get-questions.service';
import { DeleteQuestionService } from '../../api/questions/delete-question.service';

@Component({
  selector: 'app-edit-question',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './edit-question.component.html',
  styleUrl: './edit-question.component.css'
})
export class EditQuestionComponent implements OnInit {
  form: FormGroup;
  questionNumber = 2
  private _question!: QuestionResponse

  @Input()
  set question(question: QuestionResponse){
    this._question = question
    console.log('setting Question')
    console.log(question)
    if(this.form){
      this.updateFormWithQuestion()
    }
  }

  @Output() toggleModalOutput = new EventEmitter<any>();
  @Output() loadQuestionsOutput = new EventEmitter<any>();

  constructor(private fb: FormBuilder, 
      private addQuestionService: AddQuestionService, private toastr: ToastrService, private deleteQuestionService: DeleteQuestionService){
      console.log('Setting question with constructor')
      this.form = this.fb.group({
        question: ['', [Validators.required, Validators.maxLength(200)]],
        answer_one: ['', [Validators.required, Validators.maxLength(200)]],
        answer_two: ['', [Validators.required, Validators.maxLength(200)]],
        answer_three: [''],
        answer_four: [''],
        answer_five: [''],
        correctGroup: ['one'],
        explanation: ['', [Validators.required, Validators.maxLength(200)]],
        difficulty: [0]
      });
  }

  toggleModal(){
    this.updateFormWithQuestion()
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

  updateQuestionNumber(event: any){
    this.questionNumber = event.target.value;
    this.defaultAnswers()
    console.log(this.questionNumber)
  }

  ngOnInit() {
    console.log(this.question)
    this.updateFormWithQuestion();
  }

  printQuestion(){
    console.log(this._question)
    this.updateFormWithQuestion()
  }

  private updateFormWithQuestion() {
    if (this._question) {
      this.form.patchValue({
        question: this._question.questions,
        answer_one: this._question.answers[0]?.answer || '',

        answer_two: this._question.answers[1]?.answer || '',

        answer_three: this._question.answers[2]?.answer || '',

        answer_four: this._question.answers[3]?.answer || '',
        
        answer_five: this._question.answers[4]?.answer || '',

        correctGroup: this.checkCorrect(this._question.answers),
        explanation: this._question.explanation,
        difficulty: this._question.difficulty
      });
      this.questionNumber = this._question.answers.length
    }
  }

  checkCorrect(answers: Answer[]): string{
    const nums = ['one', 'two', 'three', 'four', 'five']

    const correctAnswerIndex = answers.findIndex(answer => answer.correct === true);
    return nums[correctAnswerIndex]
  }

  async onDeleteQuestion(){
    try{
      const request = await this.deleteQuestionService.deleteQuestion(this._question.question_id, this._question.topic_id)
      request.subscribe({
        next: (response) => {
          console.log('Question deleted successfully')
          this.toggleModal()
          this.loadQuestionsOutput.emit()
          this.toastr.success('Question Deleted', 'Successfully deleted question!')
        },
        error: (error) => console.error('Error updating:', error)
      })
    }catch (error) {
      console.error('Authentication error:', error);
    }

  }

  async onUpdateQuestion() {
    console.log(this.form.value); 
    if (this.form.valid) {
      console.log('valid and sending'); 
      try{
        const request = await this.addQuestionService.updateQuestion(this.form.value, this._question.topic_id, this._question.question_id);
        request.subscribe({
          next: (response) => {
            console.log('Question updaded successfully')
            this.toggleModal()
            this.loadQuestionsOutput.emit()
            this.toastr.success('Question Updated', 'Successfully updated question!')
          },
          error: (error) => console.error('Error updating:', error)
        });
      }catch (error) {
        console.error('Authentication error:', error);
      }
    }else{
      console.log('Form Errors:', this.form.errors)
      console.log('Form Status:', this.form.status)
      Object.keys(this.form.controls).forEach(key => {
        const control = this.form.get(key);
        if (!control?.valid) {
          console.log(`\nInvalid Control: ${key}`);
          console.log('Value:', control?.value);
          console.log('Status:', control?.status);
          console.log('Errors:', control?.errors);
          console.log('Validators:', control?.validator);
        }
      });
      this.toastr.warning('Please ensure all fields are filled out!','Oops!', {
        closeButton: true
      })
    }
  }

}
