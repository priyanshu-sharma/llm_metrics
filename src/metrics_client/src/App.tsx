import './App.css';
import EvaluationTitle from './components/Evaluation-Title/Evaluation-Title';
import Metrics from './components/Metrics/Metrics';
import Model from './components/Model/Model';
import Prompt from './components/Prompt/Prompt';
import Title from './components/Title/Title';
import Upload from './components/Upload/Upload';

const App = () => {
  return (
      <div className='base'>
        <Title />
        <EvaluationTitle />
        <Prompt />
        <Metrics />
        <Model />
        <Upload />
      </div>
  );
};

export default App;
