import React, { Component } from 'react'
import Form from './Form';
import DataProvider from './DataProvider';
import Table from "./Table";


class Home extends Component { 
    render() {
        return (
            <div>
                <Form endpoint="api/v1/tweet/" />
                <br />
                <DataProvider endpoint="api/v1/tweet/"
                        render={data => <Table data={data.results} />} />
            </div>
        );
    }
}

export default Home;