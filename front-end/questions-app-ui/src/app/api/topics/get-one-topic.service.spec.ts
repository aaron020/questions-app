import { TestBed } from '@angular/core/testing';

import { GetOneTopicService } from './get-one-topic.service';

describe('GetOneTopicService', () => {
  let service: GetOneTopicService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetOneTopicService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
