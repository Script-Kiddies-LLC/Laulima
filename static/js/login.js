import React from 'react';

class Login extends React.Component {
  render() {
    return (
      <div>
        <div className="row" style={{paddingTop: '170px', marginBottom: 0}}>
          <div className="row">
            <div className="col s10 offset-s1 l6 offset-l3 center">
              <h2>Login to Laulima</h2>
            </div>
          </div>
          <form className="col s10 offset-s1 l6 offset-l3" style={{backgroundColor: '#f7f7f7', border: '1px solid #000', paddingTop: '12px'}} name="login" id="login" action="" method="post">
            <div className="row" style={{borderRadius: '5px', border: '1px solid #000'}}>
              <div className="input-field col s12">
                <i className="material-icons prefix">account_circle</i>
                <input name="user_name" id="user_name" type="text" className="validate" />
                <label htmlFor="user_name">User Name</label>
              </div>
            </div>
            <div className="row" style={{borderRadius: '5px', border: '1px solid #000'}}>
              <div className="input-field col s12">
                <i className="material-icons prefix">lock</i>
                <input name="password" id="password" type="password" className="validate" />
                <label htmlFor="password">Password</label>
              </div>
            </div>
            <div id="result"></div>
            <div className="row">
              <button className="btn waves-effect waves-light" type="submit" name="action">Submit
                <i className="material-icons right">send</i>
              </button>
           </div>
          </form>
        </div>
      </div>
    );
  }
}

export default Login;
