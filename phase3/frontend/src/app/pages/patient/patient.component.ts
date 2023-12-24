import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import {HttpClient} from "@angular/common/http";
import { reserveSlotModelResponse } from '../../models/reserve_slot_model';
import {Router} from "@angular/router";
import { getSlotsModelArray, getSlotsModelResponseBody } from '../../models/get-doctor-appointments';
import { getDoctorsResponse, getDoctorsResponseModel } from '../../models/get-doctor';
import { getSlotsResponse, getSlotsResponseModel } from '../../models/get-slots-model';
import { ElementRef } from '@angular/core';

@Component({
  selector: 'app-patient',
  templateUrl: './patient.component.html',
  styleUrl: './patient.component.css'
})

export class PatientComponent implements OnInit {
  constructor(private router:Router,private http:HttpClient,private elRef:ElementRef) {
  }
  doctorsNames : Array<getDoctorsResponseModel> = [];

  appointmentSlots : Array<getSlotsModelArray> = [];
  patientID:Number = -1
  slots : Array<getSlotsResponseModel> = []

  ngOnInit(): void {
    this.id=localStorage.getItem("patient_id")
    var num: number = +this.id;
    this.patientID = num;
    this.getReservedSlots()
    this.patientName = localStorage.getItem('patient_name');
    this.getDoctors()
    this.edit = this.elRef.nativeElement.querySelector('#Edit');
    this.create = this.elRef.nativeElement.querySelector('#create');
    this.reserveButton = this.elRef.nativeElement.querySelector('#reserveButton');
    this.editButton = this.elRef.nativeElement.querySelector('#editButton');
    this.oldSlotID
  }


  edit:any
  create:any
  reserveButton:any
  editButton:any
  id:any
  patientName:any
  selectedDr:Number = -1
  slotID:Number = -1
  oldSlotID:Number = -1

  onDoctorChange(value:string){
    var val:Number = +value
    this.selectedDr = val
    this.getSlots()
  }

  CancelFunction(val:Number){
    this.http.post("https://backend-ali-elmallah-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/cancelReservation",{PatientID:this.patientID,slotID:val}).subscribe((data)=>{
      if(data!=null){
        alert("reservation cancelled!")
      }
    })
  }

  grabIdForEditFunction(val:Number){
    this.oldSlotID = val
    this.create.style.display = 'none'
    this.reserveButton.style.display = 'none'
    this.edit.style.display = 'block'
    this.editButton.style.display = 'inline'
  }

  editFunction(){
    this.http.post("http://localhost:5000/updateReservation",{newSlotID:this.slotID,patientID:this.patientID,slotID:this.oldSlotID}).subscribe((data)=>{
      if(data!=null){
        alert("updated successfully!")
      }
    })
    this.create.style.display = 'block'
    this.reserveButton.style.display = 'inline'
    this.edit.style.display = 'none'
    this.editButton.style.display = 'none'
  }
  
  getDoctors(){
    this.http.get<getDoctorsResponse[]>("https://backend-ali-elmallah-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/getDoctors",).subscribe((data)=>{
      if(data!=null){
        this.doctorsNames=data
        console.log(data)
      }
    })
  }

  onReservationChange(value:string){
    var val:Number = +value 
    this.slotID = val
  }

  reserveFunction(){
    this.http.patch("https://backend-ali-elmallah-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/reserveSlot",{slotID:this.slotID,patientID:this.patientID}).subscribe((data)=>{
      if(data!=null){
        alert("reserved successfully!")
      }
    })
  }

  getSlots(){
    this.http.post<getSlotsModelResponseBody[]>("https://backend-ali-elmallah-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/getDoctorAppointmentsWithId",{doctorID:this.selectedDr}).subscribe((data)=>{
      if(data!=null){
        this.appointmentSlots=data
        console.log(data)
      }
    })
  }

  getReservedSlots(){
    this.http.post<getSlotsResponse[]>("https://backend-ali-elmallah-dev.apps.sandbox-m4.g2pi.p1.openshiftapps.com/getReservations",{patientID:this.patientID}).subscribe((data)=>{
      if(data!=null){
        this.slots=data
        console.log(data)
      }
    })
  }

}