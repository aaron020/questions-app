import { Component, signal } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common'; 

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
  constructor(public authService: AuthService,  private router: Router){}

  isChecked = signal(false)
  ngOnInit(): void {
    this.authService.checkInitialAuthState();
    const storedTheme = localStorage.getItem('theme');
    const htmlElement = document.documentElement;



    if (storedTheme === 'dark') {
      htmlElement.classList.add('dark');
      this.isChecked.set(true)
    } else {
      htmlElement.classList.remove('dark');
    }
  }

  onCheckboxChange(event: Event){
    const isChecked = (event.target as HTMLInputElement).checked;
    const htmlElement = document.documentElement;

    console.log('Checkbox is now:', isChecked ? 'Checked' : 'Unchecked');
    // Perform actions based on the checkbox state
    if (isChecked) {
      htmlElement.classList.add('dark'); // Enable dark mode
      localStorage.setItem('theme', 'dark');
    } else {
      htmlElement.classList.remove('dark'); // Disable dark mode
      localStorage.setItem('theme', 'light');
    }
    
  }

  async handleSignOut(event: MouseEvent){
    event.preventDefault();

    try{
      const result = await this.authService.signOut();
    


      if (result.success) {
        await this.router.navigate(['/']);
      }else {
        // Handle any logout errors here
        console.error('Logout failed:', result.error);
        // You might want to show a toast notification here
      }
    } catch(error){
      console.log(error)
    }
  }

}
