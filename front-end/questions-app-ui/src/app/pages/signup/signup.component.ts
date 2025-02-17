import { Component } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { ToastrService } from 'ngx-toastr';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-signup',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  email: string = ''
  username: string = '';
  password: string = '';

  constructor(private authService: AuthService, private toastr: ToastrService){
  }

  async onSubmit() {
    try {
      const result = await this.authService.signUp(this.email, this.username, this.password);
      
      if (result.success) {
        this.toastr.info('Succesfully signed up!', `Welcome ${this.username}`)
        // You can add navigation logic here
      } else {
        console.error('Login failed:', result.error);
      }
    } catch (error) {
      console.error('An error occurred:', error);
    }
  }
}
