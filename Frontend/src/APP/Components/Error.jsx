function Error(props) {
    const { errorMessage = null } = props;
  
    if (!errorMessage) {
      return null;
    }
  
    return (
      <div className="error-class">
        <h3 className="error-title">Error!</h3>
        <p className="error-message">{errorMessage}</p>
      </div>
    );
  }
  
  export default Error;