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
        path: 'signup',
        loadComponent:() => {
            return import('./pages/signup/signup.component').then((m) => m.SignupComponent)
        } 
    },
    {
        path: 'topic/:topic',
        loadComponent:() => {
            return import('./pages/topic-questions/topic-questions.component').then((m) => m.TopicQuestionsComponent)
        } 
    },
    {
        path: 'question/add/:topic',
        loadComponent:() => {
            return import('./pages/add-question/add-question.component').then((m) => m.AddQuestionComponent)
        } 
    },
    {
        path: 'topic/modify/:topic',
        loadComponent:() => {
            return import('./pages/topic-question-modify/topic-question-modify.component').then((m) => m.TopicQuestionModifyComponent)
        } 
    },
    {
        path: 'topic/test/:topic',
        loadComponent:() => {
            return import('./pages/topic-test/topic-test.component').then((m) => m.TopicTestComponent)
        } 
    },

];