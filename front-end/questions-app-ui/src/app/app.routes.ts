import { Routes } from '@angular/router';

export const routes: Routes = [    
    {
        path: '',
        pathMatch: 'full',
        loadComponent:() => { 
            return import('./pages/topics/topics.component'). then((m) => m. TopicsComponent);
        },
    }
];