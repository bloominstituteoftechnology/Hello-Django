import React, { Component } from 'react';

class Note extends Component {
    constructor(props) {
        super(props);
        this.state = {
            toggle: false
        }
    }

    handleClick() {
        this.setState({ toggle: !this.state.toggle })
    }

    render() {
        return (
            <div
            className="note" 
            style={{ "background": this.props.getRandomColor() }}
            onClick={ () => { this.handleClick() }}
            > 
            <h1 className="note__title"> { this.props.note.title } </h1>
            { this.state.toggle ? <div className="note__content"> { this.props.note.content } </div> : null }
            </div>
        )   
    }
}

export default Note;