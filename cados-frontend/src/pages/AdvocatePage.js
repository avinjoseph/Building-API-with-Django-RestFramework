import React, {useEffect,useState} from 'react'
import {useParams} from 'react-router-dom'
import axios from 'axios'

const AdvocatePage = () => {
    const params = useParams()
    const username = params.username;

    const [advocate,setAdvocate] = useState(null);

    useEffect(() => {
      getData();
    },[username]); //here username is returned because any time username changes it need to be shown

    let getData = async()=>{
      let response = await axios.get(`https://cados.up.railway.app/advocates/${username}`)
      console.log("This data is the response from axios",response.data.advocate);
      setAdvocate(response.data.advocate)
    }

    // we need to wrap into these literals and check whether the advocate has data or not otherwise it will strike error
  return (
      <>
        {advocate && (
          
          <div className='advocate_preview_wrapper'>
              <img className='advocate_preview_image' src={advocate.profile_pic} />
              <strong>{advocate.name}</strong>
              <a href={advocate.twitter}>@{advocate.username}</a>
              <p>{advocate.bio}</p>                   
          </div>

        )}
        
      </>
  )
}

export default AdvocatePage
