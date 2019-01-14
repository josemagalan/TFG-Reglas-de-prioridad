import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
/*import { MenuLateral3Component } from './menu-lateral3/menu-lateral3.component';
import { MenuLateral2Component } from './menu-lateral2/menu-lateral2.component';
import { MenuSuperiorComponent } from './menu-superior/menu-superior.component';*/
import { MenuInputEjecucionComponent } from './menu-input-ejecucion/menu-input-ejecucion.component';
import { AppRoutingModule } from './app-routing.module';
import { HomeComponent } from './home/home.component';
import { InputManualComponent } from './input-manual/input-manual.component';
import { ContactListComponent } from './contact-list/contact-list.component';
import { HttpClientModule } from  '@angular/common/http';
import { PiezaComponent } from './pieza/pieza.component';
import { FormFasesComponent } from './form-fases/form-fases.component';
import { TablaResultadosComponent } from './tabla-resultados/tabla-resultados.component';


@NgModule({
  declarations: [
    AppComponent,
   
    MenuInputEjecucionComponent,
    HomeComponent,
    InputManualComponent,
    ContactListComponent,
    PiezaComponent,
    FormFasesComponent,
    TablaResultadosComponent
    
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }