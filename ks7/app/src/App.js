import React, { Component } from 'react'
import './App.css'
import 'whatwg-fetch'

import { AddTask, TodoList } from './Todo'

class App extends Component {

  constructor(props) {
    super(props)
    this.state = {
      message: 'moon',
      todoItems: []
    }

    this.onTaskAdded = this.onTaskAdded.bind(this)

    this.fetchMessage()
    this.fetchTodoItems()
  }

  fetchTodoItems(){
    fetch('/api/todo/list', {
      'Content': 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({ todoItems: json.todoList})
    })
  }

  fetchMessage() {
    fetch('/api/hello', {
      'Content': 'GET',
      headers: {
        'Content-Type': 'application/json'
      }
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({ message: json.message })
    })
  }

  onTaskAdded(taksName) {
    const newItem = {
      name: taksName,
      done: false
    }

    this.setState({
      todoItems: this.state.todoItems.concat(newItem)
    })
  }

  render() {
    return <div className="App">
      <header className="App-header">
        <h1 className="App-title">ks7 app</h1>
      </header>
      <p className="App-intro">
        ks7 app here...
          hello {this.state.message}
      </p>
      <AddTask onTaskAdded={this.onTaskAdded} />
      <TodoList items={this.state.todoItems} />
    </div>
  }
}

export default App
