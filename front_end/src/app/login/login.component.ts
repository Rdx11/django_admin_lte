import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { routerTransition } from '../router.animations';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { User } from '../models/user';

interface UserResponse {
  login: string;
  bio: string;
  company: string;
}



@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.scss'],
    animations: [routerTransition()]
})
export class LoginComponent implements OnInit {
	public user: any = new User(null, null, null);
    constructor(private http:HttpClient,private router:Router) {}
    public response_msg="";
    ngOnInit() {     
    }
    LoginUser(){
      const req = this.http.post('http://127.0.0.1:8000/login/',this.user,{observe: 'response'})
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
          this.response_msg=err.error.response_msg;
        }
      );
    }

   
}
