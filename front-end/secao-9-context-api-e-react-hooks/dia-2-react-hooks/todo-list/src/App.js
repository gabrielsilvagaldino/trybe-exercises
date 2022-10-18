import React from "react";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";

function App() {
  return (
    <div>
      <TodoForm />
      <ul>
        <TodoList/>
      </ul>
    </div>
  );
}

export default App;
