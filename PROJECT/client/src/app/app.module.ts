import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';

import { AppComponent } from './app.component';
import { MessageComponent } from "./chat/messages/message.component";
import { MessageListComponent } from "./chat/messages/message-list.component";
import { MessageInputComponent } from "./chat/messages/message-input.component";
import { MessagesComponent } from "./chat/messages/messages.component";
import { ChatComponent } from './chat/chat.component';
import { ProfileComponent } from './profile/profile.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { AuthenticationService } from './authentication.service';
import { AuthGuardService } from './auth-guard.service';

const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'chat', component: ChatComponent },
    { path: 'messages', component: MessagesComponent },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'profile', component: ProfileComponent, canActivate: [AuthGuardService] }
];

@NgModule({
    declarations: [
        AppComponent,
        MessageComponent,
        MessageListComponent,
        MessageInputComponent,
        MessagesComponent,
        ProfileComponent,
        LoginComponent,
        RegisterComponent,
        HomeComponent,
        ChatComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        HttpClientModule,
        RouterModule.forRoot(routes),
    ],
    providers: [
        AuthenticationService,
        AuthGuardService
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
