import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatIconModule } from '@angular/material/icon';

import { ButtonOverviewExample } from './buttons/button-overview-example';
import { MatDividerModule} from '@angular/material/divider';

@NgModule({
  declarations: [
    AppComponent,
    ButtonOverviewExample
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatIconModule,
    MatDividerModule
  ],
  providers: [],
  bootstrap: [AppComponent, ButtonOverviewExample]
})
export class AppModule { }
