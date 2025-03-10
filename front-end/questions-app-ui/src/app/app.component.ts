import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { NavComponent } from './component/nav/nav.component';
import { initFlowbite } from 'flowbite';
import { AddQuestionComponent } from './component/add-question/add-question.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, NavComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'questions-app-ui';
  
  ngOnInit(): void {
    initFlowbite();
  }
}
