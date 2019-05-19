// frontend/src/App.js

import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      statusAtivo: true,
      activeItem: {
        name: "",
        description: "",
        address: "",
        status: false
      },
      barsList: []
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/bars/")
      .then(res => this.setState({ barsList: res.data }))
      .catch(err => console.log(err));
  };
  displayCompleted = status => {
    if (status) {
      return this.setState({ statusAtivo: true });
    }
    return this.setState({ statusAtivo: false });
  };
  renderTabList = () => {
    return (
      <div className="my-5 tab-list">
        <span
          onClick={() => this.displayCompleted(true)}
          className={this.state.statusAtivo ? "active" : ""}
        >
          Ativo
        </span>
        <span
          onClick={() => this.displayCompleted(false)}
          className={this.state.statusAtivo ? "" : "active"}
        >
          Inativo
        </span>
      </div>
    );
  };
  renderItems = () => {
    const { statusAtivo } = this.state;
    const newItems = this.state.barsList.filter(
      item => item.status === statusAtivo
    );
    return newItems.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2`}
          title={item.description}
        >
          {item.name}

          <span
            className={`todo-title ml-2`}
            title={item.address}
          >
            <b> Endereço:</b>
            {item.address}
          </span >
          <span
            className={`todo-title ml-2`}
            title={item.address}
          >
            <b> Qtd Produtos:</b>
            {item.products.length}
          </span >
          <span
            className={`todo-title ml-2`}
            title={item.address}
          >
            <b> Qtd Games:</b>
            {item.games.length}
          </span >
        </span>

        <span>
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2"
          >
            {" "}
            Editar{" "}
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Deletar{" "}
          </button>
        </span>
      </li >
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/bars/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/bars/", item)
      .then(res => this.refreshList());
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/bars/${item.id}`)
      .then(res => this.refreshList());
  };
  createItem = () => {
    const item = { name: "", description: "", address: "", status: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Game Bar App</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button onClick={this.createItem} className="btn btn-primary">
                  Adicionar bar
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
