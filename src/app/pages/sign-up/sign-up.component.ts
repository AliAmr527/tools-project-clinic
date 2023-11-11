import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";
import { SignUpModelResponse } from '../../models/sign-up-model';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrl: './sign-up.component.css'
})
export class SignUpComponent {
  constructor(private router:Router,private http:HttpClient) {
  }

  email:string='';
  name:string='';
  password:string='';
  role:string="doctor";


  signUp(){
    if(this.email.trim().length==0){
      //PRINT HERE
    }else if(this.password.trim().length==0){

    }else if(this.name.trim().length==0){

    }
    else{
      let body = {
        email : this.email,
        password :this.password,
        name:this.name,
        role:this.role
      }
  
        //sign up
        this.http.post<SignUpModelResponse>("http://127.0.0.1:5000/signUp",body).subscribe((data)=>{
          if(data!=null){
            alert("signed up succesfully!")
            this.router.navigateByUrl('/signin');
          }
          
        })
    }
    }
  }

