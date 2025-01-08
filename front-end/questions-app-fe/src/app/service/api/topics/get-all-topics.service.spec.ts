import { TestBed } from '@angular/core/testing';

import { GetAllTopicsService } from './get-all-topics.service';

describe('GetAllTopicsService', () => {
  let service: GetAllTopicsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GetAllTopicsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
