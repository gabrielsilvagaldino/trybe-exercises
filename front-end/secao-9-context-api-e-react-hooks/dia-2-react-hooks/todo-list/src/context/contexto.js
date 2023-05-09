import { createContext, useState } from "react";

export const MyContext = createContext()

const Provider = (props) => {
  const [form, setForm] = useState({
    fullName: '',
    yearsOld: '',
    city: '',
    modulo: '',
  })

  const [list, setList] = useState([])

  const handleOnchange = ({ target }) => {
    setForm((antigo) => ({
      ...antigo, [target.name]: target.value,
    }))
  }

  const handleOnSubmit = (event) => {
    event.preventDefault();
    setList(list.concat(form))
    setForm({
      fullName: '',
      yearsOld: '',
      city: '',
      modulo: form.modulo
    });
  }

  const value = {
    submit: handleOnSubmit,
    change: handleOnchange,
    form,
    list,
  }

  return(
    <MyContext.Provider value={ value }>
      {props.children}
    </MyContext.Provider>
  )
}

export default Provider;
