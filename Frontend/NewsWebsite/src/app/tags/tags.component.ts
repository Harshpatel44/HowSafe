import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CatService } from './tags.service';

@Component({
  selector: 'app-tags',
  templateUrl: './tags.component.html',
  styleUrls: ['./tags.component.css']
})


export class TagsComponent implements OnInit {
  public tags=[
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'ko', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
      {"name":'kohli', "url":""}, 
      {"name":'virat', "url":""},
    ];
  constructor(private http: HttpClient, private CatService: CatService) { 
    
  }
  
  sample(){
    console.log('harsh');
    console.log(this.CatService.getCat("lucy"));
  }

  ngOnInit(): void {
   
  }

}
