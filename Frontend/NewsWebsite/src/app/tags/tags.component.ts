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
  public tags2=[];
  sample(){
    console.log('harsh');
    console.log(this.tags2);
  }

  ngOnInit(): void {
    this.CatService.getAllCats()
      .subscribe(data=> this.tags2 = data);
  }

}
