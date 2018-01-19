import React, { Component } from 'react'

import './Todo.css'

export class AddTask extends Component {

  constructor(props) {
    super(props)
    this.addTaskSubmit = this.addTaskSubmit.bind(this)
  }

  addTaskSubmit(e) {
    e.preventDefault()
    this.props.onTaskAdded(e.target.name.value)
    e.target.name.value = ''
  }

  render() {
    return <div className='add-task'>
      <form onSubmit={this.addTaskSubmit}>
        <input
          className='add-task-name'
          type='text'
          name='name'
          placeholder='What needs to be done?'
          size="30"
        />
      </form>
    </div>
  }
}

export class TodoList extends Component {

  deleteTaskClick(itemName){
    this.props.onTaskDeleted(itemName)
  }

  updateItemClick(item){
    this.props.onTaskUpdate(item)
  }

  render() {
    return <div className='tasks'>
      {this.props.items.map((item, i) => 
        <div className='task-item' key={'item-' + i}>
          <div className='task-item-tick' title='click to do or undo a task' onClick={() => this.updateItemClick(item)}>{item.done? '☑': '☐'}</div>
          <div className='task-item-name'>{item.name}</div>
          <div className='task-item-delete' title='click to remove a task from your list' onClick={() => this.deleteTaskClick(item.name)}>x</div>
        </div>
      )}
    </div>
  }
}
