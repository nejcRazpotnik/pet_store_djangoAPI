import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PetByIdComponent } from './pet-by-id.component';

describe('PetByIdComponent', () => {
  let component: PetByIdComponent;
  let fixture: ComponentFixture<PetByIdComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PetByIdComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PetByIdComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
