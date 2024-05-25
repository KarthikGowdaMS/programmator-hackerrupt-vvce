import React, { Component } from "react";
import "../css/searchbar.css";

class Searchbar extends Component {
  render() {
    return (
      <div className="scr-btn">
        <input type="text" placeholder="Search Here..." id="scr"></input>
        <br />
        <button type="submit" id="btn" onClick={() => this.senddata({ id: 1 })}>
          <span>Search</span>
        </button>
      </div>
    );
  }
}

export default Searchbar;