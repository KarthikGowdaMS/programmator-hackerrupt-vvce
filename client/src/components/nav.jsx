import React, { Component } from "react";
import "../css/nav.css";
class NavBar extends Component {
  state = {};
  render() {
    return (
      <div className="nav-div">
        <div className="clr">
          <nav className="navbar">
            <h2 class="title">Know Your Drug</h2>
          </nav>
        </div>
      </div>
    );
  }
}

export default NavBar;