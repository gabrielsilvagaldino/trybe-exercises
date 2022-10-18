import React, { useContext } from 'react'; 
import { MyContext } from '../context/contexto';

const TodoForm = (props) => {

  const { submit, change, form } = useContext(MyContext)

  return(
    <form onSubmit={ submit }>
      <label htmlFor='fullName'>
        Nome:
        <input name='fullName' onChange={ change } value={form.fullName} type='text' placeholder='Nome'/>  
      </label>
      <br/>
      <label htmlFor='yearsOld'>
        Idade:
        <input name='yearsOld' onChange={ change } value={form.yearsOld} type='number' placeholder='Idade'/>  
      </label>
      <br/>
      <label htmlFor='city'>
        Cidade:
        <input name='city' onChange={ change } value={form.city} type='text' placeholder='Cidade'/>  
      </label>
      <br/>
      <label>
        <input name='modulo' onChange={ change } type='radio' value='Fundamentos'/>
        Fundamentos
      </label>
      <br/>
      <label>
        <input name='modulo' onChange={ change } type='radio' value='Front-end'/>
        Front-end
      </label>
      <br/>
      <label>
        <input name='modulo' onChange={ change } type='radio' value='Back-end'/>
        Back-end
      </label>
      <br/>
      <label>
        <input name='modulo' onChange={ change } type='radio' value='Ciência da Computação'/>
        Ciência da Computação
      </label>

      <button type='submit'>
        Cadastrar
      </button>
    </form>
  )
}

export default TodoForm
