import React from 'react'
import '../App.css'
import bg from './images/bg.png';
const Home = () => {
  return (
    <div className='home-layout' style={{ backgroundImage: `url(${bg})` }}>
      <div className='overlay'>
        <h3>SPEAK WITH YOUR HANDS....</h3>
        <h1>SIGN LANGUAGE</h1>
        
        
      </div>
    </div>
  )
}

export default Home