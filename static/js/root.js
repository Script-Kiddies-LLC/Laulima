import React from 'react';
import Nav from './nav/root.js';
import Main from './main/root.js';

class Root extends React.Component {
  constructor(props, context) {
    super(props, context);
    this.state = {
      authenticated: false,
      username: null,
      password: null
    }
    this.loginAuth = this.loginAuth.bind(this);
  };
  loginAuth() {
    console.log('Testing!...');
    console.log($('#username').text())
    console.log($('#password').text())
    fetch('/', {
      'method': 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: $('#username').text(),
        password: $('password').text()
      })
    })
  };
  componentDidMount() {
    console.log(this.state);
  };
  render() {
    return (
      <div>
        <header>
          <Nav />
        </header>
        <main>
          <Main
            authenticated={this.state.authenticated}
            loginAuth={this.loginAuth}
          />
        </main>
        <footer>
        </footer>
      </div>
    );
  }
}

export default Root;
