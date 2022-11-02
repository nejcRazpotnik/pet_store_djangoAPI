import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Animal } from '../Animal';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PetByIdService {
  private apiURL: string = 'http://localhost:5432/pet/'

  constructor(private http:HttpClient) { }

  getById(id: number): Observable<Animal> {
    return this.http.get<Animal>(this.apiURL + id.toString() + '/')
  }

  deleteById(id: number): Observable<Animal> { //use form
    let headers = new HttpHeaders({
      'Content-type': 'application/x-www-form-urlencoded'
    });
    let options = { headers: headers};
    let endpointURL:string = this.apiURL + id.toString() + '/';
    return this.http.delete<Animal>(endpointURL, options);
  }

  postById(id: number, body: Animal)/*: Observable<Animal>  */{ //use form
    let headers = new HttpHeaders({
      'Content-type': 'application/x-www-form-urlencoded'
    });
    let options = { headers: headers};
    let endpointURL:string = this.apiURL + id.toString() + '/';
    return this.http.post<Animal>(endpointURL, body, options);
  }

}
