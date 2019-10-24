import { Component, OnInit } from '@angular/core';
import { routerTransition } from '../router.animations';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { User } from '../models/user';

@Component({
    selector: 'app-signup',
    templateUrl: './signup.component.html',
    styleUrls: ['./signup.component.scss'],
    animations: [routerTransition()]
})
export class SignupComponent implements OnInit {
	public user: any = new User(null, null, null);
    constructor(private http:HttpClient,private router:Router) {}
    public response_msg="";

    ngOnInit() {}


    SignupUser(){
      const req = this.http.post('http://127.0.0.1:8000/register/',this.user,{observe: 'response'})
      .subscribe(
        res => {
        if(res.status==200){
            localStorage.setItem('token', res.body['token']);
            localStorage.setItem('username', res.body['username']);
            localStorage.setItem('isLoggedin', 'true');
            this.router.navigate(['/dashboard']);
          }
        },
        err => {
          var msg="";
          for (const key of Object.keys(err.error.response_msg)) {
            if(msg!="")
            {
              msg+=" ";
            }
             msg+=key+' : '+err.error.response_msg[key];
          }
          
          this.response_msg=msg;
        }
      );
    }
}
