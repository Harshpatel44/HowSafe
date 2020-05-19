import { Component, OnInit } from '@angular/core'
import { RequestResponse } from '../app.service'
import { HttpClient } from '@angular/common/http'

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {
  public categories=[]
  constructor( private http:HttpClient, private requestResponse:RequestResponse) {
      this.requestResponse.getCategories()
      .subscribe(data=> this.categories = data)
   }
  // public categories=[
  //   {"name":"General News"},
  //   {"name":"Sports News"},
  //   {"name":"Entertainment News"},
  //   {"name":"Technology News"},
  //   {"name":"Science News"},
  //   {"name":"Business News"},
  // ]
  ngOnInit(): void {
  }

}
