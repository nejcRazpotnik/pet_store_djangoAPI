import { TestBed } from '@angular/core/testing';

import { PetByIdService } from './pet-by-id.service';

describe('PetByIdService', () => {
  let service: PetByIdService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PetByIdService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
