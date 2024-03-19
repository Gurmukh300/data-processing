import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";

const krl = process.env.REACT_APP_REST_API_URL;
function App() {
  const [datas, setData] = useState([]);
  const [file, setFile] = useState(null);

  const fetchData = async () => {
    try {
      const result = await axios.get(`${krl}`);

      setData(result.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(`${krl}upload_csv/`, formData);
      console.log(response.data);
    } catch (error) {
      console.error("Error uploading file:", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  return (
    <>
      <div className="App">
        <br/>
        <br/>
        <form onSubmit={handleSubmit}>
          <input type="file" onChange={handleFileChange} />
          <button type="submit">Upload</button>
        </form>
        {datas.length > 0 &&
          datas.map((item, index) => (
            <div key={index}>
              {/* Render each property of the item */}
              <br/>
              <p>ID: {item.id}</p>
              <p>Name: {item.name}</p>
              <p>Birthdate: {item.birthdate}</p>
              <p>Score: {item.score}</p>
              <p>Grade: {item.grade}</p>
              {/* Add more properties as needed */}
            </div>
          ))}
        {/* <button onClick={handleSendData}>Send</button> */}
      </div>
    </>
  );
}

export default App;
