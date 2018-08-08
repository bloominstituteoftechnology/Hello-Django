import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
// import ApolloClient from 'apollo-boost';
import axios from 'axios';

axios.get('http://localhost:8000/graphql/?query=%7B%0A%20%20notes%20%7B%0A%20%20%20%20id%0A%20%20%20%20title%0A%20%20%20%20content%0A%20%20%7D%0A%7D%0A&operationName=null')
.then (response => console.log(response.data.data.notes));
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
// import gql from 'graphql-tag';

// const client = new ApolloClient ({
//     uri: "http://localhost:8000/graphql/"
// });

// client
//     .query({
//         query: gql` {
//                 notes {
//                 id 
//                 title
//                 content
//             }
//         }
//         `
//     })

// .then(result => console.log(result));