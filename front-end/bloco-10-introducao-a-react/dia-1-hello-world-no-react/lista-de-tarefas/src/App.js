import React from 'react';
import './App.css';

const coisasPraFazer = ['arrumar cama','tomar café', 'estudar', 'beber água']

function Task(a) {
  return (
    <li>{a}</li>
  );
}

class Teste extends React.Component {
  render(){
    return coisasPraFazer.map((e) => {
      return Task(e)
    })
  }
}

export default Teste;
