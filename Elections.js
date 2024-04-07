// src/components/Elections.js

import React, { useState, useEffect } from 'react';

const Elections = () => {
    const [elections, setElections] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchElections = async () => {
            try {
                const response = await fetch('/api/elections');
                if (!response.ok) {
                    throw new Error('Failed to fetch');
                }
                const data = await response.json();
                setElections(data.elections);
            } catch (error) {
                setError(error.toString());
            } finally {
                setLoading(false);
            }
        };

        fetchElections();
    }, []);

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;

    return (
        <div>
            <h1>Upcoming Elections</h1>
            <ul>
                {elections.map((election) => (
                    <li key={election.id}>{election.name} - {election.electionDay}</li>
                ))}
            </ul>
        </div>
    );
};

export default Elections;
