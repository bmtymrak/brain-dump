import React, {useState} from 'react'

function Note(props){

    return(
        <div>
            <p>{props.note.content}</p>
        </div>
    )
}

export default Note