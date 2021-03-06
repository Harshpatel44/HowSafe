import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs'


export interface tags{
    name : string
}
export interface news{
    heading : string
    description : string
    imageUrl : string
    url : string
    publishedAt : string
    source : string
}
export interface categories{
    name: string
}

@Injectable()
export class RequestResponse{
    private dir="http://localhost:3000"
    constructor(private http:HttpClient){

    }

    getTags():Observable<tags[]>{
        return this.http.get<tags[]>(this.dir+"/tags/")
    }

    getNews():Observable<news[]>{
        return this.http.get<news[]>(this.dir+"/news/")
    }
    getCategories():Observable<categories[]>{
        return this.http.get<categories[]>(this.dir+"/categories/")
    }
}