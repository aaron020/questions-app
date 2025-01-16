import { Component, Inject, PLATFORM_ID, signal } from '@angular/core';
import { AuthService } from '../../service/auth.service';
import { Router } from '@angular/router';
import { CommonModule, isPlatformServer } from '@angular/common'; 
import { ThemeService } from '../../service/theme.service';


@Component({
  selector: 'app-nav',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
  isServer: boolean;

  constructor(public authService: AuthService,  private router: Router, private themeService: ThemeService, @Inject(PLATFORM_ID) private platformId: object){
    this.isServer = isPlatformServer(platformId);
  }

  isChecked = signal<boolean>(this.themeService.initTheme());
  
  ngOnInit(): void {
    this.authService.checkInitialAuthState();
  }

  onCheckboxChange(event: Event){
    const isChecked = (event.target as HTMLInputElement).checked;
    this.themeService.toggleDarkMode(isChecked)
    this.isChecked.set(isChecked)
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
