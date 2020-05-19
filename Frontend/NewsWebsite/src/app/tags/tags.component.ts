import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { RequestResponse } from '../app.service'

@Component({
  selector: 'app-tags',
  templateUrl: './tags.component.html',
  styleUrls: ['./tags.component.css']
})


export class TagsComponent implements OnInit {
  
  constructor(private http: HttpClient, private tagsLocal: RequestResponse) { 
    this.tagsLocal.getTags()
      .subscribe(data=> this.tagsList = data);
  }
  public tagsList=[];
  



  sample(){
    console.log('harsh');
    console.log(this.tagsList);
  }

  ngOnInit(): void {
    
  }

}
