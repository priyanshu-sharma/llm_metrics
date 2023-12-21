import { useEffect, useState } from "react";
import { getRating } from "../../services/api/metrics-client";
import "./Table.css";

const Table = () => {
  const [isLoading, setIsLoading]: any = useState(true);
  const [response, setResponse]: any = useState("");
  const loadData = async () => {
    const response = await getRating(10);
    console.log(response.data.results);
    setResponse(response.data.results);
    setIsLoading(false);
  };
  useEffect(() => {
    loadData();
  }, []);

  if (isLoading) {
    return <div className="loading-data">Loading Data</div>;
  }
  return (
    <div className="table-view">
      <table>
        <tr>
          <th>Prompt</th>
          <th>Response</th>
          <th>Rating Type</th>
          <th>Models</th>
          <th>Metrics</th>
        </tr>
        {response.map((val: any, key: any) => {
          return (
            <tr key={key}>
              <td>{val.response__prompt__sentence}</td>
              <td>{val.response__result}</td>
              <td>{val.rating_type}</td>
              <td>{val.response__prompt__llm_models}</td>
              <td>{JSON.stringify(val.metrics)}</td>
            </tr>
          );
        })}
      </table>
    </div>
  );
};

export default Table;
