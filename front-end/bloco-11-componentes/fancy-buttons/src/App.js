import React from 'react';
import './App.css';


class App extends React.Component {
  constructor() {
    super()
    this.handleClick = this.handleClick.bind(this)
    this.state = {
      numeroDeClicks: 0
    }
  }

  handleClick() {
    this.setState((anterior, _props) => ({
      numeroDeClicks: anterior.numeroDeClicks + 1
    }))
  }
  
  render(){
    return (
      <div>
        <button className="App" onClick={this.handleClick}>{this.state.numeroDeClicks}</button>
      </div>
    );
  }
}

export default App;
