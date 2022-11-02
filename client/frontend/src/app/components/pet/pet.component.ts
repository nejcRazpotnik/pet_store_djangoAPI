import { Component, Input, OnInit } from '@angular/core';
import { Animal } from 'src/app/Animal';

@Component({
  selector: 'app-pet',
  templateUrl: './pet.component.html',
  styleUrls: ['./pet.component.css']
})
export class PetComponent implements OnInit {
  @Input() petItem?: Animal;

  constructor() { }

  ngOnInit(): void {

  }

}
