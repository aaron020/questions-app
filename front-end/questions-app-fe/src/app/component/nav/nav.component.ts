import { Component, signal } from '@angular/core';

@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
  isChecked = signal(false)
  ngOnInit(): void {
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

}
