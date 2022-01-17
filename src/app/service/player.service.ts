import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable, pipe } from "rxjs";
import { map } from 'rxjs/operators';
import { Player } from "../model/model";

@Injectable({
  providedIn: "root",
})
export class PlayerService {

  constructor(private http: HttpClient) { }

  getAllPlayers(): Observable<Player[]> {
    return this.http.get<Player[]>(`http://127.0.0.1:5002/players`);
  }

}
