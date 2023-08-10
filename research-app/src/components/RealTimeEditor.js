import React, { useState, useEffect } from 'react';
import { EditorState, convertFromRaw, convertToRaw } from 'draft-js';
import { Editor } from 'react-draft-wysiwyg';
import socket from '../utils/socket';
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';

function RealTimeEditor() {
    const [editorState, setEditorState] = useState(EditorState.createEmpty());

    useEffect(() => {
        socket.on('contentChange', (content) => {
            const newEditorState = EditorState.push(
                editorState,
                convertFromRaw(content)
            );
            setEditorState(newEditorState);
        });

        return () => {
            socket.off('contentChange');
        };
    }, [editorState]);

    const handleEditorChange = (newState) => {
        setEditorState(newState);

        // Emit content changes to other connected users
        const content = newState.getCurrentContent();
        socket.emit('contentChange', convertToRaw(content));
    };

    return (
        <Editor
            editorState={editorState}
            onEditorStateChange={handleEditorChange}
        />
    );
}

export default RealTimeEditor;
