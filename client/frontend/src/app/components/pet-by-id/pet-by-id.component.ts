import { Component, OnInit } from '@angular/core';
import { Animal } from 'src/app/Animal';
@Component({
  selector: 'app-pet-by-id',
  templateUrl: './pet-by-id.component.html',
  styleUrls: ['./pet-by-id.component.css']
})
export class PetByIdComponent implements OnInit {
  animal?: Animal
  id?: number;
  name?: string;
  category?: string;
  pictures?: Array<string> = [];
  status?: string;
  tags?: string;

  constructor() { }

  ngOnInit(): void {
  }
  
  getPet(id: number | undefined) {

  }

  postPet(target:Animal) {

  }

  deletePet(target:Animal) {

  }
}
