import { useState } from "react";
import "./Evaluation.css";
import { uploadPrompt } from "../../services/api/metrics-client";

const Evaluation = () => {
  const [prompt, setPrompt]: any = useState("");
  const [metrics, setMetrics]: any = useState("");
  const [dataset, setDataset]: any = useState("");
  const handlePrompt = (event: any) => {
    setPrompt(event.target.value);
  };

  const handleBiasMetrics = (event: any) => {
    setMetrics("['bias']");
  };

  const handleCorrectnessMetrics = (event: any) => {
    setMetrics("['correctness']");
  };

  const handleAllMetrics = (event: any) => {
    setMetrics("['bias', 'correctness']");
  };

  const handleDataset = (event: any) => {
    setDataset(event.target.value);
  };

  const handleUpload = async () => {
    const response = await uploadPrompt(dataset, metrics, prompt);
    console.log(response);
  };

  return (
    <div>
      <div className="evaluation-title">Generate and Evaluate Prompt</div>
      <div className="prompt">
        <div className="prompt-heading">Enter your prompt here</div>
        <div className="prompt-input">
          <textarea
            className="prompt-textarea"
            onChange={handlePrompt}
          ></textarea>
        </div>
      </div>
      <div className="metrics">
        <div className="metrics-heading">Metrics</div>
        <div className="metrics-selector">
          <div className="metrics-checkbox">
            <div className="metrics-bias-checkbox">
              <label>
                <input
                  type="checkbox"
                  value="bias"
                  onChange={handleBiasMetrics}
                ></input>
                Bias
              </label>
            </div>
            <div className="metrics-correctness-checkbox">
              <label>
                <input
                  type="checkbox"
                  value="correctness"
                  onChange={handleCorrectnessMetrics}
                ></input>
                Correctness
              </label>
            </div>
            <div className="metrics-all-checkbox">
              <label>
                <input
                  type="checkbox"
                  value="all"
                  onChange={handleAllMetrics}
                ></input>
                All
              </label>
            </div>
          </div>
        </div>
      </div>
      <div className="model">
        <div className="model-heading">LLM Model</div>
        <div className="model-dropdown">
          <select className="model-select">
            <option value="CHAT_GPT">Chat GPT</option>
            {/* <option value="BARD">Bard</option> */}
          </select>
        </div>
      </div>
      <div className="dataset">
        <div className="dataset-heading">Dataset</div>
        <div className="dataset-dropdown">
          <input
            className="dataset-file"
            type="file"
            onChange={handleDataset}
          ></input>
        </div>
      </div>
      <div className="upload-section">
        <div className="upload-button">
          <button className="button" onClick={handleUpload}>
            Upload
          </button>
        </div>
      </div>
    </div>
  );
};

export default Evaluation;
