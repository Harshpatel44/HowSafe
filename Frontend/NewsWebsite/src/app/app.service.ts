import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'


export interface tags{
    name : string
}

@Injectable()
export class RequestResponse{
    private dir="http://localhost:3000"
    constructor(private http:HttpClient){

    }

    getTags():Observable<tags[]>{
        return this.http.get<tags[]>(this.dir+"/tags/")
    }
}