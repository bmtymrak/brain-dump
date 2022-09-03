import React, { useState, useEffect } from 'react';
import Note from './Note.js'


function App(){

    const [notes, setNotes] = useState([]);

    useEffect(() => {
        fetch('notes/')
        .then((response) => response.json())
        .then((data)=>setNotes(data))
    }, [])
    
    return(
        <div>
            <h1>Brain Dump</h1>
            {notes.map((note, index) =>(
                <Note key={index} note={note}/>
            ))}
        </div>
    )
}

export default App;