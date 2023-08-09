import React from 'react'
import { useSelector } from 'react-redux'
import { Link } from 'react-router-dom'

const Header = () => {
    // const name = useSelector((store)=>store.AuthSlice.person.name)
    // console.log(name)
  return (
    <div>
        <Link to="/">Home</Link>
        <span>   ||   </span>
        <Link to="/login">Login</Link>
        {/* <p>Hello and welcome Mr.{name}</p> */}
    </div>
  )
}

export default Header