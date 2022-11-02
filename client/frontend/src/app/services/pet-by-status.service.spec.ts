import { TestBed } from '@angular/core/testing';

import { PetByStatusService } from './pet-by-status.service';

describe('PetByStatusService', () => {
  let service: PetByStatusService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PetByStatusService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
