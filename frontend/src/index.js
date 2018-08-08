import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import ApolloClient from 'apollo-boost';
import gql from 'graphql-tag';

const client = new ApolloClient ({
    uri: "http://localhost:8000/graphql/"
});

client
    .query({
        query: gql` {
                notes {
                id 
                title
                content
            }
        }
        `
    })

.then(result => console.log(result));

ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
