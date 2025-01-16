import { isPlatformBrowser, isPlatformServer } from '@angular/common';
import { Inject, TransferState, Injectable, makeStateKey, PLATFORM_ID } from '@angular/core';


const THEME_KEY = makeStateKey<boolean>('theme');

@Injectable({
  providedIn: 'root'
})
export class ThemeService {
  constructor(@Inject(PLATFORM_ID) private platformId: Object, private transferState: TransferState) {
  }

  initTheme(){
    if (this.transferState.hasKey(THEME_KEY) && isPlatformServer(this.platformId)){
      const storedState = this.transferState.get(THEME_KEY, true)
      this.applyTheme(storedState)
      console.log(`returning value storedstate ${storedState}`)
      return true
    }

    let isDark = false

    if(isPlatformBrowser(this.platformId)){
      const storedTheme = localStorage.getItem('theme');
      isDark = storedTheme === 'dark';
    }

    this.transferState.set(THEME_KEY, isDark);
    this.applyTheme(isDark);
    console.log(`returning value isdark ${isDark}`)
    return isDark;
  }

  private applyTheme(isDark: boolean) {
    if (isPlatformBrowser(this.platformId)) {
      const htmlElement = document.documentElement;
      if (isDark) {
        htmlElement.classList.add('dark');
      } else {
        htmlElement.classList.remove('dark');
      }
    }
  }

  toggleDarkMode(checked: boolean){
    if (isPlatformBrowser(this.platformId)){
      const htmlElement = document.documentElement;
      if (checked){
        htmlElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
      }else{
        htmlElement.classList.remove('dark');
        localStorage.setItem('theme', 'light');
      }
    }
    this.transferState.set(THEME_KEY, checked);

  }

}
