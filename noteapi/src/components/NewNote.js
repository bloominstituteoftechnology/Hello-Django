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

    postNote = e => {
        e.preventDefault();
        const token = "Token a30df5495e88a321b9d83f4b435f65502a0ebc0c"
        const note = { title: this.state.title, content: this.state.content, url: this.state.url }

        const option = {
            method: 'POST',
            url: "https://frozen-ridge-71012.herokuapp.com/api/notes/",
            data: note,
            headers: { 'content-type': 'application/json', 'Authorization': token }
        }

        axios(option)
        .then(note => {
            console.log(note)
            window.location.reload();
        })
        .catch(err => 
            console.log(err)
        )
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
                    <input 
                        name="content"
                        value={ this.state.content }
                        placeholder="Content"
                        type="text"
                        onChange = { this.textChange }
                    />
                    <input 
                        name="url"
                        value={ this.state.url }
                        placeholder="URL"
                        type="text"
                        onChange = { this.textChange }
                    />
                    <button onClick={ this.postNote }>Post New Note</button>
                </form>
            </div>
        )
    }
}

export default NewNote;