import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import AppRoot from './AppRoot';
import { BrowserRouter } from 'react-router-dom';
import CaptureEmailUI from './components/emailCap';
import SurveyApp from './components/survey/SurveyApp';
import reportWebVitals from './reportWebVitals';
import 'bootstrap/dist/css/bootstrap.css'

const appRootUi = document.getElementById("root")
if (appRootUi){
  ReactDOM.render(<BrowserRouter><AppRoot /></BrowserRouter>,appRootUi)
}


const surveyUi = document.getElementById("survey-app-ui")
if (surveyUi){
  ReactDOM.render(<BrowserRouter><SurveyApp /></BrowserRouter>,surveyUi)
}


const e = React.createElement;

//<CaptureEmailUI/>

// Find all DOM containers, and render our component into them.
const containers = document.querySelectorAll('.cap-ui')
containers.forEach(domContainer => {
  // render the component into the DOM
  ReactDOM.render(
    e(CaptureEmailUI, { config: domContainer.dataset}),
    domContainer
  )
});

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

