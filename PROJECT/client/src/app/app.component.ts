import { Component } from '@angular/core';
import { AuthenticationService } from './authentication.service';
import { MessageService } from "./chat/messages/message.service";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [MessageService]
})
export class AppComponent {
  constructor(public auth: AuthenticationService) {}
}
