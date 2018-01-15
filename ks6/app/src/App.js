import React, { Component } from 'react'
import './App.css'
import 'whatwg-fetch'

class App extends Component {

  constructor(props){
    super(props)
    this.state= { message: 'moon'}
    this.fetchMessage()
  }

  fetchMessage(){
    fetch('/api/hello', {
      headers: {
        "Content-Type": "application/json"
      }
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({message: json.message})
    })
  }

  render() {
    return <div className="App">
        <header className="App-header">
          <h1 className="App-title">ks7 app</h1>
        </header>
        <p className="App-intro">
          ks6 app here...
          hello {this.state.message}
        </p>
      </div>
  }
}

export default App
