import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PetComponent } from './components/pet/pet.component';

import { HttpClientModule } from '@angular/common/http'
import { FormsModule} from '@angular/forms';
import { PetByIdComponent } from './components/pet-by-id/pet-by-id.component';
import { ButtonComponent } from './components/button/button.component'

@NgModule({
  declarations: [
    AppComponent,
    PetComponent,
    PetByIdComponent,
    ButtonComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
