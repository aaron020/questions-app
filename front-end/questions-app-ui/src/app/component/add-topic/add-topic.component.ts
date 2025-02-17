import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { Modal } from 'flowbite';
import { AddTopicService } from '../../api/topics/add-topic.service';
import { ToastrService } from 'ngx-toastr';
import { Router } from '@angular/router';

@Component({
  selector: 'app-add-topic',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './add-topic.component.html',
  styleUrl: './add-topic.component.css'
})
export class AddTopicComponent {
    form: FormGroup;
    private modal: Modal | undefined;
    @Output() toggleModalOutput = new EventEmitter<any>();

    toggleModal(){
      this.defaultValues()
      this.toggleModalOutput.emit()
    }


    constructor(private fb: FormBuilder, private addTopicService: AddTopicService, private toastr: ToastrService, private router: Router){
      this.form = this.fb.group({
        topic_name: ['', [Validators.required, Validators.maxLength(200)]],
        description: ['', [Validators.required, Validators.maxLength(200)]],
        category: ['science'],
      });
    }


    defaultValues(){
      this.form.patchValue({
        topic_name: '',
        description: '',
        category: ['science'],
      })
    }


    async onAddTopic(){
      if (this.form.valid) {
        try{
          const request = await this.addTopicService.addTopic(this.form.value)
          request.subscribe({
            next: (response) => {
              const navigate_url = `/topic/${response}`
              this.router.navigate([navigate_url]);
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
