import './Table.css';
import { useState, useEffect } from "react";
import { getRating } from "../../services/api/metrics-client";

const Table = () => {
    const [isLoading, setIsLoading]: any = useState(true);

    const loadData = async () => {
        const response = await getRating(10);
        console.log(response);
        setIsLoading(false);
    }
    useEffect(() => {
        loadData();
      }, []);
    
      if (isLoading) {
        return <div className='loading-data'>Loading Data</div>;
      }
    return (
        <div className='table'>Hello World</div>
    )
}

export default Table;