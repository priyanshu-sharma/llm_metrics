import "./Evaluation.css";

const Evaluation = () => {
  return (
    <div>
      <div className="evaluation-title">Generate and Evaluate Prompt</div>
      <div className="prompt">
        <div className="prompt-heading">Enter your prompt here</div>
        <div className="prompt-input"></div>
      </div>
      <div className="metrics">
        <div className="metrics-heading">Metrics</div>
        <div className="metrics-selector"></div>
      </div>
      <div className="model">
        <div className="model-heading">LLM Model</div>
        <div className="model-dropdown"></div>
      </div>
      <div className="dataset">
        <div className="dataset-heading">Dataset</div>
        <div className="dataset-dropdown"></div>
      </div>
      <div className="upload-section">
        <div className="upload-button">
          <button className="button">Upload</button>
        </div>
      </div>
    </div>
  );
};

export default Evaluation;
