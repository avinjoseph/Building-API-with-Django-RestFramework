import React, {useEffect,useState} from 'react'
import axios from 'axios'

const HomePage = () => {

    const [advocates, setAdvocates] = useState([])

    useEffect(() =>{
        getData()
    },[])

    let getData = async() =>{
        let response = await axios.get('http://127.0.0.1:8000/advocates/')
        console.log(response.data)
        setAdvocates(response.data)
    }

  return (
    <div>
        <h1>Home Page</h1>
        <div>
            {advocates.map((advocate,index) =>{
                return <div key={index}>
                    <strong>{advocate.name}</strong>
                </div>
            })}
        </div>
    </div>
  )
}

export default HomePage
