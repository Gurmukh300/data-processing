import { useState, useEffect } from "react";
import axios from "axios";

const DataFetcher = ({ children }) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
        try {
            const response = await axios.get(process.env.REACT_APP_REST_API_URL);
            setData(response.data);
        } catch (error) {
            setError(error);
        } finally {
            setLoading(false);
        }
        };

        fetchData();
    }, []);

    return children({ data, loading, error });
};

export default DataFetcher;
