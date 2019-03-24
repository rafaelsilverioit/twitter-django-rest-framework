import React, { Component } from 'react';
import PropTypes from 'prop-types';


class Form extends Component {
    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };

    state = {
        text: "",
        isPublic: false
    };

    handleChange = e => {
        this.setState({[e.target.name]: e.target.value});
    };

    handleSubmit = e => {
        e.preventDefault();

        const {text, isPublic} = this.state;

        const tweet = {text, isPublic};
        const conf = {
            method: "post",
            body: JSON.stringify(tweet),
            headers: new Headers({"Content-Type": "application/json"})
        };

        fetch(this.props.endpoint, conf)
            .then(res => console.log(res))
            .catch(err => console.err(err));
    };
        
    render() {
        const {text, isPublic} = this.state;

        return (
            <div className="column">
                <form onSubmit={this.handleSubmit}>
                    <div className="field">
                        <label className="label">Text</label>
                        <div className="control">
                            <input
                                className="input"
                                type="text"
                                name="text"
                                onChange={this.handleChange}
                                defaultValue={text}
                                required
                            />
                        </div>
                    </div>

                    <div className="field">
                        <label className="label">Público</label>
                        <div className="control">
                            <input
                                className="radio"
                                type="radio"
                                name="isPublic"
                                onChange={this.handleChange}
                                defaultValue={isPublic}
                                required
                            />
                        </div>
                    </div>

                    <div className="control">
                        <button type="submit" className="button is-info">
                            Tweet
                        </button>
                    </div>
                </form>
            </div>
        );
    }
}

export default Form;
