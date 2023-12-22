import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HttpClient} from "@angular/common/http";
import {SignInModelResponse} from "../../models/sign-in-model";
import {Router} from "@angular/router";

@Component({
  selector: 'app-login',
  templateUrl: './sign-in.component.html',
  styleUrl: './sign-in.component.css'
})
export class SignInComponent {
  // signInArray : SignInModelResponse[] = [
  //   new SignInModelResponse() = ('','','0)
  // ];
  // signInArray = new SignInModelResponse;
  // signInArray = []
  // signInArray: Array<SignInModelResponse> = new Array();
  
  // signInArray2 : Array<SignInModelResponse> = [
  //   {name:"",role:"doctor",id:0}
  // ];

  constructor(private router:Router,private http:HttpClient) {
  }
  email : string = '';
  password: string = '';
  a:string="";

  signIn(){
    if(this.email.trim().length==0){

    }else if(this.password.trim().length==0){

    }
    else {
      let body = {
        "email" : this.email,
        "password" :this.password
      }
      //PUT THE LOGIN API HERE
      this.http.post<SignInModelResponse>(`http://127.0.0.1:5000/signIn`,body).subscribe((data)=>{
          if (data['role']=='doctor'){
            this.router.navigateByUrl('/doctor');
            localStorage.setItem("doctor_id",`${data['id']}`)
            localStorage.setItem("doctor_name",`${data['name']}`)

          }else {
            this.router.navigateByUrl('/patient');
            localStorage.setItem("patient_id",`${data['id']}`)
            localStorage.setItem("patient_name",`${data['name']}`)
          }
        }
      )
    }
  }

}
