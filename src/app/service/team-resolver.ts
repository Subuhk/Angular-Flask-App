import { Injectable } from "@angular/core";
import { Resolve, ActivatedRouteSnapshot } from "@angular/router";
import { Observable } from "rxjs";
import { Team } from "../model/model";
import { TeamService } from "./team.service";

@Injectable()
export class TeamResolver implements Resolve<Observable<any>> {
  constructor(private teamService: TeamService) { }

  resolve(route: ActivatedRouteSnapshot): Observable<Team> {
    const teamId = route.params["teamId"];
    return this.teamService.getTeamDetails(teamId);
  }
}
