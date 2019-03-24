import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";


const App =() => (
    <React.Fragment>
        <DataProvider endpoint="api/v1/tweet/"
                      render={data => <Table data={data.results} />} />
        
        <Form endpoint="api/v1/tweet/" />
    </React.Fragment>
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
