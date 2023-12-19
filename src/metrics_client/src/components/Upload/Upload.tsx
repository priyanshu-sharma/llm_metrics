import UploadButton from '../Upload-Button/Upload-Button';
import './Upload.css';

const Upload = () => {
    return (
        <div className='upload-section'>
            <div className='upload-text'>Upload the prompt here</div>
            <div className='upload-button'><UploadButton /></div>
        </div>
    )
}

export default Upload;