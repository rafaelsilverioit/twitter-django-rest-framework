import React from 'react';
import PropTypes from 'prop-types';
import key from "weak-key";


const Table = ({data}) =>
    !data.length ? (
        <p>Nothing to show</p>
    ) : (
        <div className="column">
            <h2 className="subtitle">
                Showing <strong>{data.length} tweets</strong>
            </h2>

            <table className="table is-striped">
                <thead>
                    <tr>
                        {Object.entries(data[0]).map(e => <th key={key(e)}>{e[0]}</th>)}
                    </tr>
                </thead>
                <tbody>
                    {data.map(e => (
                        <tr key={e.id}>
                            {Object.entries(e).map(e => <td key={key(e)}>{e[1]}</td>)}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );

Table.propTypes = {
    data: PropTypes.array.isRequired
};

export default Table;
