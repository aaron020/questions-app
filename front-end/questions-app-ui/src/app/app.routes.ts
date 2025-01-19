import { Routes } from '@angular/router';

export const routes: Routes = [    
    {
        path: '',
        pathMatch: 'full',
        loadComponent:() => { 
            return import('./pages/topics/topics.component'). then((m) => m. TopicsComponent);
        },   
    },
    {
        path: 'signin',
        loadComponent:() => {
            return import('./pages/signin/signin.component').then((m) => m.SigninComponent)
        } 
    },
    {
        path: 'topic/:topic',
        loadComponent:() => {
            return import('./pages/topic-questions/topic-questions.component').then((m) => m.TopicQuestionsComponent)
        } 
    },

];