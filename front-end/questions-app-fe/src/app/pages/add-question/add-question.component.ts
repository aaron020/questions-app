import { CommonModule } from '@angular/common';
import { Component, OnInit, signal } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { AddQuestionService } from '../../service/api/add-question.service';

@Component({
  selector: 'app-add-question',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './add-question.component.html',
  styleUrl: './add-question.component.css'
})
export class AddQuestionComponent implements OnInit{
  topic = signal<string>('');
  form: FormGroup;

  constructor(private route: ActivatedRoute, private fb: FormBuilder, private addQuestionService: AddQuestionService) {
    this.form = this.fb.group({
      question: ['', [Validators.required, Validators.max(200)]],
      answer_a: ['', [Validators.required, Validators.max(200)]],
      answer_b: ['', [Validators.required, Validators.max(200)]],
      answer_c: ['', [Validators.required, Validators.max(200)]],
      answer_d: ['', [Validators.required, Validators.max(200)]],
      answer_a_correct: [false],
      answer_b_correct: [false],
      answer_c_correct: [false],
      answer_d_correct: [false],
      explanation: ['', [Validators.required, Validators.max(200)]],
      difficulty: ['defualt', [Validators.required, Validators.pattern('^(?!default$).*$')]]
      
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.topic.set(params['topic']); // Assuming 'category' is your route parameter
    });
  }

  async onSubmit() {
    console.log(this.form.value); 
    if (this.form.valid) {
      console.log('valid and sending'); 
      try{
        const request = await this.addQuestionService.addQuestion(this.form.value);
        request.subscribe({
          next: (response) => console.log('Question created successfully'),
          error: (error) => console.error('Error creating question:', error)
        });
      }catch (error) {
        console.error('Authentication error:', error);
      }
    }
  }

}
