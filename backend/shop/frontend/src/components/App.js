import React, { Component} from "react";
import { Switch, Route, Link } from "react-router-dom";
import Login from "./login";
import Signup from "./signup";
import Hello from "./hello";

import axiosInstance from "../axiosApi";


class App extends Component {

    constructor() {
        super();
        this.handleLogout = this.handleLogout.bind(this);
    }

    async handleLogout() {
        try {
            const response = await axiosInstance.post('/blacklist/', {
                "refresh_token": localStorage.getItem("refresh_token")
            });
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
            axiosInstance.defaults.headers['Authorization'] = null;
            return response;
        }
        catch (e) {
            console.log(e);
        }
    };

    render() {
        return (

                        <div className="site">
                 {/*<nav>*/}
                 {/*    <Link className={"nav-link"} to={"/"}>Home</Link>*/}
                 {/*    <Link className={"nav-link"} to={"/login/"}>Login</Link>*/}
                 {/*    <Link className={"nav-link"} to={"/signup/"}>Signup</Link>*/}
                 {/*    <Link className={"nav-link"} to={"/hello/"}>Hello</Link>*/}
                 {/*    <button onClick={this.handleLogout}>Logout</button>*/}
                 {/*</nav>*/}
                            <nav className="navbar navbar-default navbar-static-top">
                                <div className="container">
                                    <div className="navbar-header">
                                        {/*<button type="button" className="navbar-toggle" data-toggle="collapse"*/}
                                        {/*        data-target=".navbar-collapse" onClick={this.handleLogout}>*/}
                                        {/*    Logout*/}
                                        {/*</button>*/}


                                    <ul className="nav navbar-nav navbar-right collapse navbar-collapse">
                                        <li className="active"><Link className={"nav-link"} to={"/"}>Home</Link></li>
                                        <li><Link className="icon-bar" to={"/login/"}>Login</Link></li>
                                        <li><Link className="icon-bar" to={"/signup/"}>Signup</Link></li>
                                        <li><Link className="icon-bar" to={"/hello/"}>Hello</Link></li>
                                        <li><button  class="logout" onClick={this.handleLogout}>Logout</button></li>
                                    </ul>
                                        </div>
                                </div>
                            </nav>

                            <main>
                     <h1>Ahhh after 10,000 years I'm free. Time to conquer the Earth!</h1>

                     <Switch>
                         <Route exact path={"/login/"} component={Login}/>
                         <Route exact path={"/signup/"} component={Signup}/>
                         <Route exact path={"/hello/"} component={Hello}/>
                         <Route path={"/"} render={() => <div>Home again</div>}/>
                     </Switch>
                 </main>
             </div>
        );
    }
}

export default App;