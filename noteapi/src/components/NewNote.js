import React, { Component } from 'react';
import axios from 'axios';

class NewNote extends Component {
    constructor(props) {
        super(props);
        this.state = {
            title: "",
            content: "",
            url: ""
        }
    }

    textChange = e => {
        this.setState({ [e.target.name]: e.target.value })
    }

    render() {
        return (
            <div>
                <form>
                    <input 
                    name="title"
                    value={ this.state.title }
                    placeholder="Title"
                    type="text"
                    onChange = { this.textChange }
                    />
                </form>
            </div>
        )
    }
}

export default NewNote;