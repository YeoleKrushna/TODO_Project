import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './todo.css';

const Todo = () => {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState({ title: '', description: '' });

  // Fetch todos when the component mounts
  useEffect(() => {
    fetchTodos();
  }, []);

  // Fetch todos from the API
  const fetchTodos = async () => {
    try {
      const response = await axios.get('http://localhost:8000/api/todos/');
      console.log(response.data); // Check if data is being fetched
      setTodos(response.data);
    } catch (error) {
      console.error("Error fetching todos:", error);
    }
  };

  // Add a new todo to the API
  const addTodo = async () => {
    try {
      await axios.post('http://localhost:8000/api/todos/', newTodo);
      fetchTodos();  // Refresh the list after adding
      setNewTodo({ title: '', description: '' }); // Clear input fields
    } catch (error) {
      console.error("Error adding todo:", error);
    }
  };

  // Delete a todo from the API
  const deleteTodo = async (id) => {
    await axios.delete('http://127.0.0.1:8000/todos/${id}/');
    fetchTodos();
};

  return (
    <div className="todo-container">
      <h1>Todo List</h1>
      <input
        type="text"
        placeholder="Title"
        value={newTodo.title}
        onChange={(e) => setNewTodo({ ...newTodo, title: e.target.value })}
      />
      <input
        type="text"
        placeholder="Description"
        value={newTodo.description}
        onChange={(e) => setNewTodo({ ...newTodo, description: e.target.value })}
      />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map(todo => (
          <li key={todo.id}>
            <div>
              <h2>{todo.title}</h2>
              <p>{todo.description}</p>
            </div>
            <button onClick={() => deleteTodo(todo.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Todo;
