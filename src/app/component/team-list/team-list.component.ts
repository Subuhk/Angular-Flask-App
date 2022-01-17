import { Component, OnInit } from "@angular/core";
import { Team } from "../../model/model";
import { TeamService } from "../../service/team.service";
import { delay } from "rxjs/operators";
import { PlayerService } from "src/app/service/player.service";

@Component({
  selector: "app-team-list",
  templateUrl: "./team-list.component.html",
  styleUrls: ["./team-list.component.css"],
})
export class TeamListComponent implements OnInit {
  teams: Team[];

  constructor(private teamService: TeamService) { }

  ngOnInit() {

    this.teamService.getAllTeams().subscribe((result) => (this.teams = result));
  }
}
