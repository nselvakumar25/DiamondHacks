my-react-app/
├── src/
│   ├── components/
│   │   └── Elections.js
│   ├── App.js
│   └── index.js
├── package.json
└── ...
    
import React, { useState, useEffect } from 'react';

const Elections = () => {
    const [elections, setElections] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch('/api/elections')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setElections(data.elections);
                setLoading(false);
            })
            .catch(error => {
                setError(error.toString());
                setLoading(false);
            });
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Upcoming Elections</h1>
            <ul>
                {elections.map(election => (
                    <li key={election.id}>{election.name} - {election.electionDay}</li>
                ))}
            </ul>
        </div>
    );
};

export default Elections;
