import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RequestResponse } from '../app.service'
import { strict } from 'assert';

@Component({
  selector: 'app-tags',
  templateUrl: './tags.component.html',
  styleUrls: ['./tags.component.css']
})


export class TagsComponent implements OnInit {
  
  public tagsList=[]
  constructor(private http: HttpClient, private requestResponse: RequestResponse) { 
    this.requestResponse.getTags()
      .subscribe(data => this.tagsList = data)
  }
  
  // sample(){
  //   // var tagsList=this.tagsList[0].toString()
  //   // console.log(tagsList)
  //   // console.log(JSON.stringify(tagsList))


  //   console.log(this.tagsList)
  // }
  ngOnInit(): void {
    
  }

}
