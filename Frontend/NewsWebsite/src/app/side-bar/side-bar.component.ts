import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {

  constructor() { }
  public categories=[
    {"name":"General News"},
    {"name":"Sports News"},
    {"name":"Entertainment News"},
    {"name":"Technical News"},
    {"name":"Science News"},
  ]
  ngOnInit(): void {
  }

}
