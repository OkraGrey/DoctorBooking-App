import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { loginUser  } from '../redux/features/AuthSlice'
import { useNavigate } from 'react-router-dom'
const Login = () => {
    const [email,setEmail]= useState('')
    const [password,setPassword]= useState('')
    const dispatch=useDispatch()
    const navigate=useNavigate()

    const handleLoginEvent=(e)=>{
        e.preventDefault();
        let userCredentials ={
            email,
            password,

        }
        dispatch(loginUser(userCredentials)).then((rezult)=>{
            setEmail('');
            setPassword('')
            // console.log(rezult.error.message)
            navigate('/')
        }).catch((err)=>{
            console.log("hehe")
        })
    }
  return (
    <div>
        <form onSubmit={handleLoginEvent}>
            <input type="text" name='email' placeholder='Enter email' value={email}
            onChange={(e)=>setEmail(e.target.value)}/>
            <input type="password" name="password" placeholder='Enter Password' value={password}
            onChange={(e)=>setPassword(e.target.value)} />
            <input type="submit" />
        </form>
    </div>
  )
}

export default Login