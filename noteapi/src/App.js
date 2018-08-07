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

    const optionTwo = {
        method: 'GET',
        headers: { 'content-type': 'application/json', 'Authorization': token },
        url: "https://frozen-ridge-71012.herokuapp.com/api/notes/",
    }

    axios(optionTwo)
        .then(res => {
            console.log(res)
            this.setState({ data: res.data })
        })
        .catch(err => {
          console.log(err)
        });
}

  render() {
    return (
      <div className="App">
        <div>{ this.state.data.map(note => {
          return <div> (
            Title: { note.title } Content: { note.content }
          )
            </div>
        }) }</div>
      </div>
    );
  }
}

export default App;
