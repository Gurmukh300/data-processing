import React, { useState } from 'react';
import axios from 'axios';

const krl = process.env.REACT_APP_REST_API_URL;

const CsvFileUploader = () => {
  const [file, setFile] = useState(null);
  const [uploadError, setUploadError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setUploadError(null); // Reset upload error when a new file is selected
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setUploadError('Please select a CSV file');
      return; // Exit function if no file is selected
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${krl}upload_csv/`, formData);
      console.log(response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-8 p-6 bg-white rounded-lg shadow-md">
      <h2 className="text-xl font-semibold mb-4">Upload CSV File</h2>
      <input
        type="file"
        accept=".csv"
        onChange={handleFileChange}
        className="border border-gray-300 px-4 py-2 rounded-lg w-full mb-4"
      />
      {uploadError && (
        <p className="text-red-500 mb-4">{uploadError}</p>
      )}
      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
      >
        Upload
      </button>
    </div>
  );
};

export default CsvFileUploader;
