import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { addSlotModelResponse } from '../../models/add-slot-model';
import { Router } from '@angular/router';
import { GetDoctorsList, GetDoctorsListModel } from '../../models/get-doctors-list';

@Component({
  selector: 'app-doctor',
  templateUrl: './doctor.component.html',
  styleUrl: './doctor.component.css',
})
export class DoctorComponent implements OnInit {
  constructor(private router: Router, private http: HttpClient) {}

  id: any;
  date: string = '';
  hour: string = '';
  ngOnInit(): void {
    this.id = localStorage.getItem('doctor_id');
    var num: number = +this.id;
    this.doctorId = num;
    this.docName = localStorage.getItem('doctor_name');
    this.getDoctors();
  }
  doctorId : any;
  docName: any;
  slots:Array<GetDoctorsListModel> = []
  // slots = [
  //   // { aId: 'one', bDate: '10/11/2023', cHour: '1:00 PM' },
  //   // { aId: 'two', bDate: '15/03/2023', cHour: '5:00 PM' },
  //   // { aId: 'three', bDate: '20/01/2023', cHour: '7:00 PM' },
  // ];

  addSlot() {
    if (this.date.trim().length == 0) {
    } else if (this.hour.trim().length == 0) {
    } else {
      console.log(this.id);
      let body = {
        doctorID: this.id,
        Date: this.date,
        Hour: this.hour,
      };
      this.http
        .patch<addSlotModelResponse>(
          'http://127.0.0.1:5000/addAppointment',
          body
        )
        .subscribe((data) => {
          if (data != null) {
            alert('added succesfully');
          }
        });
    }
  }


  getDoctors(){
    this.http.post<GetDoctorsList[]>('http://127.0.0.1:5000/getDoctorAppointments',{doctorID: this.doctorId}).subscribe((data) => {
      if (data != null) {
        this.slots = data
      }
    });
  }
}
