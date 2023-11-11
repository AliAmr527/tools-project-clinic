import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HttpClient} from "@angular/common/http";
import { reserveSlotModelResponse } from '../../models/reserve_slot_model';
import {Router} from "@angular/router";
import { getSlotsModelResponseBody } from '../../models/get-doctor-appointments';
import { getDoctorsResponseModel } from '../../models/get-doctor';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})
export class PatientComponent implements OnInit {
  constructor(private router:Router,private http:HttpClient) {
  }
  doctorsNames : Array<getDoctorsResponseModel> = [];

  Doctorslots : Array<any> = [];
  slotID:number=0
  patientID:any
  patientName : string = "Ali";
  slots = [
    { aId: 'one', bDate: '10/11/2023', cHour: '1:00 PM' ,dDoctor:'Ali'},
    { aId: 'two', bDate: '15/03/2023', cHour: '5:00 PM' ,dDoctor:'Ali'},
    { aId: 'three', bDate: '20/01/2023', cHour: '7:00 PM',dDoctor:'Ali' }
  ];

  doctors = ['ali', 'ali', 'ali']

  ngOnInit(): void {
    this.patientID=localStorage.getItem("patient_id")
  }

  

  onDoctorChange(value:string){

    this.getDoctors()


    // this.http.get<getSlotsModelResponseBody[]>("http://127.0.0.1:5000/getDoctors").subscribe((data)=>{
    //   if(data!=null){
    //     this.Doctorslots=data  
    //     console.log(this.Doctorslots)        
    //   }
    // })
    // var val = +value
    
    
    // console.log(val)
    // let body = {
      //   doctorID:val
    // }

  //   this.http.post<getSlotsModelResponseBody[]>("http://127.0.0.1:5000/getDoctorAppointments",body).subscribe((data)=>{
  //         if(data!=null){
  //           this.Doctorslots=data  
  //           console.log(this.Doctorslots)        
  //         }
  //       })
  // }
  }
  getDoctors(){
    this.http.get<getDoctorsResponseModel[]>("http://127.0.0.1:5000/getDoctors",).subscribe((data)=>{
      if(data!=null){
        this.doctorsNames=data
        console.log(this.doctorsNames)
      }
    })
  }
  onReservationChange(value:string){
    var val = +value 
  }
}