import React, { Component } from 'react';
import axios from 'axios';

import './App.css';

class App extends Component {
  constructor() {
    super();
    this.state = {
      data: [],
    }
  }

  componentDidMount() {
  
    const token = "Token a30df5495e88a321b9d83f4b435f65502a0ebc0c"

    const option = {
        method: 'GET',
        headers: { 'content-type': 'application/json', 'Authorization': token },
        url: "https://frozen-ridge-71012.herokuapp.com/api/notes/",
    }

    axios(option)
        .then(res => {
            console.log(res)
            this.setState({ data: res.data })
        })
        .catch(err => {
          console.log(err)
        });
  }

  getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  

  render() {
    return (
      <div className="App">
        <div>{ this.state.data.map(note => {
          return (
          <div className="note" key={note.content} style={{ "background": this.getRandomColor() }}> 
            <h1 className="note__h1"> { note.title } </h1>
            <p className="note__p"> { note.content } </p>
            </div>
        )})}
        </div>
      </div>
    );
  }
}

export default App;
