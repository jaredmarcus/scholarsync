import React, { useState } from 'react';
import { EditorState } from 'draft-js';
import { Editor } from 'react-draft-wysiwyg';
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';

function DocumentEditor() {
    const [editorState, setEditorState] = useState(() => EditorState.createEmpty());

    return (
        <div className="document-editor">
            <Editor
                editorState={editorState}
                onEditorStateChange={setEditorState}
            />
            {/* Logic to save content, handle edits, etc. */}
        </div>
    );
}

export default DocumentEditor;
