import './App.css';
import Evaluation from './components/Evaluation/Evaluation';
import Table from './components/Table/Table';
import Title from './components/Title/Title';

const App = () => {
  return (
      <div className='base'>
        <Title />
        <Evaluation />
        <Table />
      </div>
  );
};

export default App;
