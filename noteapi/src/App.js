import React, { Component } from 'react';
import axios from 'axios';

import './App.css';

class App extends Component {

  componentDidMount() {
    axios.get("https://frozen-ridge-71012.herokuapp.com/api/notes")
    .then(res => {
      console.log(res);
    })
    .catch(err => {
      console.log(err);
    })
  }

  render() {
    return (
      <div className="App">
        
      </div>
    );
  }
}

export default App;
