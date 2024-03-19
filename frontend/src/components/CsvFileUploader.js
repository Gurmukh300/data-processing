import React, { useState } from 'react';
import axios from 'axios';
import DataFetcher from './DataFetcher';

const CsvFileUploader = () => {
  const [file, setFile] = useState(null);
  const [uploadError, setUploadError] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [rowsPerPage] = useState(10); // Set the number of rows per page

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
    setUploadError(null);
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    if (!file) {
      setUploadError('Please select a CSV file');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post(`${process.env.REACT_APP_REST_API_URL}upload_csv/`, formData);
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

      <h2 className="text-xl font-semibold mt-8 mb-4">Data Table</h2>
      <DataFetcher>
        {({ data, loading, error }) => (
          <>
            {loading && <p>Loading...</p>}
            {error && <p>Error: {error.message}</p>}
            <table className="table-auto w-full">
              <thead>
                <tr>
                  <th className="border px-4 py-2">Name</th>
                  <th className="border px-4 py-2">Birthdate</th>
                  <th className="border px-4 py-2">Score</th>
                  <th className="border px-4 py-2">Grade</th>
                </tr>
              </thead>
              <tbody>
                {data
                  .slice((currentPage - 1) * rowsPerPage, currentPage * rowsPerPage)
                  .map((row, index) => (
                    <tr key={index}>
                      <td className="border px-4 py-2">{row.name}</td>
                      <td className="border px-4 py-2">{row.birthdate}</td>
                      <td className="border px-4 py-2">{row.score}</td>
                      <td className="border px-4 py-2">{row.grade}</td>
                    </tr>
                  ))}
              </tbody>
            </table>
            <div className="flex justify-center mt-4">
              <button
                onClick={() => setCurrentPage(currentPage - 1)}
                disabled={currentPage === 1}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg mr-2 hover:bg-blue-600"
              >
                Previous
              </button>
              <button
                onClick={() => setCurrentPage(currentPage + 1)}
                disabled={currentPage === Math.ceil(data.length / rowsPerPage)}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
              >
                Next
              </button>
            </div>
            <div className="text-center mt-4">
              Page {currentPage} of {Math.ceil(data.length / rowsPerPage)}
            </div>
          </>
        )}
      </DataFetcher>
    </div>
  );
};

export default CsvFileUploader;
