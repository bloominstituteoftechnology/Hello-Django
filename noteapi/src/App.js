import React, { Component } from 'react';
import axios from 'axios';

import './App.css';
import DisplayNote from './components/DisplayNote';
import NewNote from './components/NewNote';

class App extends Component {
  constructor() {
    super();
    this.state = {
      notes: [],
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
          // console.log(res)
          this.setState({ notes: res.data })
      })
      .catch(err => {
        console.log(err)
    });
  }

  getRandomColor() {
    let letters = '0123456789ABCDEF';
    let color = '#';
    for (let i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }
  
  render() {
    return (
      <div className="App">
        <NewNote />
        { this.state.notes.map(note => 
          <DisplayNote 
          key={ note.title } 
          note={ note } 
          getRandomColor = { this.getRandomColor }
          />
        )}
      </div>
    );
  }
}

export default App;
