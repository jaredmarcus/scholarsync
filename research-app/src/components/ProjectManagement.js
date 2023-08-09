import React, { useState } from 'react';

function ProjectManagement() {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = () => {
        // Logic to send the title and description to backend
    };

    return (
        <div className="project-management">
            <h2>Manage Projects</h2>
            <form onSubmit={handleSubmit}>
                <input
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Project Title"
                />
                <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    placeholder="Project Description"
                />
                <button type="submit">Create Project</button>
            </form>
        </div>
    );
}

export default ProjectManagement;
