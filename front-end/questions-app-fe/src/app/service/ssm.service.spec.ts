import { TestBed } from '@angular/core/testing';

import { SsmService } from './ssm.service';

describe('SsmService', () => {
  let service: SsmService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(SsmService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
