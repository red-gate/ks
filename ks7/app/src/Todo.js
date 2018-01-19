import React, { Component } from 'react'

export class AddTask extends Component {

  constructor(props) {
    super(props)
    this.addTaskSubmit = this.addTaskSubmit.bind(this)
  }

  addTaskSubmit(e) {
    e.preventDefault()
    this.props.onTaskAdded(e.target.name.value)
  }

  render() {
    return <div className='add-task'>
      <form onSubmit={this.addTaskSubmit}>
        <input type='text' name='name' placeholder='What needs to be done?' />
      </form>
    </div>
  }
}

export class TodoList extends Component {

  deleteTaskClick(itemName){
    this.props.onTaskDeleted(itemName)
  }
  
  render() {
    return <div className='tasks'>
      <ul>
        {this.props.items.map((item, i) => 
          <li key={'item-' + i}>{item.name} <div onClick={() => this.deleteTaskClick(item.name)}>x</div></li>
        )}
      </ul>
    </div>
  }
}
