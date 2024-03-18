import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

const krl = process.env.REACT_APP_REST_API_URL
function App() {
  const [datas, setData] = useState([]);

  const fetchData = async () => {
   
    try {
      const result = await axios.get(`${krl}`);
   
      setData(result.data)
      
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const postData = async () => {
    const name = "test z"
    const birthdate = "2000-09-09"
    const score = 5
    const grade = "L"
    const body = {name,birthdate,score,grade}
    const response = await axios.post(krl, body)
    console.log(response)
    return response.data
  }

  const handleSendData = async()=> {
    const newData = await postData()
    if (newData) {
      setData(prevState => [...prevState, newData])
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
     <div className="App">
       {datas.length > 0 &&
         datas.map((item, index) => (
           <div key={index}>
             {/* Render each property of the item */}
             <p>ID: {item.id}</p>
             <p>Name: {item.name}</p>
             {/* Add more properties as needed */}
           </div>
         ))}
      <button onClick={handleSendData}>Send</button>
     </div>
    </>
  );
}

export default App;
