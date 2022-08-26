import React from "react";
import logo from './logo.svg';
import './App.css';
import axios from "axios";
import Menu from "./components/menu";
import UserList from "./components/users_list";
import Footer from "./components/footer";


class App extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
      const users =response.data
      this.setState({
                    'users': users.results

      })
    })
        .catch(error => console.log(error))

  }
  render(){
    return (
        <div className="container">
          <Menu/>
          <UserList users ={this.state.users}/>
          <Footer/>
        </div>
    )
  }
}

  export default App;
