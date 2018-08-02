// 1. Get data from user {username and password} 
// 2. Save that data and save it somewhere? (variable)
// 3. Create object {"username": "whatever user enters", "password": "whatever the user enters"}
// 4. Provide the object in the body of the request and raw, JSON
// 5. Make a POST request to  http://localhost:8000/api-token-auth/ (after I hit send)
// 6. If error from request tell user they entered wrong data and if success user is able to access notes

// View notes component
// Container of notes
// Delete note component
import React, { Component } from 'react';
import axios from 'axios';

class SignIn extends Component {
    state = {
        username: "",
        password: ""
    }


    handleSign= () => {
        const { username, password } = this.state;
        axios
            .post("https//http://localhost:8000/api-token-auth/", { username, password })
            
    }


    render() {
        return (
            <div>
                <input type="text" placeholder="username"/>
                <input type="password" placeholder="password"/>
                <input type="submit" value="Submit"/>
            </div>
        );
    }
}

export default SignIn;

