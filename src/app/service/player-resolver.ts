import { Observable } from "rxjs";
import { Injectable } from "@angular/core";
import { Resolve } from "@angular/router";
import { PlayerService } from "./player.service";

@Injectable()
export class PlayerResolver implements Resolve<Observable<any>> {
  constructor(private playerService: PlayerService) { }

  resolve(): Observable<any> {
    return this.playerService.getAllPlayers();
  }
}
