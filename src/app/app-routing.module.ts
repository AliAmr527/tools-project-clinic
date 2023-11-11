import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {SignInComponent} from "./pages/sing-in/sign-in.component";
import {SignUpComponent} from "./pages/sign-up/sign-up.component";
import {DoctorComponent} from "./pages/doctor/doctor.component";
import { PatientComponent } from './pages/patient/patient.component';


const routes: Routes = [
  {path: '' , component: SignInComponent},
  {path: 'patient' , component: PatientComponent},
  {path: 'doctor' , component: DoctorComponent},
  {path: 'signup' , component: SignUpComponent},
  {path: 'signin' , component: SignInComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
