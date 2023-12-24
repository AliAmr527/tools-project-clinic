export interface GetDoctorsList {
  name: string;
  id: Number;
}
export class GetDoctorsListModel {
  constructor() {
    this.name = '';
    this.id = 0;
  }
  name: string;
  id: Number;
}
