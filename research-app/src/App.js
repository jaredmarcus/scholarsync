import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Navigation from './components/Navigation';
import UserProfile from './components/UserProfile';
import ProjectManagement from './components/ProjectManagement';
import DocumentEditor from './components/DocumentEditor';

import './App.css';

function App() {
    // Mock user data for demonstration
    const user = {
        name: "John Doe",
        qualifications: "PhD in Machine Learning",
        interests: "Deep Learning, Computer Vision",
        projects: [
            { id: 1, title: "Research on Neural Networks" },
            { id: 2, title: "Study of GPT Models" }
        ]
    };

    return (
        <Router>
            <div className="App">
                <Navigation />

                <Switch>
                    <Route path="/profile">
                        <UserProfile user={user} />
                    </Route>
                    <Route path="/projects">
                        <ProjectManagement />
                    </Route>
                    <Route path="/document-editor">
                        <DocumentEditor />
                    </Route>
                    <Route path="/">
                        {/* Home page, can be a Dashboard or something similar */}
                        <h1>Welcome to ResearchApp</h1>
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}

export default App;
