import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { Team } from "../model/model";
import { map } from "rxjs/operators";

@Injectable({
  providedIn: "root",
})
export class TeamService {
  constructor(private http: HttpClient) { }

  getAllTeams(): Observable<Team[]> {
    return this.http.get<Team[]>(`http://127.0.0.1:5002/teams`).pipe(map(
      teams => teams
    ));
  }

  getTeamDetails(teamId: number): Observable<Team> {
    return this.http.get<Team>(`http://127.0.0.1:5002/teams/${teamId}`);
  }
}
