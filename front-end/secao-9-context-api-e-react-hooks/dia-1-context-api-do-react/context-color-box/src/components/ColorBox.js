// ./components/ColorBox.js
import React from 'react';
import '../styles/box.css';
import { context } from './MyContext';
class ColorBox extends React.Component {
  render() {
    const { testa, info } = this.context
    return(
      <button
        type="button"
        className="box"
        onClick={testa}
        style={ { backgroundColor: info.corAtual } }
      >
        Click me to change my color!
      </button>
    )
  }
}

ColorBox.contextType = context;

export default ColorBox;