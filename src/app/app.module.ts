import { NgModule } from "@angular/core";
import { BrowserModule } from "@angular/platform-browser";
import { RouterModule } from "@angular/router";
import { ReactiveFormsModule } from "@angular/forms";

import { AppComponent } from "./app.component";
import { TopBarComponent } from "./component/top-bar/top-bar.component";
import { TeamListComponent } from "./component/team-list/team-list.component";
import { TeamDetailsComponent } from "./component/team-details/team-details.component";
import { HTTP_INTERCEPTORS, HttpClientModule } from "@angular/common/http";
import { ServerMockService } from "./mock/server-mock.service";
import { TeamResolver } from "./service/team-resolver";
import { PlayerResolver } from "./service/player-resolver";
import { MatSortModule } from "@angular/material/sort";
import { MatCardModule } from '@angular/material/card';
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";

@NgModule({
  imports: [
    BrowserModule,
    ReactiveFormsModule,
    HttpClientModule,
    MatSortModule,
    MatCardModule,
    RouterModule.forRoot(
      [
        { path: "", component: TeamListComponent },
        {
          path: "teams/:teamId",
          component: TeamDetailsComponent,
          resolve: {
            team: TeamResolver,
            players: PlayerResolver,
          },
        },
      ],
      { useHash: true }
    ),
    BrowserAnimationsModule,
  ],
  declarations: [
    AppComponent,
    TopBarComponent,
    TeamListComponent,
    TeamDetailsComponent,
  ],
  bootstrap: [AppComponent],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: ServerMockService, multi: true },
    TeamResolver,
    PlayerResolver,
  ],
})
export class AppModule { }
