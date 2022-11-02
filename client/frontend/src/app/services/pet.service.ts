import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Animal } from '../Animal';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PetService {
  private apiURL: string = 'http://localhost:5432/pet'

  constructor(private http:HttpClient) { }

  postPet(pet: Animal){
    return this.http.post<Animal>(this.apiURL, pet);
  }

  putPet(pet: Animal) {
    return this.http.put<Animal>(this.apiURL, pet);
  }
}
