import React, { createContext } from 'react'

const defaultValue = {
  numero: 0,
  cores: ['blue', 'red', 'green'],
  corAtual: 'blue'
}

export const context = createContext(defaultValue)

class Provider extends React.Component {
  state = {
    numero: 0,
    cores: ['blue', 'red', 'green'],
    corAtual: 'blue'
  }

  handleOnClick = () => {
    console.log('alo');
    const { numero, cores } = this.state
    this.setState({ numero: numero + 1 })
    this.setState({corAtual: cores[numero] , numero: numero + 1 })
    if (numero === 2) {
      this.setState({numero: 0})
    }
  }


  render() {
    const arquivos = {
      testa: this.handleOnClick,
      info: this.state
    }
    return(
      <context.Provider value={ arquivos }>
        { this.props.children }
      </context.Provider>
    );
  }
}

export default Provider
