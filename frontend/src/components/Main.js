import { Route, NavLink,  HashRouter } from "react-router-dom";
import { Redirect, Switch } from 'react-router'
import React from 'react';
import Home from "./Home";
import Beer from "./beer";
import PageNotFound from "./PageNotFound";

export default class Main extends React.Component {
    render() {
      return (
        <HashRouter>
          
      <div>
      <div className="navbar navbar-inverse">
        <ul className="nav navbar-nav">
              <li><NavLink exact to="/">Home</NavLink></li>
              <li><NavLink exact to="/beer">Beer</NavLink></li>
              {/* <li><NavLink exact to="/search" style={{color:'white'}} activeClassName='wow' activeStyle={{backgroundColor:'#5f6268'}}>Search</NavLink></li> */}
            </ul>
            </div>
            <div className="content">
              <Switch>
                <Route exact path="/" component={Home}/>
                <Route exact path="/events" component={Beer}/>
                <Route component={PageNotFound} />
              </Switch>
            </div>
          </div>
        </HashRouter>
      );
    }
  }