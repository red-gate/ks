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
    this.onTaskDeleted = this.onTaskDeleted.bind(this)
    this.onTaskUpdate = this.onTaskUpdate.bind(this)

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

  onTaskAdded(taskName) {
    const newItem = {
      name: taskName,
      done: false,
      id: Date.now()
    }

    const payload = { newItem }

    fetch('/api/todo/add', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload),
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({ todoItems: json.todoList})
    })
  }

  onTaskUpdate(item){
    const itemToUpdate = this.state.todoItems.find(x => x.id === item.id)
    const copyItem = {...itemToUpdate}
    copyItem.done = !copyItem.done
    const payload = { itemToUpdate: copyItem }

    !!itemToUpdate && fetch('/api/todo/item/update', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({ todoItems: json.todoList})
    })
  }

  onTaskDeleted(taskId) {
    const itemToDelete = this.state.todoItems.find(x => x.id === taskId)
    const payload = { itemToDelete }
    !!itemToDelete && fetch('/api/todo/delete', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    }).then(response => {
      return response.json()
    }).then(json => {
      this.setState({ todoItems: json.todoList})
    })
  }

  render() {
    return <div className='App'>
      <header className='App-header'>
        <h1 className='App-title'>ks8-1 app</h1>
      </header>
      <p className='App-intro'>
        ks8-1 message from web server: {this.state.message}
      </p>
      <AddTask onTaskAdded={this.onTaskAdded} />
      <TodoList
        items={this.state.todoItems}
        onTaskUpdate={this.onTaskUpdate}
        onTaskDeleted={this.onTaskDeleted}/>
    </div>
  }
}

export default App
