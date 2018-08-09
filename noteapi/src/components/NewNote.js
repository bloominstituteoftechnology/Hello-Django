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
}

export default NewNote;