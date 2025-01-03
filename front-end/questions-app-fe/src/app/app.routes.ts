import { Routes } from '@angular/router';

export const routes: Routes = [    
    {
        path: '',
        pathMatch: 'full',
        loadComponent:() => { 
            return import('./pages/home/home.component'). then((m) => m. HomeComponent);
        },
    },
    {
        path: 'add/question/:topic',
        loadComponent:() => {
            return import('./pages/add-question/add-question.component').then((m) => m.AddQuestionComponent)
        } 
    },
    {
        path: 'sigin',
        loadComponent:() => {
            return import('./pages/signin/signin.component').then((m) => m.SigninComponent)
        } 
    }
];
