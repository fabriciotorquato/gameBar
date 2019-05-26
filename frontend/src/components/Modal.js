// frontend/src/components/Modal.js

import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem
    };
  }

  handleChange = e => {
    let { name, value } = e.target;
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }
    const activeItem = { ...this.state.activeItem, [name]: value };
    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;
    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}> Bar</ModalHeader>
        <ModalBody>
          <Form className="bar-form">
            <FormGroup>
              <Label for="name">Nome</Label>
              <Input
                type="text"
                name="name"
                className="input-name"
                value={this.state.activeItem.name}
                onChange={this.handleChange}
                placeholder="Digite o nome do Bar"
              />
            </FormGroup>
            <FormGroup>
              <Label for="description">Descrição</Label>
              <Input
                type="text"
                name="description"
                className="input-description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Digite uma breve descrição"
              />
            </FormGroup>
            <FormGroup>
              <Label for="address">Endereço</Label>
              <Input
                type="text"
                name="address"
                className="input-address"
                value={this.state.activeItem.address}
                onChange={this.handleChange}
                placeholder="Digite o endereço"
              />
            </FormGroup>
            <FormGroup check>
              <Label for="status">
                <Input
                  type="checkbox"
                  name="status"
                  className="input-status"
                  checked={this.state.activeItem.status}
                  onChange={this.handleChange}
                />
                Ativo
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            className="btn-submit"
            color="success"
            onClick={() => onSave(this.state.activeItem)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
