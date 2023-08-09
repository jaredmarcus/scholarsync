import React from 'react';

function UserProfile({ user }) {
    return (
        <div className="profile">
            <h2>{user.name}</h2>
            <p>Qualifications: {user.qualifications}</p>
            <p>Interests: {user.interests}</p>
            <div>
                <h3>Ongoing Projects</h3>
                <ul>
                    {user.projects.map(project => (
                        <li key={project.id}>{project.title}</li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default UserProfile;
