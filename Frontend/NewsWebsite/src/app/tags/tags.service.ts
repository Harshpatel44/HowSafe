import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable, Subject, asapScheduler, pipe, of, from, interval, merge, fromEvent } from 'rxjs';

export interface Cat {
  name: string
}

@Injectable()
export class CatService {
  constructor(private http: HttpClient) {}

//   getAllCats(){
//     return this.http.get('http://localhost:3000/tags/cats')
//   }

  getAllCats(): Observable<Cat[]> {
    return this.http.get<Cat[]>('http://localhost:3000/tags/cats')
  }

  getCat(name: string){
    return this.http.get<Cat>('http://localhost:3000/tags/cats/' + name)
  }

//   insertCat(cat: Cat){
//     return this.http.post<Cat>('http://localhost:8000/api/cats/', cat)
//   }

//   updateCat(cat: Cat){
//     return this.http.put<void>(
//       'http://localhost:8000/api/cats/' + cat.name,
//       cat
//     )
//   }

//   deleteCat(name: string) {
//     return this.http.delete('http://localhost:8000/api/cats/' + name)
//   }
}