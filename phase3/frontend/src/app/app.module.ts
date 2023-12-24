import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module'
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import {HttpClientModule} from "@angular/common/http";
import { SignInComponent } from './pages/sing-in/sign-in.component';
import { SignUpComponent } from './pages/sign-up/sign-up.component';
import { DoctorComponent } from './pages/doctor/doctor.component';
import { PatientComponent } from './pages/patient/patient.component';
@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    SignUpComponent,
    DoctorComponent,
    PatientComponent

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
