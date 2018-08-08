import React, { Component } from 'react';

class Note extends Component {
    constructor(props) {
        super(props);
        this.state = {
            toggle: true
        }
    }

    handleClick() {
        this.setState({ toggle: !this.state.toggle })
    }

    render() {
        return (
            <div>
                <div
                className="note" 
                style={{ "background": this.props.getRandomColor() }}
                onClick={ () => { this.handleClick() }}
                > 
                <h1 className="note__h1"> { this.props.note.title } </h1>
                { this.state.toggle ? <p className="note__p"> { this.props.note.content } </p> : null }
                </div>
            </div>
        )   
    }
}

export default Note;