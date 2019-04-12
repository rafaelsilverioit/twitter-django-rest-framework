import React from 'react';
import PropTypes from 'prop-types';
import key from "weak-key";


const Table = ({data}) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="container col-md-6">
            <div className="table-responsive">
                <table className="table table-striped table-bordered table-hover">
                    <caption className="text-center">Show more tweets</caption>
                    <thead className="thead-dark">
                        <tr>
                            {Object.entries(data[0]).map(e => {
                                let col = e[0];

                                if(["id", "text", "owner", "is_public", "created_at"].includes(col)) {
                                    switch (col) {
                                        case "id":
                                            col = "#";
                                            break;
                                        case "is_public":
                                            col = "privacy";
                                            break;
                                        case "created_at":
                                            col = "published";
                                            break;
                                        default: break;
                                    }

                                    return <th key={key(e)}>{col}</th>;
                                }

                                return null;
                            })}
                        </tr>
                    </thead>
                    <tbody>
                        {data.map(e => (
                            <tr key={e.id}>
                                {Object.entries(e).map(e => {
                                    if(["id", "text", "owner", "is_public", "created_at"].includes(e[0])) {
                                        let row = e[1];

                                        if(e[0] === "is_public") {
                                            row = row ? "public" : "private";
                                        }

                                        if(e[0] === "created_at") {
                                            let date = new Date(row);
                                            row = date.toLocaleDateString("pt-BR");
                                        }

                                        return <td key={key(e)}>{row}</td>;
                                    }

                                    return null;
                                })}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );

Table.propTypes = {
    data: PropTypes.array.isRequired
};

export default Table;
