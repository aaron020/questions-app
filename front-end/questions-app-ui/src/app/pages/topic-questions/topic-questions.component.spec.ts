import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TopicQuestionsComponent } from './topic-questions.component';

describe('TopicQuestionsComponent', () => {
  let component: TopicQuestionsComponent;
  let fixture: ComponentFixture<TopicQuestionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TopicQuestionsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(TopicQuestionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
