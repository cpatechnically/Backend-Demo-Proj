import React, {Component} from 'react';
import { project_details, app_config } from './data/config.json'
import {Route,Switch, Redirect} from 'react-router-dom';
import SurveyApp from './components/survey/SurveyApp';
import PostsApp from './components/posts/PostsApp';
import CaptureEmailUI from './components/emailCap';
import NotFound from './components/common/pages/notFound';
import AppHome from './components/common/pages/home';
import NavBar from './components/common/navbar';
let paths = app_config['webapp_config']['sitemap']["paths"]

class AppRoot extends Component {
    state = {
        rootUrl:"",
        appconfig:[],
        appPaths:[],
        chartData:[],
      }
    
      componentDidMount() {
        const appconfig = project_details
        const appPaths = paths
        this.setState({appPaths,appconfig})
        console.log("mounted appPaths",appPaths,"appconfig",appconfig)
        console.log('props',this.props)
      }
    
      handleRouteComponent = (path) => {
        console.log(path)
      }
    handleRouteComponent = (path) => {
        console.log(path)
    }
    render() { 
        const {appPaths, appconfig} = this.state
        
    return (
        <div>
            <div className="container-fluid">
                <NavBar 
                    navlinks={appPaths}
                    appconfig={appconfig}
                />
            </div>
            <div className="container sub-nav">
                <h1>AppRoot</h1>
            </div>
            <div className="container content-container">
                <Switch>
                    {/* <Route path={`/resources`} component={CodeRefApp} /> */}
                    <Route path={`/survey`} component={SurveyApp} />
                    <Route path={`/emailcap`} component={CaptureEmailUI} />
                    <Route path={`/posts`} component={PostsApp} />
                    {/* <Route path={`${djUrl}/`} ROUTE PROPS/PASSING PROPS
                        render={(props) => <AppHome homeUrl="/analytics" {...props} />} 
                    /> */}
                    <Route path={'/'} component ={AppHome} />
                    <Route path={'/not-found'} component={NotFound} />
                    <Redirect from='/' exact to={`/`} />
                    <Redirect to={`/not-found`} />
                </Switch>
            </div>
        </div>
        );
    }
}
export default AppRoot;
