import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

const krl = process.env.REACT_APP_REST_API_URL
function App() {
  const [datas, setData] = useState([]);

  const fetchData = async (e) => {
   
    try {
      const result = await axios.get(`${krl}`);
   
      setData(result.data)
      
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

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
      
     </div>
    </>
  );
}

export default App;
