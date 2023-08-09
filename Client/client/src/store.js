import { configureStore } from '@reduxjs/toolkit'
import AuthSlice from './redux/features/AuthSlice'
export const store = configureStore({
  reducer: {
    auth:AuthSlice
},
})