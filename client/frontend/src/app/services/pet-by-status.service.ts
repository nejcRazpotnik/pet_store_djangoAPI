import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Animal } from '../Animal';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PetByStatusService {
  private apiURL: string = 'http://localhost:5432/pet/findByStatus';

  constructor(private http:HttpClient) { }

  getByStatus(statuses: Array<string>) {
    let append:string = '?';
    for (let i = 0; i < statuses.length; i++) {
      append += statuses[i] + ",";
    }
    return this.http.get<Animal[]>(this.apiURL);
  }
}
