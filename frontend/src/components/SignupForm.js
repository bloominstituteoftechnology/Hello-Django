import React, { Component } from 'react';
import PropTypes from 'pro-types';

class SignUpForm extends Component {
    state = {
        username: '',
        passwod: ''
    };

    handle_changes = e => {
        const name = e.target.name;
        const value = e.target.value;
        this.setState(prevstate => {
            const newState = { ...prevstate };
            newState[name] = value;
            return newState;
        });
    };

    render() {
        return (
            <form onSubmit={e => this.props.handle_signup(e, this.state)}>
                <h4>Sign Up</h4>
                <label htmlFor="username">Username</label>
                <input
                    type="text"
                    name="username"
                    value={this.state.username}
                    onChange={this.handle_changes}
                />
                <label htmlFor="password">Password</label>
                <input
                    type="password"
                    name="password"
                    value={this.state.password}
                    onChange={this.handle_changes}
                />
                <input type="submit" />
            </form>
        );
    }
}

export default SignUpForm;