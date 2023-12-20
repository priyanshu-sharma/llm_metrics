import './App.css';
import Evaluation from './components/Evaluation/Evaluation';
import Title from './components/Title/Title';

const App = () => {
  return (
      <div className='base'>
        <Title />
        <Evaluation />
      </div>
  );
};

export default App;
