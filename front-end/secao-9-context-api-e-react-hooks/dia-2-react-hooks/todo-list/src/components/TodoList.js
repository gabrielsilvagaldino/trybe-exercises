import React, { useContext } from "react";
import { MyContext } from "../context/contexto";

const TodoList = () => {
  const { list } = useContext(MyContext)

  return list.map((e) => 
    <li key={Math.random()}>{
      `Nome: ${e.fullName}, Idade: ${e.yearsOld} anos, Cidade: ${e.city}, Módulo: ${e.modulo}`
    }</li>)
}

export default TodoList