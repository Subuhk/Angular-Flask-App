import { Component, OnInit } from "@angular/core";
import { Team, Player } from "../../model/model";
import { ActivatedRoute } from "@angular/router";
import { Sort } from "@angular/material/sort";

@Component({
  selector: "app-team-details",
  templateUrl: "./team-details.component.html",
  styleUrls: ["./team-details.component.css"],
})
export class TeamDetailsComponent implements OnInit {
  teamId: number;
  team: Team;
  players: Player[];
  sortedData: Player[];

  constructor(private route: ActivatedRoute) {
    this.teamId = +this.route.snapshot.paramMap.get("teamId");
  }

  ngOnInit(): void {
    //To retreive details of selected team
    this.team = this.route.snapshot.data.team[0];

    //To retreive all the players of selected team
    this.players = this.route.snapshot.data.players.filter(
      (player) => player.teamId === this.team.id && player.position !== ""
    );

    this.sortedData = this.players.slice();
  }

  //for sorting the columns of player table
  sortData(sort: Sort) {
    const data = this.players.slice();
    if (!sort.active || sort.direction === "") {
      this.sortedData = data;
      return;
    }

    this.sortedData = data.sort((a, b) => {
      const isAsc = sort.direction === "asc";
      switch (sort.active) {
        case "firstName":
          return this.compare(a.firstName, b.firstName, isAsc);
        case "position":
          return this.compare(a.position, b.position, isAsc);
        case "heightInches":
          return this.compare(a.heightInches, b.heightInches, isAsc);
        case "weightPounds":
          return this.compare(a.weightPounds, b.weightPounds, isAsc);
        default:
          return 0;
      }
    });
  }

  compare(a: number | string, b: number | string, isAsc: boolean) {
    return (a < b ? -1 : 1) * (isAsc ? 1 : -1);
  }
}
