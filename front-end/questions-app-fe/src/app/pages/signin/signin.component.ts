import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { AuthService } from '../../service/auth.service';

@Component({
  selector: 'app-signin',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './signin.component.html',
  styleUrl: './signin.component.css'
})
export class SigninComponent {
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService){}

  async onSubmit() {
    try {
      const result = await this.authService.signIn(this.username, this.password);
      
      if (result.success) {
        console.log('Successfully logged in!');
        // You can add navigation logic here
      } else {
        console.error('Login failed:', result.error);
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  }
}


