import { createAsyncThunk, createSlice } from '@reduxjs/toolkit'
import axios from 'axios'
const initialState = {
    is_loading:false,
    user:null,
    error:null,
}

export const loginUser = createAsyncThunk(
    'auth/loginUser',
    async(userCredentials)=>{

        try {
            const response = await axios.post('http://127.0.0.1:8000/accounts/get_token/', userCredentials);
            // console.log("-----------")
            // console.log(response);
            // console.log("-----------")


            if (response.status == 200) {
                localStorage.setItem('user', JSON.stringify(response.data));
                console.log(response)
                return response.data;
            } else {
                // Handle non-200 status here or throw an error
                console.log("ELSE ERROR")
                throw new Error('Non-200 status received');
            }
        } catch (error) {
            // Handle errors here
            console.log('Error:', error);
        }
        




        // console.log('Inside userCredentials')
        //     const request =null
        //     axios.post('http://127.0.0.1:8000/accounts/get_token/',userCredentials)
        //     .then(response=>{
        //         console.log(response)
        //     })
        //     .catch(error=>{
        //         console.log(error)
        //     })
        

        // console.log(response)
        // console.log("This line is not executing if status is other than 200")
        // console.log(response.status)
        // if(response.status===200){
        //     // localStorage.setItem('user',JSON.stringify(response.data))
        //     return response
        // }
        // else{
        //     alert('Something Went Wronge')
        //     console.log("Something Went fairly  wrong")
        //     return response
        // }
        
    }
)

export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: (builder)=>{
    builder
    .addCase(loginUser.pending,(state)=>{
        console.log("PENDING")
        state.is_loading=true;
        state.user=null;
        state.error=null;
    })
    .addCase(loginUser.rejected,(state,action)=>{
        console.log("INSIDE REJECTED REDUCERS")
        state.pending=false;
        state.user=null;
        console.log(action.error.message)
        if(action.error.message=="Request failed with status code 401")
        {
            state.error = "Access Denied! Invalid Username or Password!"
        }
        else{state.error=action.error.message}
    })
    .addCase(loginUser.fulfilled,(state,action)=>{
        console.log("FULLFILLED")
        state.pending=false;
        state.user=action.payload;
        console.log(state.user)
        state.error=null
    })
   
  }
})
export default authSlice.reducer