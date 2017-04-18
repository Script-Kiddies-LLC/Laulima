import React from 'react';

class Root extends React.Component {
  render() {
    return (
      <center>
        <div className="row teal accent-3">
          <h1 className="white-text" style={{margin: 0, padding: '10px 0 10px 0'}}> </h1>
        </div>
        <div className="row">
          <div className="sections">
          </div>
          {/* {this.props.body.sections.map(function(e, i) {
            return(
              <div className="col s10 offset-s1 l10 offset-l1">
                <div className="card-panel">
                  <h4 style={{borderBottom: '3px solid #333'}}>{ section.keys()[0] }</h4>
                  <iframe src="{{section.values()[0]['src']}}" frameborder="0" scrolling="no" onload="resizeIframe(this)"></iframe>
                </div>
              </div>
            )
          })
          } */}
        </div>
      </center>
    );
  }
}

export default Root;
