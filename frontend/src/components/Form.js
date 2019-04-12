import React, { Component } from 'react';
import PropTypes from 'prop-types';


class Form extends Component {
    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };

    state = {
        text: "",
        is_public: false
    };

    handleChange = e => {
        let val = e.target.value;

        if(e.target.name === "isPublic") {
            val = val == 'true';
        }

        this.setState({[e.target.name]: val});
    };

    handleSubmit = e => {
        e.preventDefault();

        const {text, is_public} = this.state;

        const tweet = {text, is_public};

        const conf = {
            method: "post",
            body: JSON.stringify(tweet),
            headers: new Headers({"Content-Type": "application/json"})
        };

        fetch(this.props.endpoint, conf)
            .then(res => console.log(res))
            .catch(err => console.error(err));
    };
        
    render() {
        return (
            <div className="container col-md-6" style={{paddingTop: 30}}>
                <div className="column">
                    <form onSubmit={this.handleSubmit}>
                        <div className="form-group">
                            <div className="control">
                                <textarea
                                    className="form-control"
                                    name="text"
                                    onChange={this.handleChange}
                                    defaultValue="What are you up to?"
                                    cols={50}
                                    rows={7}
                                    minLength={1}
                                    maxLength={250}
                                    required
                                />
                            </div>
                        </div>
                        <div className="form-group">
                            <select
                                className="custom-select col-sm-3 pull-left"
                                id="is_public"
                                name="is_public"
                                onChange={this.handleChange}
                                required>
                                <option value="true" defaultChecked>Público</option>
                                <option value="false">Privado</option>
                            </select>

                            <label htmlFor="isPublic" className="label col-sm-5 text-left">
                                <i className="fas fa-globe-americas" />
                            </label>

                            <button type="submit" className="btn btn-primary col-sm-4 pull-right">
                                <i className="fab fa-twitter" /> Tweet
                            </button>
                        </div>

                    </form>
                </div>
            </div>
        );
    }
}

export default Form;
