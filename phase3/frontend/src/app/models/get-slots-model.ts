export interface getSlotsResponse {
    id: Number;
  date: string;
  hour: string;
  
}
export class getSlotsResponseModel {
  constructor() {
    this.id = 0;
    this.date = '';
    this.hour = '';
  }
  id: Number;
  date: string;
  hour: string;
}
